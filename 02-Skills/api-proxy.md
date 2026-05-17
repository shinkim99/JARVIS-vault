---
title: api-proxy
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# api-proxy

> 외부 AI API 키를 서버에 격리해 클라이언트에 노출하지 않는 프록시 패턴.

## 설명

클라이언트가 직접 외부 API를 호출하지 않고 내부 프록시 엔드포인트를 통해 요청. 서버가 `.env`에서 키를 읽어 외부 API로 포워딩. 50MB 업로드 한도, CORS, 에러 핸들링 포함.

## 사용 프로그램

- [[GRID-Server]] — Express.js `/api/scan` → Gemini API 포워딩. `GEMINI_API_KEY` 은닉
- [[PRISM]] — FastAPI + httpx로 Anthropic/OpenAI/Google/Perplexity API 프록시. SSL verify=False(회사 프록시 대응)

## 관련 모듈

- [[Express-server]] — GRID-Server 프록시 구현
- [[FastAPI-backend]] — PRISM 프록시 구현
- [[Gemini-API-Proxy]] — GRID-Server의 Gemini 특화 프록시
- [[Multi-LLM-Router]] — PRISM의 멀티 프로바이더 라우팅
