---
title: cycle-analysis
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-14
updated: 2026-05-15
---

# cycle-analysis

> 배터리 충방전 사이클 데이터 분석. 용량 유지율, 효율, 열화 거동 분석.

## 설명

충방전 사이클러(Cycler) 출력 데이터를 파싱하여 용량(mAh/g), 쿨롱 효율(CE), 에너지 밀도 등의 지표를 계산하고 시각화. 80% 용량 유지 사이클 자동 감지, Baseline 정규화, C-rate 고정 레시피(0.1C~5C) 추출.

## 사용 프로그램

- [[Cycle-Analysis-Rate]] — C-rate별 용량·효율
- [[Cycle-Analysis-HalfCell]] — 반전지 충방전 사이클
- [[Cycle-Analysis-FullCell-OP]] — 풀셀 운영 조건
- [[Data-Intelligence-Studio]] — 통합 라이브러리 (4종 차트 모드)

## 관련 스킬

- [[csv-parsing]] — 사이클러 CSV 파싱
- [[chart-rendering]] — 사이클 데이터 시각화
- [[data-import]] — 파일 업로드 UI
