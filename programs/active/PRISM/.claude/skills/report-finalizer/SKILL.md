---
name: report-finalizer
description: |
  Use this skill when finalizing PRISM reports, fixing truncated reports, or
  generating multi-section R&D analysis output that risks exceeding model token
  limits. Triggers on: "PRISM finalize", "보고서 마무리", "report truncated",
  "report cut off", "보고서 잘림", "finalizer 수정", "split report", "long report
  generation", "max_tokens 부족", any task involving the Finalizer step of the
  PRISM Draft→Review→Edit→Final pipeline. Use proactively when generating any
  R&D report longer than ~2000 words — the truncation risk is real and confirmed.
---

# Report Finalizer

Fixes PRISM's confirmed root cause of report truncation (`max_tokens` too low on
final Claude call) and provides split-generation logic for reports longer than
a single completion can produce.

## When this triggers

- PRISM pipeline final step where Claude produces the user-facing HTML report
- Any standalone R&D report generation where output > 2000 words is expected
- Investigation of "report cut off mid-sentence" symptoms

## Procedure

### Step 1 — Estimate output length

Before calling the final model, estimate target output tokens:

| Report tier | Sections | Estimated tokens | Strategy |
|---|---|---|---|
| Short | 3–5 | ≤ 4000 | Single call, `max_tokens=4000` |
| Standard | 6–10 | 4000–8000 | Single call, `max_tokens=8000` |
| Long | 11–20 | 8000–16000 | **Split generation required** |
| Comprehensive | 20+ | > 16000 | **Split + concatenation** |

Heuristic: `target_tokens ≈ 200 * section_count + 1000 * complex_section_count`
where "complex" = tables, code blocks, or comparison matrices.

### Step 2 — Single-call path (Short / Standard)

```python
response = await client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=8000,        # NEVER below this for finalizer
    system=FINALIZER_SYSTEM_PROMPT,
    messages=[{"role": "user", "content": prepared_input}],
)
```

**Critical**: `max_tokens` MUST be ≥ 8000 for any PRISM finalizer call. This is
the confirmed root cause of historical truncation issues.

### Step 3 — Split-generation path (Long / Comprehensive)

Run `scripts/split_finalizer.py` which:

1. Parses Editor output into section outline
2. Groups sections into 4000-token chunks
3. Generates each chunk with shared system prompt + previous-chunk-summary as context
4. Concatenates with HTML structural healing (close unclosed tags, dedupe section IDs)

```python
from scripts.split_finalizer import split_finalize

final_html = await split_finalize(
    editor_output=editor_output,
    target_sections=section_outline,
    model="claude-sonnet-4-20250514",
    chunk_max_tokens=4000,
)
```

### Step 4 — Validate output

After generation, run `scripts/validate_report.py`:

- Checks HTML well-formedness
- Verifies every planned section is present
- Detects truncation signals: trailing partial sentence, unclosed `<div>`/`<table>`, missing final section
- Confirms v5 design system classes used: `.metric-card`, `.fact-badge`, `.est-badge`, `.out-badge`, `.synergy-block`, `.bottleneck-block`, `.principle-block`

If validation fails:
- Log to `logs/finalizer_failures/` with timestamp
- Retry **once** with `max_tokens` increased by 50%
- If second attempt fails, return partial output flagged with `<!-- TRUNCATED -->` comment and surface error to user — do not silently degrade

### Step 5 — Audit log

Every finalizer run writes to `logs/finalizer/<timestamp>.json`:

```json
{
  "timestamp": "...",
  "task_type": "...",
  "tier": "long",
  "section_count": 14,
  "tokens_in": 12340,
  "tokens_out": 11200,
  "max_tokens_used": 4000,
  "chunks": 3,
  "validation_passed": true,
  "v5_classes_present": ["metric-card", "fact-badge", ...],
  "duration_sec": 87.3
}
```

These logs feed Program Creator's few-shot example library.

## Output format requirements (PRISM-specific)

Final report MUST be **HTML using v5 CSS classes**, never raw Markdown:

| Element | Class | Purpose |
|---|---|---|
| Metric callout | `.metric-card` | KPIs, numbers |
| Confirmed fact | `.fact-badge` | Verified by Perplexity |
| Estimate | `.est-badge` | Model inference |
| Outlier | `.out-badge` | Flagged uncertainty |
| Synergy | `.synergy-block` (purple) | Positive interaction |
| Bottleneck | `.bottleneck-block` (red) | Blocker |
| Principle | `.principle-block` (cyan) | Technical first principle |

System prompt for the final call: see `references/finalizer_system_prompt.md`.

## Related skills

- `vault-indexer` — to update PRISM project status after finalizer runs
- `prism-task-classifier` — to determine which task-type system prompt to load

## Notes

- Never use `claude-3-5-sonnet-20240620` — deprecated.
- Korean + English mixing in output is expected and preserved.
- If user explicitly requests Markdown output (rare, for export), bypass v5 classes — but warn that this loses visual hierarchy.
