---
title: Environment-Workflow
type: guide
tags: [guide, active]
created: 2026-05-14
---

# Environment-Workflow Guide

> 집 / 회사 / 서버 환경별 작업 흐름 가이드 및 SSL 치트시트.

---

## 환경 구분

| 환경 | 특징 | 주의사항 |
|---|---|---|
| 집 (Home) | 자유로운 외부 API 접근 | — |
| 회사 (Office) | 사내 SSL 인증서 인터셉트 | 인증서 관련 오류 발생 가능 |
| 서버 (Server) | 원격 접근, 포트 개방 필요 | 방화벽, 포트 포워딩 설정 |

---

## SSL 치트시트

### Node.js / Express

회사 환경에서 자체 서명 인증서 오류 시:

```bash
# 환경변수로 추가 CA 인증서 지정
NODE_EXTRA_CA_CERTS=/path/to/company-ca.crt node server.js
```

또는 개발 환경 한정 (비권장):
```javascript
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
```

---

### Python (httpx / requests)

```python
# httpx — 검증 비활성화 (개발 전용)
import httpx
client = httpx.Client(verify=False)

# requests
import requests
response = requests.get(url, verify=False)

# 또는 CA 번들 지정 (권장)
response = requests.get(url, verify='/path/to/company-ca.crt')
```

---

### Anthropic SDK (Python)

```python
import anthropic
import httpx

client = anthropic.Anthropic(
    http_client=httpx.Client(verify=False)  # 회사 환경 한정
)
```

또는 환경변수:
```bash
export SSL_CERT_FILE=/path/to/company-ca.crt
```

---

### Google (Gemini) SDK (Python)

```python
import google.generativeai as genai
import httpx

# 네이티브 클라이언트 옵션 활용
# google-auth 라이브러리의 REQUESTS_CA_BUNDLE 환경변수
export REQUESTS_CA_BUNDLE=/path/to/company-ca.crt
```

---

## 환경별 빠른 체크리스트

### 집 환경
- [ ] `.env` 파일에 API key 설정
- [ ] `node server.js` 또는 `uvicorn main:app`
- [ ] 브라우저에서 `localhost:3000` 접속

### 회사 환경
- [ ] `NODE_EXTRA_CA_CERTS` 또는 `SSL_CERT_FILE` 설정
- [ ] 프록시 설정 확인 (`http_proxy`, `https_proxy`)
- [ ] VPN 연결 상태 확인

### 서버 환경
- [ ] 포트 개방 (방화벽 inbound rule)
- [ ] `.env` 파일 서버에 배포 (git에 포함 금지)
- [ ] `pm2` 또는 `systemd`로 프로세스 관리
