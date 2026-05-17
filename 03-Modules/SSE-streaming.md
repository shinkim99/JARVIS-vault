---
title: SSE-streaming
type: module
tags: [module, active]
stack:
  - Python
  - Server-Sent Events
  - FastAPI
created: 2026-05-14
---

# SSE-streaming

> Server-Sent Events(SSE) 기반 실시간 단계별 스트리밍 모듈.

## 설명

파이프라인 각 단계의 진행 상황을 SSE로 클라이언트에 실시간 전달. 단계 시작·완료·에러 이벤트를 구조화된 JSON으로 스트리밍.

## 기술 스택

- **Server-Sent Events** (HTTP 단방향 스트리밍)
- **FastAPI** `EventSourceResponse`
- **JavaScript** `EventSource` API (클라이언트)

## 소속 프로그램

- [[PRISM]]

## 관련 모듈

- [[FastAPI-backend]]
- [[Flowchart-UI]]
