---
title: n8n-Connector
type: module
tags: [module, active]
stack:
  - JavaScript
  - n8n
  - Fetch API
created: 2026-05-15
---

# n8n-Connector

> n8n 클라우드 웹훅 트리거 + 결과 수신 모듈 (tech-intelligence).

## 설명

활성 도메인 설정(JSON)을 `https://shinkim99.app.n8n.cloud/webhook/tech-intel-run`으로 POST. n8n 워크플로우가 분석 수행 후 결과를 `postMessage` 또는 URL 파라미터(`?results=...`)로 반환. 결과를 `localStorage`에 영속화하고 결과 카드 UI로 렌더링.

## 기술 스택

- **JavaScript Fetch API** — 웹훅 POST
- **postMessage API** — 외부 창에서 결과 수신
- **localStorage** — 설정/결과 영속화
- **n8n Cloud** — 워크플로우 자동화 플랫폼

## 소속 프로그램

- [[tech-intelligence]]

## 관련 스킬

- [[n8n-webhook]]
