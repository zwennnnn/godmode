---
name: Cyber Security
slug: cyber-security
source: https://roadmap.sh/cyber-security + https://roadmap.sh/ai-red-teaming + https://roadmap.sh/api-security-best-practices
last-updated: 2026-07-30
tech-count: 6
status: in-progress
---

# Cyber Security

> **Category:** Disciplines and practices for protecting systems, data, and users from attack — application security, network security, pentesting, AI-specific threats, and the security mindset every engineer needs.
> **Sources:** [roadmap.sh/cyber-security](https://roadmap.sh/cyber-security), [roadmap.sh/ai-red-teaming](https://roadmap.sh/ai-red-teaming), [roadmap.sh/api-security-best-practices](https://roadmap.sh/api-security-best-practices)

This roadmap covers the security knowledge every backend engineer, DevOps engineer, and tech lead needs in 2026 — application security fundamentals, the OWASP Top 10, network basics, penetration testing, API security, and the new frontier of AI/LLM security.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Cyber Security (fundamentals) | [cyber-security.md](cyber-security.md) | placeholder |
| 2 | Application Security (AppSec / OWASP) | [application-security.md](application-security.md) | placeholder |
| 3 | Penetration Testing | [penetration-testing.md](penetration-testing.md) | placeholder |
| 4 | Network Security | [network-security.md](network-security.md) | placeholder |
| 5 | API Security | [api-security.md](api-security.md) | placeholder |
| 6 | AI Red Teaming | [ai-red-teaming.md](ai-red-teaming.md) | placeholder |

---

## Quick Decision Guide

### If you build any web app

At minimum, [application-security.md](application-security.md) — OWASP Top 10 + SAST/SCA in CI.

### If you build APIs

[api-security.md](api-security.md) — OAuth 2.0 / OIDC, OWASP API Top 10, JWT best practices.

### If you ship AI features

[ai-red-teaming.md](ai-red-teaming.md) — prompt injection, jailbreaks, OWASP LLM Top 10, Lakera Guard / Garak / PyRIT.

### If you operate infrastructure

[network-security.md](network-security.md) — TLS 1.3, Zero Trust, WAF, DDoS protection (Cloudflare is default).

### If you want to find your own bugs

[penetration-testing.md](penetration-testing.md) — methodology, tools (Kali, Burp, Metasploit), bug bounty platforms.

### If you're starting from zero

1. Start with [cyber-security.md](cyber-security.md) — the discipline overview.
2. Then [application-security.md](application-security.md) — the most common starting point.
3. Add [api-security.md](api-security.md) if you have APIs.
4. Add [network-security.md](network-security.md) if you operate infra.
5. Add [ai-red-teaming.md](ai-red-teaming.md) if you ship AI.
6. Add [penetration-testing.md](penetration-testing.md) when you want validation.

---

## Cross-references

- For LLM-specific security threats (prompt injection, indirect injection, excessive agency), see [`../ai-ml-llm/ai-safety-alignment.md`](../ai-ml-llm/ai-safety-alignment.md).
- For authentication implementation, see [`../frontend-backend/authentication.md`](../frontend-backend/authentication.md).
- For infrastructure hardening, see [`../devops-cloud/secrets-management.md`](../devops-cloud/secrets-management.md).

---

## Build progress

**Phase 12 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.