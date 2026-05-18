# JARVIS Ecosystem State — 2026-05-18

> Consolidation snapshot. Reflects all decisions from prior conversations.
> Updated when major architecture decisions change.

---

## Active Focus

**Phase 1** (May 2026, final week) — Foundation
- This consolidation: CLAUDE.md 3-tier + first skill
- Claude Desktop + Python 3.12 install
- NotebookLM MCP auth

---

## Component Status

### Programs

| Program | Status | Repo | Role |
|---|---|---|---|
| PRISM | v0.5 dev | `shinkim99/PRISM` | Multi-AI R&D analysis pipeline |
| GRID | v13.3 active | `shinkim99/GRID` | Express + Gemini proxy (port 3000) |
| Workbench | v0.7 dev | `shinkim99/workbench` | Lightweight Claude Artifact dashboard |
| Program Creator | dev (spec done) | — | Natural language → new program generator |
| NEXUS | dev (Phase 1) | — | OMEGA-style 3D unified command center |
| wb-library | **PAUSED** | `shinkim99/wb-library` | Will be absorbed into NEXUS |
| Data-Intelligence-Studio | active | `shinkim99/Data-Intelligence-Studio` | Data analysis tools |
| Tech-Intelligence | active | `shinkim99/tech-intelligence` | Tech trend / patent scanning |
| Cross-Validator | archived | `shinkim99/Cross-validator` | Predecessor of PRISM |
| JARVIS-vault | active | `shinkim99/JARVIS-vault` | Obsidian knowledge layer |
| Homepage | planned (Aug) | — | Personal all-in-one platform |
| CDP-related | **archived** | various | Reference only, no new work |

### Skills (target order)

1. ⭐ **report-finalizer** (PRISM) — building now (2026-05-18)
2. vault-indexer (global)
3. eis-analyzer (R&D)
4. slurry-recipe (R&D)
5. prism-task-classifier (PRISM)

### Key Architecture Decision: wb-library → NEXUS

**Decision recorded 2026-05-17**:
- wb-library was already built with programs.json, registry, AES-encrypted import/export, password auth
- Recognized that wb-library + Workbench Artifact + planned NEXUS Item Bay = same thing built 3 times
- **wb-library development is paused**
- Its data structure and schema migrate into NEXUS as Phase 2 work
- NEXUS is the evolutionary successor, not a parallel system

### Key Architecture Decision: NEXUS = OMEGA visualization

**Decision recorded 2026-05-17**:
- NEXUS is not just a CRUD dashboard
- Target visualization: 378-node 3D cylinder + network graph + clustering as nebulae
- Left panel: metrics; Right panel: projects/goals; Bottom: activity log
- Stack: FastAPI + React + Three.js
- Data layer: Obsidian vault → API → 3D viz

### Key Architecture Decision: Workbench role redefined

**Decision recorded 2026-05-18 (this session)**:
- Workbench is **not** the SSoT
- Workbench INIT array = snapshot exported from vault
- Workbench purpose:
  - Portable lightweight artifact for sharing with other teams
  - Reference base for Program Creator
  - Quick visual access during current task
- Vault = SSoT; NEXUS = primary viewer; Workbench = portable view

---

## Homepage — Confirmed Sub-Spec

**Source**: 2026-05-17 design session

| Attribute | Decision |
|---|---|
| Identity | All-in-one (branding + community + media curation + tool showcase) |
| Stack | Full custom, Next.js + Vercel direction |
| Revenue priority | 1. AdSense  2. Subscription/membership  3. Premium tool sales (PRISM)  4. Affiliate |
| Phase 1 (2–4w) | Auth + blog + SEO MVP |
| Phase 2 (1–2m) | AI news auto-curation + stock dashboard |
| Phase 3 (2–3m) | Monetization layer + JARVIS tool exposure |
| Start | 2026-08-01 (Phase 4 of overall ecosystem roadmap) |

---

## What's Off the Table

- CDP-related new feature work (archived; reference only)
- wb-library new development (paused, awaiting NEXUS migration)
- Notion as SSoT (downgraded to summary links only)
- Parallel multi-model calls in PRISM (replaced by sequential refinement)
- Google Antigravity for production (premature, rate limit instability)
- Treating Workbench INIT array as authoritative data (it's a snapshot)

---

## File Locations (after this consolidation)

```
JARVIS-vault/                           ← shinkim99/JARVIS-vault
├── _meta/
│   ├── CLAUDE.md                       ← Global master (Shin's context)
│   └── ecosystem-state.md              ← This file
├── programs/
│   └── active/
│       └── PRISM/
│           ├── CLAUDE.md               ← Project-level
│           └── .claude/skills/
│               └── report-finalizer/
│                   ├── SKILL.md
│                   ├── scripts/
│                   │   ├── split_finalizer.py
│                   │   └── validate_report.py
│                   └── references/
│                       └── finalizer_system_prompt.md
```

**Deployment**: Copy `_meta/CLAUDE.md` to `~/.claude/CLAUDE.md` for global Claude Code use.
Copy each project-level `CLAUDE.md` into the project root (`D:\projects\PRISM\CLAUDE.md`).
Skills live in the project's `.claude/skills/` and are auto-discovered.

---

## Next Sessions

After this consolidation, expected next work:
1. Apply report-finalizer skill to PRISM v0.5 → close issues #6 and #7
2. Build vault-indexer skill (auto-generate Workbench INIT from vault frontmatter)
3. NEXUS Phase 1 continuation (FastAPI scaffolding + vault parser)
4. Migrate wb-library data schema → NEXUS database
