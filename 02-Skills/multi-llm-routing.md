---
title: multi-llm-routing
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# multi-llm-routing

> 여러 LLM 프로바이더(Anthropic, OpenAI, Google, Perplexity)를 역할별로 자동 라우팅.

## 설명

단일 `call_model(model, role, content)` 인터페이스로 4개 프로바이더를 추상화. 모델명→프로바이더 자동 감지, API 키 관리, 비용 추적, 에러 핸들링(연결 실패/타임아웃/인증 오류) 통합.

역할 시스템: researcher / critic / domain_expert / web_searcher / synthesizer / reviewer / editor / finalizer

## 사용 프로그램

- [[PRISM]] — 8단계 파이프라인에서 각 단계마다 최적 모델 라우팅
- [[Cross-validator]] — 전신 구조, 동일 멀티모델 교차 검증 패턴

## 관련 모듈

- [[Multi-LLM-Router]] — providers.py 구현체

## 지원 프로바이더

| 프로바이더 | 모델 | 티어 |
|---|---|---|
| Anthropic | claude-haiku-4-5, claude-sonnet-4-6, claude-opus-4-6 | economy/standard/premium |
| OpenAI | gpt-4.1-mini, gpt-4.1 | economy/standard |
| Google | gemini-2.5-flash, gemini-2.5-pro | economy/standard |
| Perplexity | sonar, sonar-pro, sonar-reasoning-pro | economy/standard/premium |
