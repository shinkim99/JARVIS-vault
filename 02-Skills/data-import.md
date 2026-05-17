---
title: data-import
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# data-import

> 파일 드래그앤드롭 + 클릭 업로드로 데이터를 인제스트. CSV/JSON/PDF/DOCX/PPTX/이미지 지원.

## 설명

사용자가 로컬 파일을 UI에 드롭하거나 클릭해 선택하면 브라우저(또는 서버)가 파싱해 내부 데이터 구조로 변환. 장비 자동 감지(Won-A Tech, Neware, Biologic), 배치 업로드, IndexedDB 영속화 등 구현 수준이 프로그램마다 다름.

## 사용 프로그램

- [[Data-Intelligence-Studio]] — CSV + JSON, IndexedDB, 100MB 한도, 장비 자동 감지
- [[Cycle-Analysis-HalfCell]] — CSV 충방전 데이터
- [[Cycle-Analysis-Rate]] — CSV C-rate 데이터
- [[Cycle-Analysis-FullCell-OP]] — CSV 풀셀 데이터
- [[Percolation-ALL]] — CSV 퍼콜레이션 데이터
- [[Percolation-EIS]] — CSV EIS 데이터
- [[PRISM]] — PDF/DOCX/PPTX/PNG/HTML 업로드 (서버사이드 파싱 → Gemini OCR)
- [[wb-library]] — JSON 라이브러리 백업 임포트

## 관련 스킬

- [[csv-parsing]] — CSV 특화 파싱 로직
- [[file-parsing]] — PRISM의 서버사이드 파싱
