"""
split_finalizer.py — Multi-chunk report generation for PRISM

Splits long reports into 4000-token chunks, generates each with shared context,
and concatenates with structural healing.

Triggered by report-finalizer skill when target output > 8000 tokens.
"""

from __future__ import annotations

import asyncio
import logging
import re
from dataclasses import dataclass, field
from typing import Any

from anthropic import AsyncAnthropic

logger = logging.getLogger(__name__)

CHUNK_MAX_TOKENS = 4000
SAFE_OVERLAP_SUMMARY_TOKENS = 300


@dataclass
class SectionPlan:
    """One section in the final report."""
    id: str
    title: str
    estimated_tokens: int
    content_hints: str = ""


@dataclass
class ChunkPlan:
    """A group of sections to generate in one model call."""
    index: int
    sections: list[SectionPlan]
    estimated_tokens: int = 0
    previous_summary: str = ""

    def __post_init__(self) -> None:
        if not self.estimated_tokens:
            self.estimated_tokens = sum(s.estimated_tokens for s in self.sections)


def group_sections_into_chunks(
    sections: list[SectionPlan],
    chunk_budget: int = CHUNK_MAX_TOKENS,
) -> list[ChunkPlan]:
    """Greedy bin-packing of sections into chunks under token budget."""
    chunks: list[ChunkPlan] = []
    current: list[SectionPlan] = []
    current_total = 0

    for sec in sections:
        if sec.estimated_tokens > chunk_budget:
            logger.warning(
                "Section %s estimated at %d tokens exceeds chunk budget %d. "
                "Will generate alone and may still truncate.",
                sec.id, sec.estimated_tokens, chunk_budget,
            )
            if current:
                chunks.append(ChunkPlan(len(chunks), current))
                current, current_total = [], 0
            chunks.append(ChunkPlan(len(chunks), [sec]))
            continue

        if current_total + sec.estimated_tokens > chunk_budget and current:
            chunks.append(ChunkPlan(len(chunks), current))
            current, current_total = [], 0

        current.append(sec)
        current_total += sec.estimated_tokens

    if current:
        chunks.append(ChunkPlan(len(chunks), current))

    return chunks


async def generate_chunk(
    client: AsyncAnthropic,
    chunk: ChunkPlan,
    editor_output: str,
    system_prompt: str,
    model: str,
    is_first: bool,
    is_last: bool,
) -> str:
    """Generate one chunk's HTML."""
    section_brief = "\n".join(
        f"- {s.id}: {s.title} (~{s.estimated_tokens} tokens)" for s in chunk.sections
    )

    position_hint = (
        "This is the FIRST chunk. Open document structure but DO NOT close <body> or <html>."
        if is_first
        else "This is the FINAL chunk. Close all open structural tags."
        if is_last
        else "This is a MIDDLE chunk. Do not open or close <body>/<html>. Just emit the sections."
    )

    user_msg = f"""
Editor output (full report material):
---
{editor_output}
---

Generate ONLY the following sections for this chunk:
{section_brief}

{position_hint}

{f"Previous chunk ended with: {chunk.previous_summary}" if chunk.previous_summary else ""}

Use v5 CSS classes: .metric-card, .fact-badge, .est-badge, .out-badge,
.synergy-block, .bottleneck-block, .principle-block.

Output ONLY the HTML for the assigned sections. No commentary, no markdown fences.
""".strip()

    response = await client.messages.create(
        model=model,
        max_tokens=CHUNK_MAX_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": user_msg}],
    )

    return response.content[0].text


def summarize_for_next_chunk(html: str, max_chars: int = 600) -> str:
    """Extract last paragraph or section heading for continuity context."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text[-max_chars:] if len(text) > max_chars else text


def heal_html_structure(parts: list[str]) -> str:
    """Concatenate chunks and fix common structural issues."""
    joined = "\n".join(parts)

    # Dedupe section IDs (rare, but possible if model regenerates)
    seen_ids: set[str] = set()
    def replace_id(match: re.Match[str]) -> str:
        full_id = match.group(1)
        if full_id in seen_ids:
            new_id = f"{full_id}-dup{len(seen_ids)}"
            seen_ids.add(new_id)
            return f'id="{new_id}"'
        seen_ids.add(full_id)
        return match.group(0)
    joined = re.sub(r'id="([^"]+)"', replace_id, joined)

    # Balance open/close counts for major tags
    for tag in ("div", "section", "table", "tr", "td"):
        opens = len(re.findall(rf"<{tag}[\s>]", joined))
        closes = len(re.findall(rf"</{tag}>", joined))
        if opens > closes:
            joined += f"\n{'</' + tag + '>' * (opens - closes)}"
            logger.warning("Added %d missing </%s> tags during heal", opens - closes, tag)

    return joined


async def split_finalize(
    editor_output: str,
    target_sections: list[SectionPlan],
    system_prompt: str,
    client: AsyncAnthropic | None = None,
    model: str = "claude-sonnet-4-20250514",
    chunk_max_tokens: int = CHUNK_MAX_TOKENS,
) -> dict[str, Any]:
    """
    Main entry point. Generates a long report in chunks and returns
    {html, chunks_count, healed, audit}.
    """
    client = client or AsyncAnthropic()
    chunks = group_sections_into_chunks(target_sections, chunk_max_tokens)

    logger.info("Split-finalize: %d sections → %d chunks", len(target_sections), len(chunks))

    rendered: list[str] = []
    for i, chunk in enumerate(chunks):
        if i > 0:
            chunk.previous_summary = summarize_for_next_chunk(rendered[-1])
        html = await generate_chunk(
            client=client,
            chunk=chunk,
            editor_output=editor_output,
            system_prompt=system_prompt,
            model=model,
            is_first=(i == 0),
            is_last=(i == len(chunks) - 1),
        )
        rendered.append(html)
        logger.info("Chunk %d/%d generated (%d chars)", i + 1, len(chunks), len(html))

    final_html = heal_html_structure(rendered)

    return {
        "html": final_html,
        "chunks_count": len(chunks),
        "healed": True,
        "audit": {
            "sections": [s.id for s in target_sections],
            "chunk_token_estimates": [c.estimated_tokens for c in chunks],
        },
    }


if __name__ == "__main__":
    # Smoke test
    sections = [
        SectionPlan(id=f"sec-{i}", title=f"Section {i}", estimated_tokens=800)
        for i in range(12)
    ]
    chunks = group_sections_into_chunks(sections)
    print(f"12 sections × 800 tok → {len(chunks)} chunks")
    for c in chunks:
        print(f"  Chunk {c.index}: {len(c.sections)} sections, ~{c.estimated_tokens} tok")
