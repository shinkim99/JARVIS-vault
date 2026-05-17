---
title: file-parsing
type: skill
tags: [skill, active]
created: 2026-05-15
---

# file-parsing

> 업로드된 PDF/DOCX/PPTX/이미지를 구조화된 마크다운으로 변환. Gemini Flash OCR 기반.

## 설명

PRISM의 `core/file_parser.py`가 담당. 파일 확장자별로 파싱 전략을 분기:
- PDF/PNG/JPG → Gemini 2.5 Flash (base64 인코딩 후 API 호출, OCR + 구조화)
- DOCX → python-docx 헤딩/본문 추출
- PPTX → python-pptx 슬라이드별 텍스트 추출
- TXT/MD → 직접 읽기
- HTML → BeautifulSoup 없이 정규식으로 태그 제거

## 사용 프로그램

- [[PRISM]] — VERITON 팩트체크 파이프라인의 문서 전처리 단계

## 관련 모듈

- [[File-Parser]] — file_parser.py 구현체
