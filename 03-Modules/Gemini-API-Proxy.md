---
title: Gemini-API-Proxy
type: module
tags: [module, active]
stack:
  - Node.js
  - Express.js
created: 2026-05-14
---

# Gemini-API-Proxy

> Gemini API key를 서버 측에서 안전하게 관리하는 프록시 모듈.

## 설명

클라이언트의 요청을 수신 → `.env`에서 `GEMINI_API_KEY` 로드 → Google Gemini API 호출 → 결과 반환. API key가 클라이언트에 노출되지 않음.

## 기술 스택

- **Node.js** + **Express.js**
- **dotenv** (환경변수 관리)
- 50MB 업로드 한도 (`express-fileupload` 또는 `multer`)

## 소속 프로그램

- [[GRID-SaaS]]
- [[GRID-Server]]

## 관련 모듈

- [[Express-server]]
