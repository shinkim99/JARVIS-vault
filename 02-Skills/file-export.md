---
title: file-export
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# file-export

> 분석 결과물을 CSV/PNG/JSON/MD/PDF/HTML/RIS/BIB 등 다양한 형식으로 다운로드.

## 설명

프로그램별로 지원 형식이 다르며, 클라이언트사이드(브라우저 Blob API)와 서버사이드(FastAPI FileResponse) 두 가지 패턴으로 구현.

## 사용 프로그램

- [[PRISM]] — MD, PDF(fpdf2/reportlab), HTML(최종보고서), RIS/BIB(참고문헌)
- [[Data-Intelligence-Studio]] — CSV(테이블), PNG(차트), JSON(라이브러리 백업)
- [[Cycle-Analysis-HalfCell]] — CSV 데이터 테이블, PNG 차트
- [[Cycle-Analysis-Rate]] — CSV, PNG
- [[Cycle-Analysis-FullCell-OP]] — CSV, PNG
- [[Percolation-ALL]] — CSV, PNG
- [[Percolation-EIS]] — CSV, PNG
- [[tech-intelligence]] — JSON(도메인 설정 백업)
- [[wb-library]] — JSON(라이브러리 내보내기)

## 관련 모듈

- [[PDF-Exporter]] — PRISM의 MD→PDF 변환 (fpdf2 + reportlab 폴백)

## 관련 스킬

- [[chart-rendering]] — PNG 차트 캡처(html2canvas)
