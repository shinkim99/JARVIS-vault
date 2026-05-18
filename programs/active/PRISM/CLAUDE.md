# CLAUDE.md — PRISM Project

> Loaded automatically when working in `D:\projects\PRISM\`.
> Inherits from `JARVIS-vault/_meta/CLAUDE.md` (global).

---

## Project Identity

**PRISM** — Parallel Review & Insight Synthesis Machine
- Multi-AI cross-validation pipeline for R&D analysis
- Rebranded from "Cross Validator"
- Version: **v0.5** (dev)
- Repo: `shinkim99/PRISM`

## Stack

| Layer | Tech |
|---|---|
| Backend | FastAPI (Python) |
| Frontend | HTML + CSS + vanilla JS (v5_Final design system) |
| Streaming | SSE (Server-Sent Events) |
| Models | Claude (draft + final judge), Perplexity (fact validation + citations), Gemini (perspective), GPT (summarization) |
| Validation | Pydantic strict + single retry + clarification loop |
| Config | `.env` auto-load via python-dotenv |

## Pipeline Pattern

**Sequential refinement** (confirmed superior to parallel):
```
Draft (Claude) → Review (Perplexity + Gemini) → Edit (GPT) → Finalize (Claude)
```

## Strategy Engine — 6 Task Types

Each type has its own strategy, validation criteria, and source priorities:
1. Technology trend analysis
2. Competitor/patent landscape
3. Material/formulation review
4. Experimental result interpretation
5. Literature synthesis
6. New business opportunity scan

## Completed (v0.1 → v0.5)

- FastAPI + HTML architecture
- `.env` API key auto-load
- Dark/light mode
- Flowchart UI (Mermaid-based)
- SSE pipeline streaming
- Strategy Engine (6 task types, per-type prompts)
- v5_Final HTML design system
- JARVIS avatar + PRISM SVG logo
- `pricing.py` model ID fixes
- `report_ready` event separation in `pipeline.py`

## Open Issues (8) — Priority Order

| # | Issue | Severity | Skill |
|---|---|---|---|
| 6 | Finalizer `max_tokens` < 8000 causes report truncation | **CRITICAL** | report-finalizer |
| 7 | Long report split-generation logic missing | **CRITICAL** | report-finalizer |
| 4 | Mid-pipeline stop (AbortController) not implemented | HIGH | — |
| 8 | Gemini 403 error handling missing | HIGH | — |
| 5 | Error modal: continue/abort choice missing | MEDIUM | — |
| 1 | Token slider label mismatch | LOW | — |
| 2 | JARVIS image not displaying (path issue) | LOW | — |
| 3 | Step 1→2 merge arrow SVG needs improvement | LOW | — |

**Root cause of #6**: Finalizer `max_tokens` parameter set too low. Confirmed. Must be ≥8000.

## File Layout

```
D:\projects\PRISM\
├── api\
│   ├── main.py              ← FastAPI entry
│   ├── pipeline.py          ← orchestration + SSE events
│   ├── strategy_engine.py   ← 6 task types
│   ├── pricing.py           ← model cost tables
│   └── prompts\             ← per-type system prompts
├── frontend\
│   └── index.html           ← single-file UI (v5_Final)
├── .claude\
│   └── skills\
│       └── report-finalizer\
├── .env                     ← gitignored
└── CLAUDE.md                ← this file
```

## Project-specific rules

- Report output: **HTML directly using v5 CSS classes**, not Markdown. (Confirmed gap vs. manual v5 reports — metric cards, FACT/EST/OUT badges, synergy/bottleneck/principle blocks.)
- Cost tier flag must be respected: Practice / Standard / Production.
- Audit log every pipeline run to `logs/` — these become few-shot examples for Program Creator.
- Never use deprecated model IDs. Current: `claude-sonnet-4-20250514`, `gemini-2.5-flash`, `pplx-*` with valid Bearer token, `gpt-*` current.

## Next Actions

1. Apply `report-finalizer` skill → fix #6, #7
2. Execution test + report quality verification against manual v5 standard
3. Address #4, #8 (high severity)
4. Cleanup pass for #1, #2, #3
