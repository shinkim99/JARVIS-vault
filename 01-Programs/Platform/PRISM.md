---
title: PRISM
version: v0.8
language: Python
status: dev
github: https://github.com/shinkim99/PRISM
tags: [program, dev]
modules:
  - FastAPI backend
  - SSE streaming
  - Flowchart UI
  - Report finalizer
  - Dark/Light theme
  - Cross-Validation-Engine
  - Fact-Check-Engine
  - Multi-LLM-Router
  - History-Manager
  - File-Parser
  - PDF-Exporter
skills:
  - strategy-engine
  - pipeline
  - pricing
  - multi-llm-routing
  - file-parsing
  - fact-check
  - file-export
  - scholar-search
  - cross-validation
  - api-proxy
created: 2026-05-14
updated: 2026-05-15
errors:
  - "Finalizer max_tokens 8000+"
  - "Gemini 403"
  - "Mid-pipeline pause"
---

# PRISM — v0.8

> Python FastAPI 기반 멀티스테이지 파이프라인 플랫폼. SSE 스트리밍으로 실시간 진행 상황을 시각화. 교차 검증 + 팩트체크 + 학술 검색 통합.

## 개요

| 항목 | 내용 |
|---|---|
| 버전 | v0.8 |
| 언어 | Python |
| 상태 | #dev |
| GitHub | [shinkim99/PRISM](https://github.com/shinkim99/PRISM) |
| 포트 | 8000 |

## 모듈

- [[FastAPI-backend]] — REST API + SSE 엔드포인트 (`api/main.py`)
- [[SSE-streaming]] — 실시간 단계별 스트리밍
- [[Flowchart-UI]] — 파이프라인 플로우차트 시각화
- [[Report-finalizer]] — 최종 HTML 보고서 생성
- [[Dark-Light-theme]] — 테마 전환
- [[Cross-Validation-Engine]] — 8단계 멀티 LLM 교차 검증 파이프라인
- [[Fact-Check-Engine]] — VERITON 팩트체크 파이프라인
- [[Multi-LLM-Router]] — 4 프로바이더 추상화 (`core/providers.py`)
- [[History-Manager]] — 실행 이력 파일시스템 영속화 (`core/history_manager.py`)
- [[File-Parser]] — PDF/DOCX/PPTX/이미지 파싱 (`core/file_parser.py`)
- [[PDF-Exporter]] — MD → PDF 변환, 한글 지원 (`core/export_manager.py`)

## 스킬

[[strategy-engine]] · [[pipeline]] · [[pricing]] · [[multi-llm-routing]] · [[cross-validation]] · [[file-parsing]] · [[fact-check]] · [[scholar-search]] · [[file-export]] · [[api-proxy]]

## API 엔드포인트 맵

| 엔드포인트 | 기능 |
|---|---|
| `POST /api/run` | 교차 검증 파이프라인 (SSE) |
| `POST /api/factcheck/run` | 팩트체크 파이프라인 (SSE) |
| `GET /api/scholar/search` | 학술 논문 검색 |
| `GET /api/history` | 실행 이력 목록 |
| `GET /api/history/{id}` | 이력 상세 + 파일 다운로드 |
| `GET /api/models` | 사용 가능한 모델 목록 |
| `POST /api/estimate-cost` | 비용 사전 산출 |

## 알려진 버그 / 이슈

| 이슈 | 설명 |
|---|---|
| Finalizer max_tokens | 8000+ 토큰에서 finalizer 중단 |
| Gemini 403 | 특정 조건에서 Gemini API 403 오류 |
| Mid-pipeline pause | 파이프라인 중간 일시정지 미구현 |
| Token slider | 슬라이더 UI 반응 불안정 |
| Step 1→2 arrow | 플로우차트 1→2 단계 화살표 렌더링 오류 |

## 전신

[[Cross-validator]] (n8n 기반 전신) → PRISM으로 재개발
