# CLAUDE.md — JARVIS Global Master

> Single source of truth for Shin's context. Loaded at every Claude Code session.
> Last updated: 2026-05-18 | Owner: Shin Kim | Vault: `shinkim99/JARVIS-vault`

---

## 1. Who I Am

- **Name**: Shin Kim (신경섭)
- **Affiliation**: KOLON INDUSTRIES, R&D
- **Domain**: CNT (carbon nanotube) dispersion · Li-ion battery electrode slurry · electrochemistry (EIS, percolation, charge/discharge)
- **Background**: Physics degree, electrochemistry + polymer physical properties
- **Role**: R&D researcher transitioning toward AX (AI Transformation) tooling — non-traditional developer building AI orchestration systems

Call me 자비스 (JARVIS) when addressing me as your persona. Korean conversation, English technical terms freely mixed.

---

## 2. Active Priorities — 3 Axes

Listed in current order of focus. CDP work is **archived** — reference only, no new development.

### Axis A — R&D
| Project | Status | Focus |
|---|---|---|
| **PRISM v0.5** ⭐ | dev | 8 open issues; finalizer max_tokens, Gemini 403, mid-pipeline pause |
| **GRID v13.3** | active | Express.js proxy (port 3000) + Gemini API |
| EIS analyzer | planned | `.mpr` parsing + equivalent circuit fitting |
| Slurry recipe DB | planned | Structured CNT dispersion conditions → PRISM input |
| IP automation | planned | Prior-art screening, invention disclosure drafting (IPMS upstream) |

### Axis B — AX (AI Transformation)
| Project | Status | Focus |
|---|---|---|
| **Program Creator** ⭐ | dev | Stage 1 ConceptSpec spec done; two-stage pipeline with human checkpoint |
| **NEXUS Layer 2** ⭐ | dev | OMEGA-style 3D dashboard; FastAPI + React + Three.js; absorbs wb-library |
| **Workbench** | dev | Lightweight Claude Artifact (jsx); now snapshot view of vault, not SSoT |
| OpenClaw | planned | Server-notebook-resident agent (Phase 3, July 2026) |
| n8n Docker | planned | Server notebook deployment (Phase 2, June 2026) |

### Axis C — Personal
| Project | Status | Focus |
|---|---|---|
| **Homepage** | planned (Phase 4, Aug 2026) | All-in-one: branding + community + AI news/stock curation + JARVIS tool showcase |
| Blog automation | planned | Cowork-driven weekly post generation |
| NotebookLM workflow | active | 5 notebooks: CNT-Dispersion, Battery-Electrode, Claude-Ecosystem, JARVIS-Dev, Patent-Prior-Art |

**Homepage confirmed sub-spec** (from 2026-05-17 design session):
- Stack: Full custom, Next.js + Vercel direction
- Revenue priority: AdSense → paid subscription → premium tool sales (PRISM) → affiliate
- Phase 1 (2–4w): auth + blog + SEO MVP
- Phase 2 (1–2m): AI news auto-curation + stock dashboard
- Phase 3 (2–3m): monetization layer + JARVIS tool exposure

---

## 3. Ecosystem Architecture

```
JARVIS-vault (Obsidian, SSoT, knowledge layer)
  ├── _meta/                ← this file lives here
  ├── programs/active/      ← currently developed
  ├── programs/library/     ← wb-library data migrated here (target)
  └── programs/archived/    ← CDP and past work
        │
        ▼ read via API
  NEXUS (FastAPI + React + Three.js, OMEGA-style)
  ├── Explorer ─ 3D graph of programs/skills/modules
  ├── Launcher ─ subprocess execution
  └── Inspector ─ Claude API-driven code review
        │
        ▼ snapshot export
  Workbench (Claude Artifact, jsx)
  └── Portable, tunable copy for other teams + Program Creator reference
        │
        ▲ generates new programs into
  Program Creator (ConceptSpec → FrameDesign pipeline)
```

**wb-library status**: Already implemented (password auth + AES + import/export). **Paused** pending NEXUS absorption. Its data structure (`programs.json`, registry schemas) is the migration source for NEXUS Phase 2.

---

## 4. Operating Rules

### Communication
- Honest, direct assessments. Acknowledge errors explicitly. No softening for the sake of it.
- Code-level specifics over abstract guidance.
- Complete replacement files over diff patches (unless the change is genuinely small).
- Korean prose + English technical terms — natural mixing.
- Don't dump unrequested options. One direction first, alternatives only if asked.

### Code
- Reliability patterns: Pydantic strict validation + single retry + clarification loop.
- Cost tiers: Practice / Standard / Production.
- Sequential refinement > naive parallel (PRISM lesson).
- SSE for real-time streaming, not polling.
- Audit logs designed to accumulate few-shot examples.

### Environment split
- **Home**: Obsidian + Claude Code, full toolchain
- **Corporate**: VSCode + git only (Obsidian blocked, HTTPS inspection active)
  - SSL fix: `NODE_EXTRA_CA_CERTS` env var + `npm cafile` (company root CA, not Node.js cert)
- **Server notebook** (planned): n8n Docker + OpenClaw

### Tool choice (confirmed via comparison)
- **Claude + Claude Code** for architecture-dependent R&D automation (PRISM, Workbench, NEXUS) — superior architecture coherence + long-context consistency
- GPT Codex for long-running autonomous parallel tasks
- Google Antigravity premature for production

---

## 5. Skills Registry (vault/.claude/skills/)

Active skills live under each project's `.claude/skills/` directory. Global skills under `_meta/.claude/skills/`.

### First wave (in build order)
1. **report-finalizer** (PRISM) — fix max_tokens truncation, split logic, validation ← building now
2. **vault-indexer** (global) — vault frontmatter → Workbench INIT auto-build
3. **eis-analyzer** (R&D) — `.mpr` + equivalent circuit fitting
4. **slurry-recipe** (R&D) — CNT dispersion JSON spec normalizer
5. **prism-task-classifier** (PRISM) — natural language → 6 task type mapping

Skill description style: trigger keywords first, "slightly pushy" per Anthropic guidance.

---

## 6. Stack Quick Reference

| Layer | Tools |
|---|---|
| AI APIs | Claude (primary), Perplexity (fact validation), Gemini (perspective), GPT (summarization) |
| Backend | FastAPI, Python, Pydantic, asyncio |
| Prototyping | Streamlit (sync API calls required), FastAPI + HTML |
| Production frontend | React + Three.js (future), HTML/CSS/JS (current) |
| Automation | n8n (legacy + Docker planned), Cowork (planned) |
| Knowledge | Obsidian vault, NotebookLM, Notion (summary only) |
| Paths | `P:\projects\` (corporate), `D:\projects\` (home) |
| GitHub `shinkim99` | GRID, Cross-validator, wb-library (paused), PRISM, Data-Intelligence-Studio, workbench, tech-intelligence, JARVIS-vault |

---

## 7. Roadmap Anchors (calendar-confirmed)

- **2026-06-01** — Phase 2 start: NotebookLM 5 notebooks, Skills install
- **2026-06-14** — n8n Docker migration
- **2026-07-01** — Phase 3 start: OpenClaw + Workbench v0.7
- **2026-08-01** — Phase 4 start: Homepage build (Next.js + Vercel)

Currently running ~2–3 weeks ahead of original 6-month roadmap.

---

## 8. What NOT to do

- Don't propose options Shin already considered and rejected (Antigravity for production, parallel multi-model calls, Notion as SSoT).
- Don't recreate work that already exists elsewhere in the vault — search first.
- Don't soften feedback. Shin explicitly asks for honest critique.
- Don't suggest CDP-related feature work. Archived.
- Don't treat Workbench INIT array as SSoT. It's a snapshot.
