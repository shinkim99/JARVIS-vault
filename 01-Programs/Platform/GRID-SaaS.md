---
title: GRID-SaaS
version: V16
language: HTML
status: active
github: https://github.com/shinkim99/GRID
tags: [program, active]
modules:
  - SaaS Dashboard
  - Gemini API Proxy
  - Chart Engine
  - Firebase Auth
  - Dark/Light theme
skills:
  - gemini-scan
  - data-viz
  - image-analysis
  - chart-rendering
  - dark-light-theme
  - user-auth
  - api-proxy
  - file-export
created: 2026-05-14
updated: 2026-05-15
---

# GRID-SaaS — V16

> HTML 기반 SaaS 대시보드. [[GRID-Server]](Express.js 프록시)를 통해 Gemini API key를 보안 처리. Firebase 인증 + Firestore 영속화.

## 개요

| 항목 | 내용 |
|---|---|
| 버전 | V16 (JARVIS Universal Engine) |
| 언어 | HTML / JavaScript |
| 상태 | #active |
| GitHub | [shinkim99/GRID](https://github.com/shinkim99/GRID) |

## 모듈

- [[SaaS-Dashboard]] — 메인 대시보드 UI (사이드바 네비게이션, 인스펙터 패널)
- [[Gemini-API-Proxy]] — API key 보안 프록시 (→ [[GRID-Server]])
- [[Chart-Engine]] — Chart.js 6종 엔진 (선형/바/누적/면적/파이, regression.js)
- [[Firebase-Auth]] — 사용자 인증, Firestore 프로젝트/히스토리 영속화
- [[Dark-Light-theme]] — CSS Custom Properties 기반 테마 전환

## 스킬

[[gemini-scan]] · [[data-viz]] · [[image-analysis]] · [[chart-rendering]] · [[dark-light-theme]] · [[user-auth]] · [[api-proxy]] · [[file-export]]

## 차트 엔진 모드

| 모드 | 설명 |
|---|---|
| STD | 표준 라인/바 차트 |
| PRO | 고급 다중 시리즈 |
| PIE | 파이/도넛 차트 |

## 아키텍처 메모

- Express.js 프록시([[GRID-Server]])가 `.env`의 `GEMINI_API_KEY`를 관리
- 클라이언트는 `/api/scan` 엔드포인트만 호출 → API key 노출 방지
- 50MB 업로드 한도 (프록시 설정)
- Firebase SDK 10.7.1 (app / auth / firestore)
