---
title: fact-check
type: skill
tags: [skill, active]
created: 2026-05-15
---

# fact-check

> 업로드 문서의 주장/데이터를 다중 AI로 교차 검증하는 VERITON 파이프라인.

## 설명

PRISM의 `skills/fact_check/` 구현. 문서를 파싱한 뒤 멀티 LLM으로 각 주장의 사실 여부를 검증. SSE 스트리밍으로 단계별 진행 상황 실시간 출력. 최종 HTML 보고서 생성.

## 사용 프로그램

- [[PRISM]] — `/api/factcheck/run` 엔드포인트

## 관련 스킬

- [[file-parsing]] — 문서 파싱 전처리
- [[multi-llm-routing]] — 검증 단계별 모델 라우팅
- [[pipeline]] — SSE 스트리밍 파이프라인
- [[file-export]] — 결과 보고서 출력

## 관련 모듈

- [[Fact-Check-Engine]]
