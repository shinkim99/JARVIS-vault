---
title: PDF-Exporter
type: module
tags: [module, active]
stack:
  - Python
  - fpdf2
  - reportlab
created: 2026-05-15
---

# PDF-Exporter

> 마크다운을 한글 지원 PDF로 변환 (`core/export_manager.py`). fpdf2 우선, reportlab 폴백.

## 설명

`generate_full_md()` → 분석 보고서 전체 마크다운 생성 (Executive Summary + 상세분석 + 원본관점 + 검토의견 + 참고문헌).

`generate_full_pdf(md_content)` → MD → PDF 변환:
1. **fpdf2** 우선: Malgun Gothic / NanumGothic 한글 폰트 자동 탐색
2. **reportlab 폴백**: SimpleDocTemplate + ParagraphStyle (한글 제한적)

헤딩 레벨(#/##/###), 불릿(- /*), 인용(>), 구분선(---) 모두 적절한 폰트 크기/스타일로 변환.

## 기술 스택

- **fpdf2** (한글 완전 지원, `add_font`)
- **reportlab** (폴백, A4, mm 단위)
- 한글 폰트: Malgun Gothic (Windows), NanumGothic (Linux)

## 소속 프로그램

- [[PRISM]] — 히스토리 보고서 PDF 다운로드

## 관련 모듈

- [[History-Manager]] — 온디맨드 PDF 생성 트리거

## 관련 스킬

- [[file-export]]
