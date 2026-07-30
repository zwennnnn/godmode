---
name: Frontend + Backend Full-Stack
slug: frontend-backend
source: https://roadmap.sh/frontend + https://roadmap.sh/backend
last-updated: 2026-07-30
tech-count: 10
status: in-progress
---

# Frontend + Backend Full-Stack Roadmap

> **Category:** Technologies for building production web applications end-to-end — UI layer, server layer, data layer, and the seams between them.
> **Sources:** [roadmap.sh/frontend](https://roadmap.sh/frontend), [roadmap.sh/backend](https://roadmap.sh/backend), [roadmap.sh/full-stack](https://roadmap.sh/full-stack)

This roadmap covers the core stack for shipping full-stack web products in 2026: language foundation, UI library, meta-framework, runtime, API design, database, authentication, state management, styling, and build tooling. The 10 picks below are the ones that actually decide your product's velocity, scalability, and hiring pool.

---

## Technologies (all researched 2026-07-30)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | TypeScript | [typescript.md](typescript.md) | researched |
| 2 | React | [react.md](react.md) | researched |
| 3 | Next.js | [nextjs.md](nextjs.md) | researched |
| 4 | Node.js / Bun | [nodejs-bun.md](nodejs-bun.md) | researched |
| 5 | API Design (REST / GraphQL / tRPC / gRPC) | [api-design.md](api-design.md) | researched |
| 6 | PostgreSQL | [postgresql.md](postgresql.md) | researched |
| 7 | Authentication (Auth.js / Clerk / Better-Auth / Lucia) | [authentication.md](authentication.md) | researched |
| 8 | State Management (Zustand / Redux Toolkit / Jotai / TanStack Query) | [state-management.md](state-management.md) | researched |
| 9 | CSS Architecture (Tailwind v4 / Vanilla Extract / Panda / CSS Modules) | [css-architecture.md](css-architecture.md) | researched |
| 10 | Build Tooling (Vite / Turbopack / Bun / esbuild / Rolldown) | [build-tooling.md](build-tooling.md) | researched |

---

## Quick Decision Guide

### If you're building an MVP web SaaS in 2026

The minimum viable stack:

1. **TypeScript** (strict) — non-negotiable.
2. **Next.js 15** (App Router) — covers frontend + API + auth boilerplate + deploy.
3. **PostgreSQL** — Neon or Supabase for managed; pglite for local dev.
4. **Auth.js** (NextAuth) or **Clerk** — Clerk if speed-to-prod matters; Auth.js if you want full control.
5. **Tailwind CSS v4** + **shadcn/ui** — fastest path to a polished UI.
6. **TanStack Query** for any client-side fetching; rely on Server Components for the rest.
7. **Zustand** only if you have cross-component client state; otherwise `useState` + Server Components.
8. **Drizzle ORM** or **Prisma** for DB access (TS-first).
9. **Vercel** for hosting — fast to ship, expensive at scale; Cloudflare / self-host if needed.

### If you're building a custom backend (API service, microservice)

1. **TypeScript** + **Bun** (greenfield) or **Node.js 22 LTS** (conservative).
2. **Hono** (Bun/edge) or **Fastify** (Node) for HTTP.
3. **Drizzle ORM** → PostgreSQL.
4. **tRPC** if your only client is TS; **REST + OpenAPI** if multiple clients.
5. **Zod** / **Valibot** for input validation.
6. **Pino** for logging; **OpenTelemetry** for traces.

### If you're building an enterprise / regulated app

- **TypeScript strict** + ESLint + Biome for code quality.
- **Next.js** (or **Remix / React Router 7** if you prefer loader/action model).
- **PostgreSQL** self-hosted or on AWS RDS / Cloud SQL.
- **Auth0** or **WorkOS** for SSO / SAML / SCIM.
- **shadcn/ui** or **Mantine** for UI.
- **Datadog** or **New Relic** for APM.

---

## Cross-references

- If the app needs AI features, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- If the app needs cloud deployment / k8s / Terraform, see [`../devops-cloud/README.md`](../devops-cloud/README.md) (Phase 4).
- If the app is mobile-first, see [`../mobile/README.md`](../mobile/README.md) (Phase 5).

---

## Build progress

**Phase 3 complete** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`. Next: Phase 4 (devops-cloud roadmap).

---

## Cross-references

- If the app needs AI features, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- If the app needs cloud deployment, see [`../devops-cloud/README.md`](../devops-cloud/README.md) (Phase 4).
- If the app is mobile-first, see [`../mobile/README.md`](../mobile/README.md) (Phase 5).

---

## Build progress

**Phase 3 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.