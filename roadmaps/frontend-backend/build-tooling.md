---
name: Build Tooling
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://vitejs.dev/
  - https://vite.dev/
  - https://vite.dev/guide/
  - https://github.com/vitejs/vite
  - https://turbo.build/
  - https://turbopack.com/
  - https://nextjs.org/docs/app/api-reference/turbopack
  - https://github.com/vercel/turbopack
  - https://esbuild.github.io/
  - https://github.com/evanw/esbuild
  - https://rolldown.rs/
  - https://github.com/rolldown/rolldown
  - https://webpack.js.org/
  - https://github.com/webpack/webpack
  - https://rspack.dev/
  - https://github.com/web-infra-dev/rspack
  - https://bun.sh/docs/bundler
  - https://oxc-project.github.io/
  - https://biomejs.dev/
tags: [build-tooling, vite, turbopack, esbuild, rolldown, webpack, rspack, bun, bundler]
---

# Build Tooling (Vite / Turbopack / Bun / esbuild)

## One-liner

The bundler + dev server that turns your source files into something the browser can run — and the tool that determines how fast you iterate.

## What It Is

A build tool does three jobs:

1. **Dev server** — serves your source files with on-demand transformation + HMR (hot module replacement).
2. **Bundler** — for production, bundles your many modules into optimized chunks (HTTP/2-friendly).
3. **Transpiler** — TS → JS, JSX → JS, modern syntax → browser-compatible syntax.

The 2026 landscape is unusually active because three waves are converging:

| Wave | Tools | Approach |
|------|-------|----------|
| **JS-native bundlers** (mature) | [Vite](https://vite.dev/), [esbuild](https://esbuild.github.io/), [Webpack](https://webpack.js.org/), [Rspack](https://rspack.dev/) | Bundlers in JS/Go/Rust; Vite uses native ESM + esbuild for dev, Rollup for prod |
| **Rust-native bundlers** (rising) | [Turbopack](https://turbo.build/), [Rolldown](https://rolldown.rs/), Rspack | Compiled in Rust for maximum speed; incremental computation |
| **Runtime-native bundlers** (emerging) | [Bun bundler](https://bun.sh/docs/bundler) | Part of the Bun runtime; integrated with JS engine |

### Vite (default in 2026)
- **Dev server**: native ESM, on-demand transformation via esbuild; **cold start <500ms** regardless of project size.
- **HMR**: instant, even with many components.
- **Prod build**: uses Rollup (will switch to Rolldown in v6).
- **Framework support**: React, Vue, Svelte, Solid, Lit, vanilla TS — all first-class.
- **v5+** (2024+) stable; **v6** (2026) replaces Rollup with **Rolldown** (Rust port of Rollup) for 5–10× faster prod builds.

### Turbopack (Vercel, Next.js)
- **Rust-native**, built by the Webpack creator.
- **Incremental computation engine** — caches work across builds; only re-computes what changed.
- **Stable for `next dev`** in Next.js 15; **beta for `next build`** (prod) in 2026.
- **Benchmark**: large Next.js apps see 5–10× faster dev cold start vs Webpack.

### Bun bundler
- **JS engine integration** — same runtime that runs your app bundles your code.
- **Fast for Bun-native projects**; less mature than Vite for general use in 2026.

### esbuild
- **Go-native**, extreme speed (~100× faster than Webpack for raw transpile).
- **Not a full bundler** — no tree-shaking, no chunk splitting, no HMR for many frameworks.
- **Used inside Vite** for dev transformation; standalone use is shrinking.

### Rolldown
- **Rust port of Rollup**, by the VoidZero / Vite team.
- **Drop-in Rollup replacement** with much faster prod builds.
- **Will be Vite's prod bundler** in v6 (replacing Rollup).

### Rspack
- **Rust-native Webpack-compatible** bundler (by ByteDance).
- **Drop-in for Webpack** with major speed wins; ecosystem of Webpack loaders mostly works.
- **Used in production** at ByteDance, Microsoft, others.

### Webpack
- **The old default** (2014–2022). Still works; still has the largest plugin ecosystem.
- **Slow** compared to modern alternatives; being phased out of greenfield projects.

## When To Use It

### Vite
- **Default for new SPAs and most frameworks** (React, Vue, Svelte, Solid, vanilla TS).
- **You want the fastest dev iteration** with the best HMR.
- **You're not on Next.js** (Next.js has its own build pipeline).

### Turbopack
- **You're on Next.js 15+** — enable via `--turbo` flag, watch the dev speed difference.
- **You have a very large app** and Webpack dev starts take >30s.

### Bun bundler
- **You're already on Bun runtime** for the backend.
- **You want a unified toolchain** (install + run + bundle + test in Bun).

### esbuild
- **You're building a CLI / library** that needs fast compilation but no bundling.
- **Inside a custom pipeline** where Vite is overkill.

### Rolldown
- **You want Rust-native prod builds** with Rollup-compatible output. (Use via Vite 6 when stable.)

### Rspack
- **You have a large Webpack codebase** you want to speed up without rewriting config.
- **You're on a framework that integrates Rspack** (Modern.js, others).

### Webpack
- **Legacy project** — don't migrate unless you have a strong reason.
- **You need a Webpack-specific plugin** that no other bundler supports.

## When NOT To Use It

### Vite
- **You're on Next.js** — Next has its own pipeline (Webpack or Turbopack).

### Turbopack
- **You're not on Next.js** — Turbopack is tightly coupled to Next.js in 2026.
- **You need stable prod builds today** — `next build --turbopack` is still beta.

### Bun bundler
- **You need a mature plugin ecosystem** — Vite's plugin ecosystem is bigger.
- **You're not on Bun runtime** — minimal benefit otherwise.

### esbuild
- **You need HMR, code splitting, full bundling features** — Vite wraps esbuild + Rollup for this.

### Rolldown
- **Greenfield in 2026** — wait for Vite 6 stable, or use Vite 5 with Rollup.

### Rspack
- **Small greenfield project** — Vite is simpler.

### Webpack
- **New project in 2026** — start with Vite (or Turbopack if Next.js).

## Why It Matters in 2026

Three forces:

1. **Rust-native bundlers are the new normal.** Turbopack, Rolldown, Rspack all moved from "experimental" to "production-ready" in 2025. Webpack's era is ending; Vite's era is mid; Rust-bundlers' era is starting.
2. **Dev iteration speed is now the bottleneck for AI-assisted development.** When you're regenerating code every 30 seconds with Cursor / Copilot / Claude Code, a 30s Webpack rebuild kills flow. Vite / Turbopack's <500ms HMR keeps you in the zone.
3. **Vite 6 + Rolldown unification.** The Vite team's plan is to replace Rollup with Rolldown in Vite 6 (2026), giving Vite a single Rust-native pipeline from dev to prod.

Practitioner defaults in 2026:
- **React / Vue / Svelte SPA** → **Vite 5** (Vite 6 with Rolldown when stable).
- **Next.js app** → **Next.js 15 with Turbopack dev** (`next dev --turbo`); Webpack or Turbopack for prod.
- **CLI / library** → **tsup** (esbuild wrapper) or **unbuild**.
- **Bun-native project** → **Bun bundler**.
- **Legacy Webpack app** → stay on Webpack unless you're ready to migrate (consider Rspack for a speedup without rewrites).

## Scoring Matrix (0–100)

### Vite
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 5+ years old; v5 stable; v6 in 2026 with Rolldown. |
| Community | 95 | The default for non-Next.js SPAs; massive plugin ecosystem. |
| Learning curve | 90 | Near-zero config; conventions are sensible. |
| Performance | 95 | Dev cold start <500ms; HMR <50ms; prod with Rolldown will be 5–10× Rollup. |
| Cost | 95 | Free. |
| DX (developer experience) | 95 | Best-in-class for greenfield. |
| Production readiness | 95 | Used by every major frontend project not on Next.js. |

### Turbopack
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 70 | Dev stable in Next 15; prod beta; couple years from Vite-equivalent maturity. |
| Community | 80 | Growing fast within Next.js community. |
| Learning curve | 90 | Just `--turbo` flag. |
| Performance | 95 | Fastest large-app cold start in 2026 benchmarks. |
| Cost | 95 | Free. |
| DX | 90 | Excellent where integrated. |
| Production readiness | 75 | Dev: yes. Prod: beta. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Parcel** | Zero-config; you want it to "just work". | You need framework-specific HMR / plugins. |
| **Snowpack** | Historical; pre-Vite era. | Vite replaced it for most uses. |
| **Rollup (standalone)** | You're bundling a library. | You're building an app — Vite wraps Rollup better. |
| **tsup** | You're bundling a TS library with zero config. | You need HMR / dev server. |
| **Metro (React Native)** | React Native projects. | Web projects. |
| **Biome / oxc (lint + format, not bundle)** | You want Rust-native lint + format. | You need bundling. |

## Sources

- [Vite Official Site](https://vite.dev/) — 2026
- [Vite Guide](https://vite.dev/guide/) — 2026
- [Vite GitHub (vitejs/vite)](https://github.com/vitejs/vite) — 2026
- [Turbopack Site](https://turbopack.com/) — 2026
- [Turbopack in Next.js](https://nextjs.org/docs/app/api-reference/turbopack) — 2026
- [Turbopack GitHub (vercel/turbopack)](https://github.com/vercel/turbopack) — 2026
- [esbuild](https://esbuild.github.io/) — 2026
- [esbuild GitHub (evanw/esbuild)](https://github.com/evanw/esbuild) — 2026
- [Rolldown](https://rolldown.rs/) — 2026
- [Rolldown GitHub (rolldown/rolldown)](https://github.com/rolldown/rolldown) — 2026
- [Webpack](https://webpack.js.org/) — 2026
- [Webpack GitHub (webpack/webpack)](https://github.com/webpack/webpack) — 2026
- [Rspack](https://rspack.dev/) — 2026
- [Rspack GitHub (web-infra-dev/rspack)](https://github.com/web-infra-dev/rspack) — 2026
- [Bun Bundler Docs](https://bun.sh/docs/bundler) — 2026
- [Oxc Project](https://oxc-project.github.io/) — 2026
- [Biome](https://biomejs.dev/) — 2026