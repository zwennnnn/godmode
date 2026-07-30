---
name: Next.js
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://nextjs.org/
  - https://nextjs.org/docs
  - https://nextjs.org/blog
  - https://github.com/vercel/next.js
  - https://nextjs.org/docs/app
  - https://nextjs.org/docs/app/api-reference/file-conventions/route
  - https://nextjs.org/docs/app/building-your-application/routing
  - https://nextjs.org/docs/app/building-your-application/data-fetching
  - https://nextjs.org/docs/app/building-your-application/caching
  - https://vercel.com/docs
  - https://nextjs.org/docs/app/building-your-application/deploying
  - https://nextjs.org/docs/app/building-your-application/testing
tags: [nextjs, react, server-components, app-router, vercel, ssr, ssg, edge, meta-framework]
---

# Next.js

## One-liner

Vercel's React meta-framework — the default way to ship production React apps in 2026, with Server Components, Server Actions, file-based routing, and edge deploy built in.

## What It Is

Next.js is a React meta-framework that provides conventions and infrastructure on top of React: file-based routing, server-side rendering (SSR), static generation (SSG), server components, server actions, image optimization, font optimization, edge runtime support, middleware, API routes, and first-class TypeScript support. You write React; Next.js handles the build, the rendering, the deployment target.

The 2026 baseline is **Next.js 15** (stable Oct 2024), with the **App Router** (the production default since v13) fully matured:

- **React Server Components by default** — every component is a Server Component unless you mark `"use client"`.
- **Server Actions** — async functions called from client components, executed on the server; replace most API routes for mutations.
- **Partial Prerendering (PPR)** — static shell + dynamic holes, deployed behind a flag.
- **`next.config.ts`** — TypeScript config is GA.
- **Turbopack** stable for `next dev` (and beta for `next build`); dramatically faster dev startup.
- **Async Request APIs (cookies(), headers(), params)** — breaking change in v15, simpler mental model.
- **Improved caching defaults** with explicit `cache:` directives and `revalidateTag` for tag-based invalidation.

Routing model:
- **`app/` directory** — App Router (the new default). Layouts, loading UI, error UI, route groups, parallel routes, intercepting routes.
- **`pages/` directory** — Pages Router (legacy, still supported). Old-school getServerSideProps / getStaticProps.
- **Route Handlers** (`app/api/.../route.ts`) — for when you actually need an HTTP endpoint (webhooks, third-party integrations).

Rendering modes:
- **Static (default)** — pre-rendered at build time.
- **Dynamic** — rendered on request (server).
- **Streaming** — server streams chunks via Suspense boundaries.
- **ISR (Incremental Static Regeneration)** — static + on-demand revalidation.

Adoption:
- Next.js is the **#1 React meta-framework** and the most-used way to ship React in production (npm: >6M weekly downloads).
- Used by: Vercel, Notion, Linear, Loom, Stripe (docs site), TikTok (web), Hulu, Twitch, thousands of startups.
- The dominant template for AI apps, SaaS dashboards, and content sites.

## When To Use It

- **You're building a React app for production.** Default choice in 2026.
- **You need SEO** (marketing pages, blogs, docs) — Next.js SSR/SSG is best-in-class.
- **You need a mix of static + dynamic + authenticated content** — Next.js handles all three.
- **You want to deploy to the edge** (Vercel, Cloudflare Workers, Netlify Edge) — first-class support.
- **You want file-based routing + layouts + nested UI** — the App Router is the best-in-class convention.
- **You want Server Components / Server Actions for free** — the dominant React 19+ pattern.
- **You're building a SaaS dashboard, marketing site, docs site, e-commerce, AI app.** All canonical Next.js.

## When NOT To Use It

- **You're building a tiny SPA** with no SEO or server-rendering needs. Vite + React Router is simpler.
- **You're on a non-React stack** (Vue, Svelte, Solid). Use the ecosystem's own meta-framework.
- **You want full control over the bundler / build pipeline.** Vite + custom setup gives more control, less magic.
- **You're deploying to a non-edge / non-Node environment** that Next.js doesn't support (very rare in 2026).
- **Your team is allergic to conventions and wants pure React.** Vite + React + Router is more flexible.
- **You need sub-100KB first-load JS for embedded widgets.** Use Preact + Vite, not Next.js.

## Why It Matters in 2026

Three forces keep Next.js at the top:

1. **Server Components won the React future.** React 19's Server Components + Server Actions are the recommended architecture. Next.js's App Router was the first production-grade implementation. Every React meta-framework competitor (Remix, React Router 7, TanStack Start) has either copied the model or lost ground.
2. **Vercel + Edge is a complete story.** `vercel deploy` from a GitHub push to global edge in 60 seconds. The DX is unmatched. Self-hosting on Cloudflare / AWS / your own infra is also well-supported.
3. **AI app template.** Every "build an AI SaaS" tutorial in 2025–2026 starts with Next.js + Vercel AI SDK + Claude/GPT. The pattern is so dominant it's almost a default.

Practitioner defaults in 2026:
- **App Router** for new projects; Pages Router only for legacy.
- **TypeScript** always.
- **Turbopack** for dev; opt into `next build --turbopack` once it hits GA.
- **Tailwind CSS** (or Vanilla Extract) for styling.
- **React Query / TanStack Query** for client-side data fetching where Server Components don't apply.
- **NextAuth / Auth.js** (or Clerk / Better-Auth) for auth (see `authentication.md`).
- **Drizzle ORM** or **Prisma** for DB access.
- **Vercel** for hosting if you can afford it; Cloudflare / self-host otherwise.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 9+ years old (Vercel, 2016); App Router stable since v13 (2023); v15 (Oct 2024) is the production baseline. |
| Community | 95 | #1 React meta-framework; >6M weekly npm downloads; dominant in tutorials and starter kits. |
| Learning curve | 55 | App Router + Server Components + caching model is a significant mental model; conventions are powerful but must be learned. |
| Performance | 90 | Static + streaming + edge + image optimization + Turbopack = excellent defaults. |
| Cost | 70 | Framework is free; Vercel hosting can get expensive at scale; self-hosting is free but ops-heavy. |
| DX (developer experience) | 95 | File-based routing, Fast Refresh, TypeScript-first, Turbopack, error overlay — best-in-class. |
| Production readiness | 95 | Used at massive scale (TikTok, Notion, Linear, Loom); Vercel hosting is rock-solid. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Remix / React Router 7** | You prefer the loader/action data flow model; you want more explicit data fetching. | You need the largest ecosystem / community. |
| **Vite + React + React Router** | You want full control, minimal magic, smallest bundle. | You need SSR / SSG / RSC / edge deploy built in. |
| **Astro** | You're building mostly static content with selective islands of interactivity. | You're building a heavy SPA / dashboard. |
| **TanStack Start** | You want type-safe server functions and full type safety end-to-end (beta in 2026). | You need ecosystem maturity today. |
| **SvelteKit** | You're on Svelte. | You're on React. |
| **Nuxt** | You're on Vue. | You're on React. |
| **Plain React (no meta-framework)** | You're building an embedded widget or internal tool with no SSR needs. | You're shipping a public web product. |

## Sources

- [Next.js Official Site](https://nextjs.org/) — 2026
- [Next.js Docs](https://nextjs.org/docs) — 2026
- [Next.js Blog](https://nextjs.org/blog) — 2026
- [Next.js GitHub (vercel/next.js)](https://github.com/vercel/next.js) — 2026
- [App Router Docs](https://nextjs.org/docs/app) — 2026
- [Route Handler File Convention](https://nextjs.org/docs/app/api-reference/file-conventions/route) — 2026
- [App Router Routing](https://nextjs.org/docs/app/building-your-application/routing) — 2026
- [App Router Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching) — 2026
- [App Router Caching](https://nextjs.org/docs/app/building-your-application/caching) — 2026
- [Vercel Docs](https://vercel.com/docs) — 2026
- [Deploying Next.js Apps](https://nextjs.org/docs/app/building-your-application/deploying) — 2026
- [Testing Next.js Apps](https://nextjs.org/docs/app/building-your-application/testing) — 2026