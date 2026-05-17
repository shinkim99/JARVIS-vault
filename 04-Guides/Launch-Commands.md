---
title: Launch Commands
type: guide
tags: [guide, shell]
updated: 2026-05-15
---

# Launch Commands

Shell Commands 플러그인 또는 터미널에서 직접 실행.

---

## PRISM

Python FastAPI 서버 (포트 8000)

```powershell
cd D:\projects\PRISM && python main.py
```

---

## GRID

HTML 프론트엔드 브라우저 실행

```powershell
cd D:\projects\GRID && start index.html
```

---

## GRID Server

Express.js 프록시 서버 (포트 3000)

```powershell
cd D:\projects\grid-server && node server.js
```

---

## 참고

- GRID와 GRID Server는 함께 실행해야 Gemini API 프록시가 동작합니다.
- PRISM은 `.env`에 API 키가 설정되어 있어야 합니다.
