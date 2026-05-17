---
title: GRID-Server
version: v1.0
language: JavaScript
status: active
tags: [program, active]
port: 3000
env:
  - GEMINI_API_KEY
upload_limit: 50MB
modules:
  - Express-server
  - Gemini API Proxy
skills:
  - api-proxy
created: 2026-05-14
updated: 2026-05-15
---

# GRID-Server — v1.0

> [[GRID-SaaS]]의 백엔드 프록시 서버. Express.js로 구현되어 Gemini API key를 안전하게 관리.

## 개요

| 항목 | 내용 |
|---|---|
| 버전 | v1.0 |
| 언어 | JavaScript (Node.js) |
| 상태 | #active |
| 포트 | 3000 |
| 업로드 한도 | 50MB |

## 모듈

- [[Express-server]] — Express.js 서버 코어 (CORS, 50MB 바디 파서)
- [[Gemini-API-Proxy]] — `/api/scan` → Gemini API 포워딩

## 스킬

[[api-proxy]]

## 환경 변수

```
GEMINI_API_KEY=<your_key>
```
`.env` 파일에 저장, 클라이언트에 절대 노출하지 않음.

## 연결 관계

- 클라이언트: [[GRID-SaaS]]
- 프록시 대상: Gemini API (Google)

## API 엔드포인트

```
POST /api/scan
Body: { model, prompt, imageBase64 }
→ Gemini generateContent API 포워딩
```

## 실행

```bash
node server.js
# 또는
npm start
```
