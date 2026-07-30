---
name: Qwik
category: frontend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://qwik.dev/
  - https://qwik.dev/docs/
  - https://github.com/QwikDev/qwik
  - https://qwik.dev/docs/components/
  - https://qwik.dev/docs/concepts/resumable/
  - https://qwik.dev/docs/integrations/react/
  - https://qwik.dev/docs/lazy/
  - https://qwik.dev/docs/route-loader/
  - https://qwik.dev/docs/action/
  - https://builder.io/blog/qwik-1
  - https://qwik.dev/docs/qwikcity/
tags: [qwik, resumability, zero-js, instant-on, web-performance, server-rendering, signals]
---

# Qwik

## One-liner

The resumable web framework — instead of hydration, it serializes app state into HTML and resumes on the client — instant Time-to-Interactive even on slow devices, the most ambitious perf-focused framework in 2026.

## What It Is

[Qwik](https://qwik.dev/) is a web framework that uses **resumability** instead of hydration. The server serializes the entire app state into HTML; the client picks up where the server left off without re-executing anything. The result: instant interactivity, near-zero JS shipped by default.

The 2026 baseline is **Qwik 1.x** (1.0 released 2023; 1.x stable since):

- **Qwik (core)** — the framework; resumable components.
- **Qwik City** — meta-framework (SSR + SSG + file-based routing + endpoints + middleware).
- **Resumability** — the core innovation.
- **Lazy loading** — every component is lazy until needed.
- **QRLs** — Qwik Resource Locators; on-demand JS.
- **Signals** — fine-grained reactivity.
- **JSX-like syntax** with `$` markers (`useSignal`, `useTask$`).
- **Integrations** — React via Qwik-React, Tailwind, etc.
- **Builder.io** — the company behind Qwik.

Adoption: Qwik is the **fastest TTI framework** in 2026 (Google Web Vitals). Used by Builder.io, select performance-critical sites, indie devs who care about Core Web Vitals.

## When To Use It

- **TTI / Core Web Vitals are #1 priority** — Qwik's reason to exist.
- **Slow mobile devices / emerging markets** — resumability shines.
- **Content site with islands of interactivity** — alternative to Astro.
- **You want zero JS by default** — Qwik ships even less than Astro.
- **You want to innovate** — Qwik's architecture is genuinely novel.

## When NOT To Use It

- **You want the ecosystem** — React wins.
- **You want familiar React DX** — Qwik has its own model; learning curve.
- **You want maximum library support** — React / Vue have more.
- **Massive SPA** — Qwik shines for content; SPA frameworks may be better.

## Why It Matters in 2026

Qwik 1.x (released 2023) stabilized resumability. The architecture is genuinely novel — instead of hydration, the server serializes state into HTML; the client resumes without re-executing. The fastest TTI framework in 2026 Core Web Vitals benchmarks. Best for slow mobile devices / emerging markets.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | 1.x stable since 2023. |
| Community | 75 | Smaller but growing. |
| Learning curve | 70 | New mental model ($ markers, QRLs). |
| Performance | 100 | Fastest TTI; near-zero JS by default. |
| Cost | 100 | Free OSS. |
| DX | 80 | Different from React/Vue; learning curve. |
| Production readiness | 80 | Used by Builder.io, select perf-critical sites. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Astro** | Content + islands. | You want resumability everywhere. |
| **SvelteKit** | Familiar Svelte stack. | You want zero JS always. |
| **Next.js** | You want React ecosystem. | You want min JS shipped. |

## Sources

- [Qwik](https://qwik.dev/) — 2026
- [Qwik Docs](https://qwik.dev/docs/) — 2026
- [Qwik GitHub (QwikDev/qwik)](https://github.com/QwikDev/qwik) — 2026
- [Qwik Components](https://qwik.dev/docs/components/) — 2026
- [Qwik Resumable](https://qwik.dev/docs/concepts/resumable/) — 2026
- [Qwik React Integration](https://qwik.dev/docs/integrations/react/) — 2026
- [Qwik Lazy](https://qwik.dev/docs/lazy/) — 2026
- [Qwik Route Loader](https://qwik.dev/docs/route-loader/) — 2026
- [Qwik Action](https://qwik.dev/docs/action/) — 2026
- [Builder.io Blog — Qwik 1](https://builder.io/blog/qwik-1) — 2026
- [Qwik City](https://qwik.dev/docs/qwikcity/) — 2026