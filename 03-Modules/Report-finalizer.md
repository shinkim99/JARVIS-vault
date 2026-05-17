---
title: Report-finalizer
type: module
tags: [module, active]
stack:
  - Python
  - Gemini API / Claude API
created: 2026-05-14
---

# Report-finalizer

> 파이프라인 최종 단계에서 구조화된 리포트를 생성하는 모듈.

## 설명

이전 단계의 중간 결과를 취합하여 최종 보고서를 생성. 긴 보고서는 자동 분할 예정.

## 기술 스택

- **Python**
- **Gemini API** / **Claude API** (LLM 호출)

## 알려진 이슈

- max_tokens 8000+ 초과 시 중단 (미해결)
- 긴 보고서 분할 로직 미완성

## 소속 프로그램

- [[PRISM]]

## 관련 모듈

- [[FastAPI-backend]]
