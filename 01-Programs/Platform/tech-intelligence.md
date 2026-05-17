---
title: tech-intelligence
language: HTML
status: active
github: https://github.com/shinkim99/tech-intelligence
tags: [program, active]
modules:
  - n8n Connector
  - Dark/Light theme
skills:
  - tech-scanning
  - n8n-webhook
  - file-export
  - data-import
created: 2026-05-14
updated: 2026-05-15
---

# tech-intelligence

> HTML 기반 기술 인텔리전스 스캐닝 도구. n8n 클라우드 워크플로우와 웹훅으로 연동해 도메인별 기술 동향 자동 분석.

## 개요

| 항목 | 내용 |
|---|---|
| 언어 | HTML / JavaScript |
| 상태 | #active |
| GitHub | [shinkim99/tech-intelligence](https://github.com/shinkim99/tech-intelligence) |

## 모듈

- [[n8n-Connector]] — n8n 웹훅 트리거 + postMessage 결과 수신
- [[Dark-Light-theme]] — Navy-to-purple 그라디언트 기반 다크 테마

## 스킬

[[tech-scanning]] · [[n8n-webhook]] · [[file-export]] · [[data-import]]

## 주요 기능

| 기능 | 설명 |
|---|---|
| 도메인 관리 | 기술 인텔리전스 도메인 CRUD (키워드, 경쟁사, TRL 레벨) |
| n8n 분석 트리거 | 활성 도메인 → 웹훅 POST → 자동 분석 |
| 결과 대시보드 | 트렌드, 전략적 적합도, 액션 추천 카드 |
| 설정 내보내기 | JSON 다운로드/업로드 (팀 공유) |
| 영속화 | localStorage (설정 + 결과) |

## n8n 웹훅

```
POST https://shinkim99.app.n8n.cloud/webhook/tech-intel-run
```
