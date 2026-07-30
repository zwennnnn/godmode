---
name: API Security
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://owasp.org/www-project-api-security/
  - https://owasp.org/www-project-api-security/2025/
  - https://github.com/OWASP/API-Security
  - https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
  - https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
  - https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
  - https://tools.ietf.org/html/rfc6749
  - https://tools.ietf.org/html/rfc6750
  - https://tools.ietf.org/html/rfc7519
  - https://datatracker.ietf.org/doc/html/rfc8725
  - https://curity.io/resources/learn/jwt-best-practices/
  - https://blog.postman.com/best-practices-for-secure-api-keys/
  - https://42crunch.com/
  - https://salt.security/
tags: [api-security, oauth, oidc, jwt, owasp-api-top-10, rest-security, graphql-security]
---

# API Security

## One-liner

Securing APIs — authentication, authorization, input validation, rate limiting, and the OWASP API Security Top 10 — the most-attacked surface in modern apps.

## What It Is

APIs are the #1 attack surface in 2026. Modern apps are API-first; everything talks via HTTP. Securing APIs means:

| Layer | What |
|-------|------|
| **Authentication** | Who is the caller? OAuth 2.0, OIDC, JWT, API keys, mTLS. |
| **Authorization** | What can they do? RBAC, ABAC, scopes, claims. |
| **Input validation** | Validate every input; reject malformed. |
| **Output encoding** | Escape output to prevent injection. |
| **Rate limiting** | Protect against abuse + DoS. |
| **Transport security** | TLS 1.2+; HSTS. |
| **CORS** | Cross-origin restrictions. |
| **Secrets management** | API keys in secret manager, never in code. |
| **Logging + monitoring** | Detect anomalies. |
| **Schema validation** | Validate against OpenAPI / GraphQL schema. |

### OWASP API Security Top 10 (2023; latest at writing)

1. **Broken Object Level Authorization (BOLA)**
2. **Broken Authentication**
3. **Broken Object Property Level Authorization (BOPLA)**
4. **Unrestricted Resource Consumption**
5. **Broken Function Level Authorization**
6. **Unrestricted Access to Sensitive Business Flows**
7. **Server Side Request Forgery (SSRF)**
8. **Security Misconfiguration**
9. **Improper Inventory Management** (shadow + zombie APIs)
10. **Unsafe Consumption of APIs**

### Key standards

| Standard | Notes |
|----------|-------|
| **OAuth 2.0** ([RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)) | Authorization framework; the standard. |
| **OAuth 2.1** | Simplified version (2020 draft, in progress 2026). |
| **OIDC** | Identity layer on top of OAuth 2.0. |
| **JWT** ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)) | JSON Web Tokens; stateless auth. |
| **JWT Best Current Practices** ([RFC 8725](https://datatracker.ietf.org/doc/html/rfc8725)) | MUST read for JWT implementations. |
| **mTLS** | Mutual TLS; for service-to-service. |
| **API Key** | Simple; for service-to-service. |
| **Bearer Token** | Most common; in `Authorization: Bearer ...`. |

### Common API attacks

| Attack | Defense |
|--------|---------|
| **BOLA** | Strict authorization checks on every object access. |
| **Broken auth** | Use proven libraries; never roll your own crypto. |
| **Injection** | Parameterized queries; ORM; validation. |
| **Excessive data exposure** | Return only what the client needs. |
| **Lack of resources / rate limiting** | Rate limit; quota; pagination. |
| **Mass assignment** | Allowlist fields; never `Object.assign(user, input)`. |
| **SSRF** | Validate URLs; block internal IPs; allowlist. |
| **Broken function level auth** | Per-endpoint auth checks; role-based. |

### Top tools (2026)

| Tool | Purpose |
|------|---------|
| **[42Crunch](https://42crunch.com/)** | API security audit + runtime. |
| **[Salt Security](https://salt.security/)** | API behavior monitoring. |
| **StackHawk** | DAST for APIs. |
| **Burp Suite** | Web / API pentest. |
| **Postman** | API testing; security tests. |
| **Akto** | Automated API security testing. |
| **Imperva API Security** | Enterprise. |

Adoption: API security is non-optional for any product with a public API. OWASP API Top 10 is required reading. Most breaches in 2024–2026 involved APIs (T-Mobile, Twitter, Optus, etc.).

## When To Use It

- **You have any public or partner API** — period.
- **You serve multiple clients** — mobile + web + partner.
- **You use OAuth / OIDC / JWT** — follow the standards.
- **You're building a microservices architecture** — service-to-service auth.
- **You want to pentest your API** — Burp / StackHawk / OWASP ZAP.

## When NOT To Use It

- **No API** — internal app, no exposure.
- **You're prototyping** — defer to production-readiness.
- **You're using only static sites** — no API to secure.

## Why It Matters in 2026

Three forces:

1. **APIs are the #1 attack surface.** More data leaks come from APIs than from web apps in 2026.
2. **AI agents call APIs at scale.** Your API is now called by LLMs, not just humans — auth + rate limiting matters more.
3. **GraphQL + REST + gRPC heterogeneity** — multiple protocols to secure.

Practitioner playbook in 2026:
1. **OAuth 2.0 / OIDC for auth** — use a library (Auth.js, Passport, Spring Security).
2. **JWT with RFC 8725 best practices** — short expiry, asymmetric signing, validate every claim.
3. **Authorization on every endpoint** — per-object, per-function.
4. **Input validation** — schema validation (Zod, JSON Schema).
5. **Rate limiting** — per-user, per-IP, per-API-key.
6. **OpenAPI / GraphQL schema as source of truth** — generate validation from it.
7. **API gateway** — Kong, Apigee, AWS API Gateway, Tyk for centralized policy.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | OAuth 15+ years; standards stable. |
| Community | 95 | Massive; OWASP. |
| Learning curve | 60 | Standards are dense; auth is hard. |
| Performance | 90 | JWT validation fast; OAuth flows can be cached. |
| Cost | 85 | OSS libs free; identity providers $$$ at scale. |
| DX | 80 | Libraries improving. |
| Production readiness | 95 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **OAuth 2.0** | Standard; multiple clients. | Simple internal APIs. |
| **API Key** | Simple service-to-service. | User-facing apps. |
| **mTLS** | Service-to-service; high security. | Browser clients (no cert). |
| **Session cookies** | Traditional web apps. | APIs; mobile. |
| **No auth** | Internal-only; trusted network. | Anything exposed. |

## Sources

- [OWASP API Security](https://owasp.org/www-project-api-security/) — 2026
- [OWASP API Security Top 10 2023](https://owasp.org/www-project-api-security/2023/) — 2023
- [OWASP API Security GitHub](https://github.com/OWASP/API-Security) — 2026
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) — 2026
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — 2026
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — 2026
- [RFC 6749 — OAuth 2.0](https://tools.ietf.org/html/rfc6749) — 2026
- [RFC 6750 — OAuth 2.0 Bearer Tokens](https://tools.ietf.org/html/rfc6750) — 2026
- [RFC 7519 — JWT](https://datatracker.ietf.org/doc/html/rfc7519) — 2026
- [RFC 8725 — JWT Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — 2026
- [Curity — JWT Best Practices](https://curity.io/resources/learn/jwt-best-practices/) — 2026
- [Postman — Best Practices for Secure API Keys](https://blog.postman.com/best-practices-for-secure-api-keys/) — 2026
- [42Crunch](https://42crunch.com/) — 2026
- [Salt Security](https://salt.security/) — 2026