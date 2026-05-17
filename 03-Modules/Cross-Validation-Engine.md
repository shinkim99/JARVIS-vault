---
title: Cross-Validation-Engine
type: module
tags: [module, active]
stack:
  - Python
  - asyncio
  - FastAPI
created: 2026-05-15
---

# Cross-Validation-Engine

> 멀티 LLM 교차 검증 파이프라인 코어 (`skills/cross_validation/pipeline.py`).

## 설명

8단계 비동기 파이프라인: researcher → critic → domain_expert → web_searcher → synthesizer → reviewer → editor → finalizer. 각 단계를 `asyncio.gather`로 병렬 실행(Draft 4역할), 이후 순차 합성.

의도(intent)별 전략 파일(`strategies.py`)로 역할-모델 매핑을 동적 구성. SSE 청크로 단계별 진행 상황 실시간 스트리밍. 최종 HTML 보고서는 CSS 컴포넌트 클래스 기반으로 finalizer가 생성.

## 기술 스택

- **Python asyncio** — 비동기 병렬 LLM 호출
- **FastAPI StreamingResponse** — SSE 스트리밍
- 의도 유형: 기술분석 / 시장조사 / 특허분석 / 문헌검토 / 신규사업

## 소속 프로그램

- [[PRISM]] — 핵심 교차 검증 스킬

## 관련 스킬

- [[cross-validation]]
- [[multi-llm-routing]]
- [[pipeline]]

## 관련 모듈

- [[Multi-LLM-Router]]
- [[SSE-streaming]]
