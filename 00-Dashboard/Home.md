---
title: JARVIS Home Dashboard
type: dashboard
tags: [dashboard, active]
updated: 2026-05-15
---

# JARVIS — R&D Command Center

> [!summary] System Overview
> **Programs** `$= dv.pages('"01-Programs"').length` &nbsp;·&nbsp; **Skills** `$= dv.pages('"02-Skills"').length` &nbsp;·&nbsp; **Modules** `$= dv.pages('"03-Modules"').length`

---

## Program Status

```dataview
TABLE WITHOUT ID
  link(file.link, file.name) AS "Program",
  status AS "Status",
  default(version, revision) AS "Ver",
  language AS "Lang",
  regexreplace(file.folder, "01-Programs/", "") AS "Platform"
FROM "01-Programs"
SORT status ASC, file.name ASC
```

---

## Errors

```dataview
TABLE WITHOUT ID
  link(file.link, file.name) AS "Program",
  status AS "Status",
  errors
FROM "01-Programs"
WHERE errors
SORT file.name ASC
```

*`errors:` frontmatter 필드가 있는 프로그램만 표시됩니다.*

---

## Skill Cross-Reference

```dataview
TABLE WITHOUT ID
  link(file.link, file.name) AS "Skill",
  length(file.inlinks) AS "사용 수"
FROM "02-Skills"
SORT length(file.inlinks) DESC
```

---

## Quick Links

```dataview
TABLE WITHOUT ID
  link(file.link, file.name) AS "Program",
  status AS "Status",
  github AS "GitHub"
FROM "01-Programs"
WHERE github
SORT file.name ASC
```

---

## Program Hub

### Platform
[[GRID-SaaS]] · [[GRID-Server]] · [[PRISM]] · [[Cross-validator]] · [[Data-Intelligence-Studio]] · [[tech-intelligence]] · [[wb-library]] · [[KII-workbench]]

### Analysis Tools
[[Cycle-Analysis-Rate]] · [[Cycle-Analysis-HalfCell]] · [[Cycle-Analysis-FullCell-OP]] · [[Percolation-ALL]] · [[Percolation-EIS]] · [[Recipe-CNT-Runsheet]] · [[Recipe-Anode]] · [[Recipe-Cathode]] · [[CDP-Working-Board]] · [[Prompt-Orchestrator]]

### Design
[[JARVIS-Workbench]] · [[NEXUS]] · [[Program-Creator]]
