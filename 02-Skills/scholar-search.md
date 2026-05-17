---
title: scholar-search
type: skill
tags: [skill, active]
created: 2026-05-15
---

# scholar-search

> 학술 논문 시맨틱 검색. DOI, 피인용 수, 요약 등 메타데이터 포함.

## 설명

PRISM의 `core/scholar.py` 구현. `/api/scholar/search?query=` 엔드포인트로 외부 학술 DB API를 호출해 관련 논문 목록(최대 20건)을 반환. 파이프라인의 web_searcher 역할과 연계.

## 사용 프로그램

- [[PRISM]] — 문헌검토 의도 파이프라인에서 참고문헌 수집
