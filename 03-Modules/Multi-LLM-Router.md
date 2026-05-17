---
title: Multi-LLM-Router
type: module
tags: [module, active]
stack:
  - Python
  - httpx
  - FastAPI
created: 2026-05-15
---

# Multi-LLM-Router

> 4개 LLM 프로바이더를 단일 인터페이스로 추상화하는 라우팅 레이어 (`core/providers.py`).

## 설명

`call_model(model, role, content, api_keys, max_tokens)` 단일 함수로 Anthropic/OpenAI/Google/Perplexity를 투명하게 라우팅. 역할별 시스템 프롬프트(8종) 내장. 회사 프록시 대응을 위해 `httpx` SSL `verify=False` 사용. 모든 에러(연결 실패/타임아웃/인증/429)를 구조화된 dict로 반환해 파이프라인이 중단되지 않음.

## 기술 스택

- **Python** + **httpx** (비동기 HTTP, SSL verify=False)
- **FastAPI** 내 의존성으로 사용
- 역할 시스템: researcher / critic / domain_expert / web_searcher / synthesizer / reviewer / editor / finalizer

## 소속 프로그램

- [[PRISM]] — 8단계 파이프라인의 핵심 라우터

## 관련 스킬

- [[multi-llm-routing]]
- [[api-proxy]]
