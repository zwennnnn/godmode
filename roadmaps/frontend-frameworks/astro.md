---
name: Astro
category: frontend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://astro.build/
  - https://docs.astro.build/
  - https://github.com/withastro/astro
  - https://docs.astro.build/en/getting-started/
  - https://docs.astro.build/en/concepts/why-astro/
  - https://docs.astro.build/en/concepts/islands/
  - https://docs.astro.build/en/guides/integrations-guide/
  - https://docs.astro.build/en/guides/content-collections/
  - https://docs.astro.build/en/concepts/server-islands/
  - https://starlight.astro.build/
  - https://docs.astro.build/en/guides/upgrade-to/v5/
  - https://astro.build/blog/astro-5/
tags: [astro, content, islands, mpa, ssr, partial-hydration, documentation]
---

# Astro

## One-liner

The web framework for content-driven sites — zero JS by default, islands of interactivity, ships Markdown / MDX / any UI framework — the default for marketing sites, docs, blogs, and content-heavy apps in 2026.

## What It Is

[Astro](https://astro.build/) is a web framework for building fast, content-driven websites. Its key innovation is the **Islands Architecture**: ship zero client-side JavaScript by default, and hydrate only the interactive components you choose.

The 2026 baseline is **Astro 5+**:

- **Astro 5** (Dec 2024) — **Server Islands** (selective server rendering inside an otherwise static page); unified content layer.
- **Content Layer API** — load content from anywhere (Markdown, MDX, CMS, API).
- **Astro Actions** — type-safe server functions.
- **View Transitions API** — multi-page SPA feel.
- **React / Vue / Svelte / Solid / Preact** integration.
- **SSR + SSG + Hybrid** modes.
- **Starlight** (Astro's docs framework — the fastest-growing docs tool).

Adoption: Astro is the **default for content-driven sites**. Used by Microsoft, Google, Cloudflare, Stripe (parts), The Verge, every modern docs site.

## When To Use It

- **Marketing site / blog / docs** — Astro's home turf.
- **Content-heavy app with islands of interactivity** — Astro's island model wins.
- **Zero JS by default** — best perf for content sites.
- **You want any UI framework** — Astro doesn't lock you in.
- **SEO + speed matter** — Astro ships minimal JS.
- **Documentation site** — Starlight is built on Astro.

## When NOT To Use It

- **Heavy SPA / dashboard** — use Next.js / Nuxt / SvelteKit.
- **Real-time apps** — not its strength.
- **You want one framework end-to-end** — Astro integrates React/Vue/Svelte but doesn't replace them.

## Why It Matters in 2026

Astro 5 Server Islands (Dec 2024) brought selective server rendering inside otherwise-static pages. Astro's content layer + zero-JS-by-default + multi-framework integration = the default for content-driven sites in 2026. Used by Microsoft, Google, Cloudflare for docs + marketing.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | Since 2021; v5 stable since 2024. |
| Community | 90 | Fast-growing; default for content sites. |
| Learning curve | 90 | Islands are intuitive; templates easy. |
| Performance | 100 | Zero JS by default; islands hydrate selectively. |
| Cost | 100 | Free OSS. |
| DX | 95 | Best for content + marketing. |
| Production readiness | 95 | Used by Microsoft, Google docs. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Next.js** | Heavy SPA / dashboard. | You want zero-JS marketing. |
| **SvelteKit** | You want Svelte end-to-end. | You want framework-agnostic islands. |
| **Qwik** | You want resumability. | You want simpler islands model. |
| **Hugo / Jekyll** | Pure static. | You need some interactivity. |

## Sources

- [Astro](https://astro.build/) — 2026
- [Astro Docs](https://docs.astro.build/) — 2026
- [Astro GitHub (withastro/astro)](https://github.com/withastro/astro) — 2026
- [Astro Getting Started](https://docs.astro.build/en/getting-started/) — 2026
- [Astro Why](https://docs.astro.build/en/concepts/why-astro/) — 2026
- [Astro Islands](https://docs.astro.build/en/concepts/islands/) — 2026
- [Astro Integrations](https://docs.astro.build/en/guides/integrations-guide/) — 2026
- [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/) — 2026
- [Astro Server Islands](https://docs.astro.build/en/concepts/server-islands/) — 2026
- [Starlight Docs](https://starlight.astro.build/) — 2026
- [Astro v5 Upgrade](https://docs.astro.build/en/guides/upgrade-to/v5/) — 2026
- [Astro 5 Release](https://astro.build/blog/astro-5/) — 2026