---
title: File-Parser
type: module
tags: [module, active]
stack:
  - Python
  - Gemini API
  - python-docx
  - python-pptx
created: 2026-05-15
---

# File-Parser

> 업로드 파일을 구조화된 마크다운으로 변환하는 파싱 모듈 (`core/file_parser.py`).

## 설명

파일 확장자별 전략 분기:
- **PDF/PNG/JPG** → Gemini 2.5 Flash (base64 인코딩 → API → OCR + 마크다운 구조화)
- **DOCX** → python-docx (헤딩 레벨 보존, 본문 추출)
- **PPTX** → python-pptx (슬라이드별 텍스트 추출)
- **TXT/MD** → UTF-8 직접 읽기
- **HTML** → 정규식으로 `<script>/<style>/<tag>` 제거 후 텍스트 추출

허용 확장자: `.pdf .docx .pptx .png .jpg .jpeg .txt .md .html`

## 기술 스택

- **Python** + **httpx** (Gemini API 비동기 호출)
- **python-docx**, **python-pptx** (오피스 포맷)
- Gemini 2.5 Flash (`gemini-2.5-flash:generateContent`)

## 소속 프로그램

- [[PRISM]] — VERITON 팩트체크 파이프라인 전처리

## 관련 스킬

- [[file-parsing]]
