---
name: Express.js
category: backend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://expressjs.com/
  - https://github.com/expressjs/express
  - https://expressjs.com/en/starter/installing.html
  - https://expressjs.com/en/guide/routing.html
  - https://expressjs.com/en/guide/migrating-5.html
  - https://expressjs.com/en/resources/middleware.html
  - https://expressjs.com/en/4x/api.html
  - https://expressjs.com/en/5x/api.html
  - https://www.npmjs.com/package/express
tags: [express, expressjs, nodejs, javascript, typescript, middleware, api]
---

# Express.js

## One-liner

The minimal, unopinionated Node.js web framework — the original and still dominant choice for Node.js HTTP servers in 2026.

## What It Is

[Express](https://expressjs.com/) is a minimal, flexible Node.js web application framework that provides robust features for web + mobile APIs. It's been the standard since 2010, with a huge middleware ecosystem.

The 2026 baseline is **Express 5.x** (Express 5 released 2024):

- **Express 5** — async error handling, async middleware, native Promise support.
- **Massive middleware ecosystem** — `morgan`, `cors`, `helmet`, `body-parser`, `cookie-parser`, `passport`, `multer`, etc.
- **Minimal core** — unopinionated; you pick your ORM / template / auth.
- **TypeScript support** — `@types/express`.

Adoption: Express remains the most-used Node.js web framework. Used by every Node.js dev at some point.

## When To Use It

- **Minimal Node.js HTTP server** — Express's sweet spot.
- **API server** — REST / GraphQL / etc.
- **Middleware-heavy apps** — huge middleware ecosystem.
- **You want full control** — Express is unopinionated.

## When NOT To Use It

- **You want structure** — NestJS is opinionated.
- **TypeScript-first** — NestJS, tRPC, or Fastify are better.
- **Modern / fast** — Fastify or Hono are faster.

## Why It Matters in 2026

Express 5 (released 2024) brought async error handling and Promise support, modernizing the original Node.js framework. Express remains the default for new Node.js APIs and the basis for many other frameworks (NestJS, Fastify started from Express concepts). The middleware ecosystem is unmatched.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 14+ years; the original. |
| Community | 100 | Massive; middleware ecosystem. |
| Learning curve | 85 | Easy; unopinionated. |
| Performance | 80 | Good; Fastify / Hono are faster. |
| Cost | 100 | Free OSS. |
| DX | 85 | Simple; many middleware. |
| Production readiness | 100 | Battle-tested everywhere. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Fastify** | Maximum Node.js perf. | Middleware ecosystem matters. |
| **Hono** | Edge runtimes; modern. | Stable ecosystem matters. |
| **NestJS** | Opinion + structure. | You want minimal. |
| **Koa** | Modern async middleware. | Ecosystem matters. |

## Sources

- [Express](https://expressjs.com/) — 2026
- [Express GitHub (expressjs/express)](https://github.com/expressjs/express) — 2026
- [Express — Installing](https://expressjs.com/en/starter/installing.html) — 2026
- [Express — Routing](https://expressjs.com/en/guide/routing.html) — 2026
- [Express — Migrating to 5](https://expressjs.com/en/guide/migrating-5.html) — 2026
- [Express Middleware](https://expressjs.com/en/resources/middleware.html) — 2026
- [Express 4 API](https://expressjs.com/en/4x/api.html) — 2026
- [Express 5 API](https://expressjs.com/en/5x/api.html) — 2026
- [Express on npm](https://www.npmjs.com/package/express) — 2026