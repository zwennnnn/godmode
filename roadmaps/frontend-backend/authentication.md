---
name: Authentication
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://authjs.dev/
  - https://clerk.com/docs
  - https://www.better-auth.com/
  - https://lucia-auth.com/
  - https://github.com/pilcrowOnPaper/arctic
  - https://supabase.com/docs/guides/auth
  - https://docs.stytch.com/
  - https://auth0.com/docs
  - https://workos.com/docs
  - https://github.com/nextauthjs/next-auth
  - https://owasp.org/www-project-top-10-for-large-language-model-applications/
  - https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
  - https://datatracker.ietf.org/doc/html/rfc6749
tags: [authentication, auth, oauth, oidc, saml, jwt, session, auth.js, clerk, better-auth, lucia]
---

# Authentication (Auth.js / Clerk / Better-Auth / Lucia)

## One-liner

Who is this user, and what are they allowed to do — the layer that gates every protected resource in your app.

## What It Is

Authentication (authn) is verifying *who* a user is; authorization (authz) is deciding *what* they can do. In 2026, most apps separate these:

- **Authn** is handled by an **auth library or service** (Auth.js, Clerk, Better-Auth, Lucia, Supabase Auth, Auth0, WorkOS, Stytch).
- **Authz** is handled by your app code (or a policy engine like Oso, Cerbos, OpenFGA).

The four leading approaches in 2026:

| Tool | Type | Best for |
|------|------|----------|
| **[Auth.js (formerly NextAuth)](https://authjs.dev/)** | OSS library | Next.js / generic JS apps; OAuth + email + credentials; huge provider ecosystem. |
| **[Clerk](https://clerk.com/docs)** | Managed service | Drop-in auth + user management UI + orgs + MFA; fastest path to production. |
| **[Better-Auth](https://www.better-auth.com/)** | OSS library (2025+) | Modern TS-first; batteries-included; framework-agnostic; rapidly gaining share. |
| **[Lucia](https://lucia-auth.com/)** | OSS library | Low-level session primitives; you build the UI; great for full control. |

Plus **[Supabase Auth](https://supabase.com/docs/guides/auth)** (if you're on Supabase), **[Auth0](https://auth0.com/docs)**, **[WorkOS](https://workos.com/docs)** (enterprise SSO / SAML), **[Stytch](https://docs.stytch.com/)** (passwordless + MFA), and **[Arctic](https://github.com/pilcrowOnPaper/arctic)** (OAuth primitives for TS).

Core concepts every auth system implements:
- **Sessions** — server-side state tracking a logged-in user (cookie / token).
- **JWTs (JSON Web Tokens)** — stateless tokens; signed (and optionally encrypted); can carry claims.
- **OAuth 2.0 / OIDC** — delegate auth to Google, GitHub, Microsoft, Apple, etc.
- **SAML** — enterprise SSO (WorkOS, Auth0, Microsoft Entra).
- **Passwordless** — magic links, WebAuthn / passkeys, one-time codes.
- **MFA** — TOTP, WebAuthn, SMS (deprecated for security).
- **Passkeys (WebAuthn)** — the 2024–2026 standard for phishing-resistant auth.

## When To Use It

### Auth.js (NextAuth)
- **You're on Next.js / any JS framework.** Default.
- **You want OAuth providers** (Google, GitHub, etc.) without managing OAuth flows yourself.
- **You want email magic-link auth** with minimal config.
- **You want full control** of the auth data (it lives in your DB).

### Clerk
- **You want the fastest path to production.** Pre-built UI, user management, orgs, MFA all included.
- **You need enterprise SSO** (SAML, OIDC) without buying WorkOS.
- **You can afford ~$25–$500/mo** for managed service (free tier available).
- **You want multi-tenancy primitives** out of the box (Organizations, Invitations, Roles).

### Better-Auth
- **TS-first, framework-agnostic** project.
- **You want OSS flexibility + modern ergonomics.** Better-Auth is the 2025–2026 challenger.
- **You need plugins** (2FA, magic links, organizations, admin, etc.) — first-class plugin system.

### Lucia
- **You want low-level control** and to build your own UI/flows.
- **You're on Deno, Bun, or a non-Next.js framework.**
- **You want a small, focused library** (Lucia v3 is "the primitives, not the framework").

### Supabase Auth
- **You're using Supabase for DB.** Built-in integration.
- **You need Row-Level Security** with JWT claims.

### Auth0 / WorkOS / Stytch
- **Enterprise / regulated industries** with SSO / SAML / SCIM requirements.
- **You need compliance certifications** (SOC2, HIPAA) handled by the auth vendor.

## When NOT To Use It

### Auth.js
- **You need enterprise SSO** (SAML) — Clerk or WorkOS is simpler.
- **You don't want to manage UI yourself** — Clerk ships components.

### Clerk
- **You're allergic to vendor lock-in or per-MAU pricing.**
- **You need full control of auth data** (some setups require DB-resident sessions only).
- **You're a tiny hobby project** with no budget.

### Better-Auth
- **You need a battle-tested library** with years of production usage — Auth.js is more proven (Better-Auth is younger).

### Lucia
- **You want pre-built UI / user management.** Lucia is primitives; you'd build everything.

### Any of them
- **You're building a true passwordless / passkey-only app** — Stytch or your own WebAuthn code may be cleaner.
- **You already have an auth system.** Don't switch for no reason.

## Why It Matters in 2026

Three forces:

1. **Passkeys (WebAuthn) went mainstream.** Apple, Google, Microsoft, and every major browser support passkeys natively. The "password is dying" prediction is real; in 2026, all major auth libraries support passkeys as first-class. Phishing-resistant auth is no longer a nice-to-have.
2. **Better-Auth emerged as the modern OSS challenger.** While Clerk dominates "managed," Better-Auth captured the "I want OSS but with batteries" niche in 2025–2026, particularly in TS-first monorepos.
3. **Auth complexity moved up the stack.** OAuth flows, MFA, sessions, orgs, invitations — building all this yourself is multi-month work. The decision is no longer "build vs buy" but "which library / service."

Practitioner defaults in 2026:
- **Next.js + want control** → Auth.js (v5) or Better-Auth.
- **Next.js + want speed** → Clerk.
- **React Native + Supabase** → Supabase Auth.
- **Enterprise / SAML / SCIM** → WorkOS or Auth0.
- **Pure Deno / Bun** → Lucia + Arctic.
- **Passkey-first product** → Stytch or Better-Auth + WebAuthn.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | Auth.js 8+ years; Clerk 6+ years; Better-Auth 1–2 years (still maturing); Lucia 5+ years. |
| Community | 90 | Auth.js huge; Clerk large; Better-Auth rapidly growing; Lucia focused. |
| Learning curve | 60 | OAuth + sessions + JWTs + MFA is a lot; libraries abstract much but mastery takes study. |
| Performance | 90 | All handle millions of users; session lookup is fast (cookie + DB or JWT verify). |
| Cost | 75 | OSS libraries free; Clerk / Auth0 / WorkOS charge per MAU (can get expensive at scale). |
| DX (developer experience) | 90 | Clerk best (pre-built UI); Auth.js good (config-first); Better-Auth best for TS purists; Lucia more DIY. |
| Production readiness | 90 | All in production at major companies; Clerk and Auth0 especially battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Build it yourself** | You need a feature none of the libraries support. | You don't have a year to spend. Don't. |
| **Firebase Auth** | You're on Firebase / GCP. | You're not on Firebase. |
| **AWS Cognito** | You're all-in on AWS; you need SAML. | DX is dated; pricing model confusing. |
| **Magic links only** | Low-stakes consumer apps; you want zero password management. | You need MFA / enterprise. |
| **Passkeys-only (WebAuthn)** | Consumer apps in 2026 — phishing-resistant + passwordless. | Enterprise / non-technical users who don't have passkeys yet. |
| **Stateless JWTs only (no sessions)** | Pure API / mobile; you control the secret. | Browser-first apps where CSRF / XSS risk is real. |

## Sources

- [Auth.js (NextAuth)](https://authjs.dev/) — 2026
- [Clerk Docs](https://clerk.com/docs) — 2026
- [Better-Auth](https://www.better-auth.com/) — 2026
- [Lucia Auth](https://lucia-auth.com/) — 2026
- [Arctic (OAuth primitives, pilcrowOnPaper)](https://github.com/pilcrowOnPaper/arctic) — 2026
- [Supabase Auth Docs](https://supabase.com/docs/guides/auth) — 2026
- [Stytch Docs](https://docs.stytch.com/) — 2026
- [Auth0 Docs](https://auth0.com/docs) — 2026
- [WorkOS Docs](https://workos.com/docs) — 2026
- [NextAuth GitHub (nextauthjs/next-auth)](https://github.com/nextauthjs/next-auth) — 2026
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — 2025
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — 2026
- [IETF RFC 6749 — OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) — 2026