---
title: Chart-Engine
type: module
tags: [module, active]
stack:
  - JavaScript
  - Chart.js
  - html2canvas
created: 2026-05-15
---

# Chart-Engine

> Chart.js 기반 인터랙티브 차트 렌더링 모듈. 줌/패닝, 커스텀 범례, 데이터 라벨, 회귀선 지원.

## 설명

모든 HTML 분석 도구에서 공유하는 차트 코어. CSS 변수로 Dark/Light 테마 자동 연동. `html2canvas`로 차트를 PNG로 캡처해 파일 다운로드 가능.

## 기술 스택

| 라이브러리 | 용도 |
|---|---|
| **Chart.js 4.4.1** | 라인/바/파이/산점도 |
| **chartjs-plugin-datalabels 2.0.0** | 데이터 포인트 라벨 오버레이 |
| **chartjs-plugin-zoom 2.0.1** | 마우스 휠/핀치 줌·패닝 |
| **hammer.js 2.0.8** | 모바일 터치 제스처 |
| **regression.js 2.0.1** | 선형/지수 회귀선 |
| **html2canvas 1.4.1** | 차트 PNG 캡처 |

## 소속 프로그램

- [[GRID-SaaS]] — 선형/바/누적/면적/파이 (6개 엔진 모드)
- [[Data-Intelligence-Studio]] — 사이클 라이프, 전압 프로파일, 효율, Rate Capability
- [[Cycle-Analysis-HalfCell]] — 반전지 사이클 시각화
- [[Cycle-Analysis-Rate]] — C-rate 용량·효율 차트
- [[Cycle-Analysis-FullCell-OP]] — 풀셀 운영 조건 차트
- [[Percolation-ALL]] — 퍼콜레이션 네트워크 임계점
- [[Percolation-EIS]] — EIS 임피던스 스펙트럼

## 관련 스킬

- [[chart-rendering]]
