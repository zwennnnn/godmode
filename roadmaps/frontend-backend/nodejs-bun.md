---
name: Node.js and Bun
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://nodejs.org/en/about
  - https://nodejs.org/en/docs
  - https://nodejs.org/en/blog
  - https://github.com/nodejs/node
  - https://bun.sh/
  - https://bun.sh/docs
  - https://bun.sh/docs/cli/run
  - https://bun.sh/docs/runtime/bunfig
  - https://github.com/oven-sh/bun
  - https://deno.com/
  - https://deno.com/blog
  - https://github.com/denoland/deno
  - https://expressjs.com/
  - https://fastify.dev/
  - https://hono.dev/
  - https://elysiajs.com/
  - https://stateofjs.com/
tags: [nodejs, bun, deno, javascript-runtime, backend, server, fastify, hono, elysia]
---

# Node.js and Bun

## One-liner

The dominant JavaScript server runtimes in 2026 — Node.js (mature, massive ecosystem) and Bun (fast, all-in-one, batteries-included).

## What It Is

A JavaScript runtime lets you execute JS/TS code outside the browser — on a server, at the edge, in a CLI. **Node.js** has been the default since 2009 (Chrome V8 + libuv event loop + npm ecosystem). **Bun** (2022+) is a newer runtime built on JavaScriptCore with native TS/JSX execution, a built-in bundler, transpiler, test runner, and package manager. **Deno** (2018+) is the third option from the original Node creator, focused on security + TS-first.

### Node.js (mature default)
- **Current LTS**: Node 22 / 24 in 2026; **Active LTS** lines every 6 months, **Maintenance LTS** for 30+ months.
- **Native TypeScript** support (since v22.6, behind a flag → default in v24) — `node file.ts` works.
- **Built-in test runner** (`node:test`) stable; fetch / WebStreams / WebCrypto standard.
- **Permissions model** (experimental).
- **Single executable applications** (SEA) — bundle a Node app into one binary.
- **V8 12.x** for top-tier JS perf.
- Massive ecosystem: **>3M npm packages**, the largest package registry on Earth.

### Bun (fast newcomer)
- **JavaScriptCore** engine (Safari's) instead of V8; faster cold start, lower memory.
- **Native TS / JSX** execution — no build step needed.
- **Built-in**: bundler, transpiler, package manager (`bun install` ~30× faster than `npm install`), test runner (`bun test`), script runner.
- **Node-API compatible** — runs most npm packages, including Express middleware.
- **Built-in SQLite** driver (`bun:sqlite`).
- **Built-in HTTP server** with native `Bun.serve()` (Web Standards + Bun-specific extensions).
- **Bun.lock** for reproducible installs.

### Deno (security-focused)
- **TypeScript-native** by default.
- **Permission-based sandbox** by default (no FS/network unless granted).
- **JSR** (JavaScript Registry) — modern alternative to npm.
- **Deno Deploy** — edge runtime.
- Smaller ecosystem; niche but loved for security-first apps.

### Server frameworks (Node / Bun / Deno)
| Framework | Runtime | Notes |
|-----------|---------|-------|
| **Express** | Node | The 10+ year default; minimal; enormous middleware ecosystem; mature but stagnant. |
| **Fastify** | Node | Schema-first; faster than Express; built-in JSON Schema validation; great TS support. |
| **Hono** | Bun / Deno / Node / Edge | Ultra-fast, Web-Standards-first; perfect for edge / Cloudflare / Bun. |
| **Elysia** | Bun | TypeScript-first; great DX; fastest in benchmarks. |
| **NestJS** | Node | Opinionated, Angular-inspired, enterprise-ready. |
| **Koa** | Node | Minimal, modern, by the Express team. |

Adoption (per [State of JS](https://stateofjs.com/)):
- **Node.js**: ~95% of JS developers have used it; the default backend JS runtime.
- **Bun**: ~25% adoption in 2024 surveys; rapidly growing for new projects and tools (Vite, Astro, etc. are testing/using Bun).
- **Deno**: ~10% adoption; strong in security-conscious + edge-first shops.

## When To Use It

### Node.js
- **You're building any JS backend.** Default.
- **You need the maximum ecosystem** (Express, Passport, Mongoose, etc.).
- **You're deploying to AWS Lambda, Google Cloud Functions, Vercel Functions** — all Node-first.
- **You need long-term stability + LTS.** Node's LTS cadence is best-in-class.

### Bun
- **Greenfield project in 2026.** Bun's DX is materially better (TS-native, 30× faster installs, all-in-one).
- **You want the fastest cold start + lowest memory** (edge functions, CLI tools, scripts).
- **You need SQLite without a separate driver** (`bun:sqlite` is built-in).
- **You're building a high-throughput API** — Hono + Bun benchmarks fastest in 2026.
- **You're migrating from Node** — Bun is Node-API compatible; usually a drop-in.

### Deno
- **You need the strongest sandbox model** (security-first; default no FS/network).
- **You're deploying to Deno Deploy** (edge runtime).
- **You want TS-native + JSR without config.**

## When NOT To Use It

### Node.js
- **You need the absolute fastest cold start.** Bun / Deno win on cold-start benchmarks.
- **You're building a single-binary CLI** and Bun/Go/Rust are better fits.

### Bun
- **You're using a heavy native module** (some still have Node-only N-API issues).
- **You need 100% production-validated stability at scale** (Node has more years of battle-testing).
- **Your team has zero Bun experience and the timeline is tight.** Node is the safe default.

### Deno
- **You depend on a large Node-only package** that hasn't been ported to JSR / npm-compat.
- **You want the most popular runtime for hiring.** Node dominates.

## Why It Matters in 2026

Three forces:

1. **TS-native execution is the new normal.** Bun, Deno, and Node 22+ all run TypeScript directly. The build-step is going away.
2. **Edge runtimes matured.** Cloudflare Workers, Vercel Edge, Deno Deploy, Bun on Fly — all production-ready. The choice is no longer "Node monolith vs serverless" but "which runtime, where, and at what cold-start cost."
3. **Bun's all-in-one tooling pressured npm.** `bun install` is 30× faster than `npm install`. npm shipped performance improvements in response; pnpm remains the speed-focused incumbent.

Practitioner defaults in 2026:
- **New web app**: Next.js (Vercel-managed Node) for the frontend; **Bun + Hono** for separate API services; **Node 22 LTS** for legacy / conservative deployments.
- **Edge / Cloudflare**: **Hono** on Workers.
- **CLI / script**: **Bun** for speed + TS.
- **Heavy enterprise**: **Node 22 LTS + NestJS or Fastify**.

## Scoring Matrix (0–100)

### Node.js
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 16+ years old (2009); the default JS backend runtime. |
| Community | 100 | >3M npm packages; every JS dev has used it; the dominant hiring pool. |
| Learning curve | 80 | Easy to start; deep ecosystem means months to master. |
| Performance | 80 | V8 is fast; native HTTP/2 / fetch; some cold-start overhead vs Bun. |
| Cost | 95 | Free; runs anywhere. |
| DX (developer experience) | 80 | npm is slower than pnpm/Bun; debugging is excellent (--inspect). |
| Production readiness | 100 | Battle-tested at every scale; LTS guarantee; the safe default. |

### Bun
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 65 | 3+ years old (2022); v1.0 in 2023; v1.x stable in 2026; still younger than Node. |
| Community | 75 | Fast-growing; ~25% adoption; loved by DX-focused devs. |
| Learning curve | 90 | Drop-in for most Node patterns; batteries-included means fewer new concepts. |
| Performance | 95 | Fastest cold start, lowest memory, fastest installs in 2026 benchmarks. |
| Cost | 95 | Free; same infra as Node. |
| DX (developer experience) | 100 | TS-native, all-in-one, fastest installs — best-in-class. |
| Production readiness | 80 | Used in production at Notion, Anthropic tools, many startups; some edge cases still surfacing. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Deno** | You need security sandbox by default; you deploy to Deno Deploy; you love TS-native. | You depend on Node-specific packages or want maximum ecosystem. |
| **Python (FastAPI / Django)** | Your team is Python-first; ML / data work. | You need the JS ecosystem. |
| **Go** | You need maximum throughput, single-binary deploy, low memory. | You want a fast-moving web ecosystem. |
| **Rust (Axum / Actix)** | You need maximum performance + safety. | You want fast iteration; team doesn't know Rust. |
| **Java (Spring Boot)** | Enterprise; huge existing investment. | You want fast iteration. |
| **Elixir / Phoenix** | You need soft real-time (chat, presence). | You want mainstream hiring. |

## Sources

- [Node.js — About](https://nodejs.org/en/about) — 2026
- [Node.js Docs](https://nodejs.org/en/docs) — 2026
- [Node.js Blog](https://nodejs.org/en/blog) — 2026
- [Node.js GitHub (nodejs/node)](https://github.com/nodejs/node) — 2026
- [Bun Official Site](https://bun.sh/) — 2026
- [Bun Docs](https://bun.sh/docs) — 2026
- [Bun CLI Run](https://bun.sh/docs/cli/run) — 2026
- [Bunfig Reference](https://bun.sh/docs/runtime/bunfig) — 2026
- [Bun GitHub (oven-sh/bun)](https://github.com/oven-sh/bun) — 2026
- [Deno](https://deno.com/) — 2026
- [Deno Blog](https://deno.com/blog) — 2026
- [Deno GitHub (denoland/deno)](https://github.com/denoland/deno) — 2026
- [Express.js](https://expressjs.com/) — 2026
- [Fastify](https://fastify.dev/) — 2026
- [Hono](https://hono.dev/) — 2026
- [Elysia](https://elysiajs.ai/) — 2026
- [State of JS](https://stateofjs.com/) — 2024+