---
title: Fact-Check-Engine
type: module
tags: [module, active]
stack:
  - Python
  - asyncio
  - FastAPI
created: 2026-05-15
---

# Fact-Check-Engine

> 문서 팩트체크 파이프라인 (VERITON) 코어 (`skills/fact_check/pipeline.py`).

## 설명

업로드 파일 → 파싱 → 주장 추출 → 멀티 LLM 검증 → HTML 보고서 생성 흐름. SSE로 단계별 진행 상황 스트리밍. 최대 50MB 파일 업로드, 처리 후 임시 파일 자동 삭제.

## 기술 스택

- **Python asyncio** + **FastAPI**
- **SSE (StreamingResponse)**

## 소속 프로그램

- [[PRISM]] — `/api/factcheck/run` 엔드포인트

## 관련 스킬

- [[fact-check]]

## 관련 모듈

- [[File-Parser]] — 업로드 문서 전처리
- [[Multi-LLM-Router]] — 검증 LLM 라우팅
- [[SSE-streaming]] — 실시간 스트리밍
