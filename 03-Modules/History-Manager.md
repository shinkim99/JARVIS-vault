---
title: History-Manager
type: module
tags: [module, active]
stack:
  - Python
  - JSON
  - FileSystem
created: 2026-05-15
---

# History-Manager

> PRISM 파이프라인 실행 이력을 파일시스템에 영속화하고 API로 노출 (`core/history_manager.py`).

## 설명

각 실행을 `core/history/{timestamp}_{query}_{id}/` 디렉토리에 저장. 내부 파일: `claim_ledger.json`, `draft.json`, `edit.json`, `final.json`, `report.html`, `report.md`, `references/*.ris/.bib`.

`/api/history` GET 목록 → `/api/history/{run_id}` 상세 → `/api/history/{run_id}/report-inline` 보고서 인라인 → `/api/history/{run_id}/{filename}` 다운로드 → `/api/history/{run_id}` DELETE 구조.

PDF가 없으면 온디맨드로 생성(MD → PDF).

## 기술 스택

- **Python** + **pathlib** + **JSON**
- FastAPI 라우터로 CRUD 엔드포인트 제공

## 소속 프로그램

- [[PRISM]]

## 관련 모듈

- [[PDF-Exporter]] — 온디맨드 PDF 생성
