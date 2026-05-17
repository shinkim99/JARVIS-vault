---
title: chart-rendering
type: skill
tags: [skill, active, shared-skill]
created: 2026-05-15
---

# chart-rendering

> Chart.js 기반 인터랙티브 차트 렌더링. 데이터셋을 라인/바/파이/산점도 등 다양한 형태로 시각화.

## 설명

Chart.js를 핵심 엔진으로 사용. 줌/패닝, 커스텀 범례, 데이터 라벨, 회귀선 등 고급 기능 포함. CSS 변수 기반 Dark/Light 테마와 연동.

## 사용 프로그램

- [[GRID-SaaS]] — 선형/바/누적/면적/파이 차트 (chartjs-plugin-datalabels, regression.js)
- [[Data-Intelligence-Studio]] — 사이클 라이프, 전압 프로파일, 효율, Rate Capability 차트
- [[Cycle-Analysis-HalfCell]] — 반전지 충방전 사이클 시각화
- [[Cycle-Analysis-Rate]] — C-rate별 용량·효율 차트
- [[Cycle-Analysis-FullCell-OP]] — 풀셀 운영 조건 차트
- [[Percolation-ALL]] — 퍼콜레이션 임계점 시각화
- [[Percolation-EIS]] — EIS 임피던스 차트

## 관련 모듈

- [[Chart-Engine]]

## 핵심 라이브러리

| 라이브러리 | 버전 | 용도 |
|---|---|---|
| Chart.js | 4.4.1 | 코어 차트 엔진 |
| chartjs-plugin-datalabels | 2.0.0 | 데이터 포인트 라벨 |
| chartjs-plugin-zoom | 2.0.1 | 줌/패닝 |
| hammer.js | 2.0.8 | 터치 제스처 |
| regression.js | 2.0.1 | 회귀선 오버레이 |
| html2canvas | 1.4.1 | 차트 PNG 캡처 |
