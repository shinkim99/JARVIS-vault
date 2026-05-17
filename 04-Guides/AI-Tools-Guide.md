---
title: AI-Tools-Guide
type: guide
tags: [guide, active]
created: 2026-05-14
---

# AI Tools Guide

> Claude Code, Codex CLI, Antigravity 등 AI 개발 도구 사용 가이드 및 MCP vs API vs CLI 구분.

---

## 도구 비교 개요

| 도구 | 유형 | 주 용도 | 환경 |
|---|---|---|---|
| Claude Code | CLI | 코드 작성·리팩토링·파일 관리 | 터미널 |
| Codex CLI | CLI | 코드 생성·완성 | 터미널 |
| Antigravity | CLI/도구 | 고급 코드 분석·생성 | 터미널 |
| Claude API | API | 프로그램 내 AI 기능 통합 | 서버/백엔드 |
| MCP | 프로토콜 | Claude와 외부 도구 연결 | Claude 클라이언트 |

---

## Claude Code

### 개요
Anthropic 공식 CLI. 터미널에서 Claude와 대화하며 코드 작업.

### 주요 기능
- 파일 읽기·쓰기·편집
- 터미널 명령 실행
- Glob/Grep 기반 코드 검색
- MCP 서버 연결
- Hooks (이벤트 기반 자동화)

### 사용 패턴
```bash
# 대화형 세션 시작
claude

# 단일 명령 실행
claude -p "이 파일의 버그를 찾아줘"

# 특정 디렉토리에서 실행
claude --project /path/to/project
```

### 설정 파일
- `~/.claude/settings.json` — 전역 설정
- `.claude/settings.json` — 프로젝트 설정
- `CLAUDE.md` — 프로젝트 컨텍스트 문서

---

## Codex CLI

### 개요
OpenAI Codex 기반 코드 생성 CLI 도구.

### 주요 기능
- 자연어 → 코드 변환
- 코드 완성 및 수정
- 터미널 명령 제안

### 사용 패턴
```bash
codex "FastAPI 서버 boilerplate 생성"
```

---

## Antigravity

### 개요
고급 AI 기반 코드 분석 및 생성 도구.

---

## MCP vs API vs CLI

### MCP (Model Context Protocol)
- **무엇**: Claude 클라이언트와 외부 도구/서비스를 연결하는 표준 프로토콜
- **언제**: Claude Code나 Claude Desktop에서 외부 서비스(Notion, Google Drive, GitHub 등)와 연동할 때
- **특징**: Claude가 직접 외부 도구를 호출

```
Claude ←→ MCP Server ←→ 외부 서비스
```

### API (Anthropic API)
- **무엇**: 내 프로그램에서 Claude 모델을 직접 호출하는 HTTP API
- **언제**: Python/JS 앱에서 Claude 기능을 구현할 때 ([[PRISM]], [[GRID-SaaS]] 등)
- **특징**: 개발자가 직접 API 호출 코드를 작성

```python
import anthropic
client = anthropic.Anthropic(api_key="...")
response = client.messages.create(...)
```

### CLI (Claude Code)
- **무엇**: 터미널에서 Claude와 대화하는 인터페이스
- **언제**: 직접 코딩 작업, 파일 편집, 리서치 등 개발 워크플로우
- **특징**: 인터랙티브 대화형, 파일시스템 직접 접근

---

## 권장 사용 시나리오

| 시나리오 | 권장 도구 |
|---|---|
| 코드 작성·리팩토링 | Claude Code (CLI) |
| 앱에 AI 기능 추가 | Anthropic API |
| Claude에서 Notion 연동 | MCP |
| 빠른 스크립트 생성 | Codex CLI |
| 배터리 분석 자동화 | API + Python 스크립트 |
