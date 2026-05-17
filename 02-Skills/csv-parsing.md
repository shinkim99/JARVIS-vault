---
title: csv-parsing
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# csv-parsing

> 충방전 사이클러(Cycler) CSV 파일 파싱. 장비별 포맷 자동 감지 및 표준 데이터 구조 변환.

## 설명

Won-A Tech, Neware, Biologic 등 장비별로 CSV 컬럼 구조가 다름. 파일명/헤더 패턴으로 자동 감지 후 표준화. 날짜(YYYYMMDD), 고형분(예: "5p"=5%), 샘플 ID 등을 파일명에서 추출.

## 사용 프로그램

- [[Data-Intelligence-Studio]] — 3종 장비 자동 감지, 100MB 한도
- [[Cycle-Analysis-HalfCell]] — 반전지 CSV
- [[Cycle-Analysis-Rate]] — C-rate CSV
- [[Cycle-Analysis-FullCell-OP]] — 풀셀 CSV
- [[Percolation-ALL]] — 퍼콜레이션 CSV
- [[Percolation-EIS]] — EIS CSV

## 관련 스킬

- [[data-import]] — 파일 업로드 UI 레이어
- [[cycle-analysis]] — 파싱 후 분석 로직
