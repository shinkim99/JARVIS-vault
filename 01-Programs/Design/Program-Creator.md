---
title: Program-Creator
version: v0.0
language: Python
status: idea
tags: [program, idea]
created: 2026-05-14
---

# Program-Creator — v0.0

> ConceptSpec JSON 기반 2-stage 파이프라인으로 프로그램을 자동 생성하는 Python 도구.

## 개요

| 항목 | 내용 |
|---|---|
| 버전 | v0.0 (컨셉) |
| 언어 | Python |
| 상태 | #idea |

## 설계 개요

- **ConceptSpec JSON**: 프로그램 스펙을 JSON 형식으로 정의
- **2-stage pipeline**:
  1. Stage 1 — 스펙 파싱 + 구조 설계
  2. Stage 2 — 코드 생성 + 검증
- **Pydantic**: 스펙 유효성 검증

## 연결 관계

- 플랫폼: [[NEXUS]] (예정)
