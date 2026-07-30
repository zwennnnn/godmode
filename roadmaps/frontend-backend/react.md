---
name: React
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://react.dev/
  - https://react.dev/learn
  - https://react.dev/reference/react/hooks
  - https://react.dev/blog/2024/12/05/react-19
  - https://github.com/facebook/react
  - https://github.com/facebook/react/wiki/Versioning-Policy
  - https://survey.stackoverflow.co/2024/technology/
  - https://stateofjs.com/
  - https://nextjs.org/blog
  - https://react.dev/reference/rsc/server-components
  - https://react.dev/reference/rsc/use-client
  - https://www.npmjs.com/package/react
tags: [react, react-19, server-components, hooks, jsx, ui, frontend]
---

# React

## One-liner

Meta's open-source UI library for building component-based, declarative user interfaces — the dominant frontend framework of the 2018–2026 era.

## What It Is

React is a JavaScript/TypeScript library for building UIs out of reusable **components**. Components are functions that take inputs (props) and return a description of UI (JSX — a syntax extension that compiles to JS objects). React then reconciles your component tree against the DOM efficiently using its virtual-DOM diffing algorithm.

The 2026 baseline is **React 19** (stable Dec 2024), which marks the completion of the server-first transition:

- **Server Components** (stable) — components that run only on the server, ship zero JS to the browser, can `await` data directly. The new default for non-interactive UI.
- **Server Actions** (stable) — async functions you call from client components that execute on the server; replace most manual API routes for mutations.
- **`use()` hook** (stable) — read resources (Promises, Context) during render; can be called inside conditionals (unlike other hooks).
- **Actions** + `useActionState` — async transition wrappers with pending/error states.
- **`useFormStatus` / `useOptimistic`** — first-class form + optimistic UI primitives.
- **`<Form>` component** — extends `<form>` with reset + pending state.
- **`ref` as a prop** — `forwardRef` is no longer needed.
- **Document Metadata** — render `<title>`, `<meta>`, `<link>` natively inside components.
- **Async transitions** via `startTransition` (mature).

Concurrent rendering (React 18) is the foundation; React 19 builds automatic batching, transitions, Suspense for data fetching, and Server Components on top.

Adoption (per [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/technology/) and [State of JS](https://stateofjs.com/)):
- React has been the **#1 most-used web framework** in Stack Overflow surveys since 2019.
- ~70%+ of professional web developers used React in 2024.
- The npm `react` package has >25M weekly downloads (most-depended-on frontend library).
- Major users: Meta, Netflix, Airbnb, Stripe, Shopify, Notion, Discord, Reddit, every startup you've heard of.

## When To Use It

- **You're building a SPA, MPA, or hybrid app** with non-trivial UI state. React's component model + ecosystem dominates.
- **You're building with Next.js** (the dominant React meta-framework).
- **You need a huge ecosystem of UI libraries, component kits, dev tools.** React's wins.
- **You need long-term hiring viability.** React devs are the largest pool.
- **You're building anything from dashboards to marketing sites to native mobile (React Native).**
- **You want to share logic between web and mobile** (React + React Native).

## When NOT To Use It

- **Static marketing site with no interactivity.** Plain HTML + a CSS framework is faster, cheaper, SEO-friendly.
- **You hate JSX and the React mental model.** Try Vue or Svelte.
- **You're on an extremely tight bundle budget for embedded / IoT.** Preact or Solid are smaller.
- **You're building native mobile-first.** React Native is mature but adds a layer; consider Swift/Kotlin or Flutter.
- **Your team has zero React experience and 5+ Vue/Svelte experience.** Don't switch for switching's sake.
- **You need server-only rendering with no client JS.** Astro / Solid Start / Qwik are better fits.

## Why It Matters in 2026

Three forces keep React at the top:

1. **The Server Components transition succeeded.** React 19 made RSC + Server Actions stable and ergonomic. Next.js 15's App Router (RSC by default) has been production-stable for 18+ months. The "React is dying for SSR" fear from 2022–2023 didn't materialize — Server Components is now the recommended architecture.
2. **AI-coding amplified React's lead.** Cursor / Copilot / Claude Code all generate React + TSX more reliably than Vue / Svelte / Angular templates. The training data skews React heavily. AI-assisted development is faster in React.
3. **Ecosystem gravity.** Every UI library ships React first; every SaaS dashboard ships a React SDK; every charting / table / form library is React-first.

Practitioner defaults in 2026:
- New apps → **React 19 + TypeScript + Next.js 15** (see `nextjs.md`).
- Existing React 18 apps → migrate incrementally to React 19 + concurrent features.
- **Don't reach for Redux by default.** Start with `useState` + `useReducer` + Server Components. Add Zustand or Jotai if needed.
- Use Server Components by default; mark Client Components explicitly with `"use client"`.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 13+ years old (Meta, 2013); React 19 stable since Dec 2024; battle-tested at every scale. |
| Community | 100 | The single largest frontend community; >25M weekly npm downloads; #1 framework in Stack Overflow surveys. |
| Learning curve | 70 | JSX + hooks + concurrent features have a real learning curve; ecosystem is overwhelming; Server Components add a new mental model. |
| Performance | 85 | Concurrent rendering + automatic batching + Server Components give excellent perf; client-only React is slower than Solid/Qwik for fine-grained updates. |
| Cost | 90 | Library is free; ecosystem is mostly free; learning + maintenance is the real cost. |
| DX (developer experience) | 90 | React DevTools is excellent; Fast Refresh is mature; Storybook, testing-library, Vite all first-class. |
| Production readiness | 95 | Used by every major web product; Server Components in production at Next.js scale (Vercel, Notion, Linear). |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Vue 3** | You prefer template syntax over JSX; you want a more curated, opinionated framework. | You need the largest ecosystem / hiring pool. |
| **Svelte / SvelteKit** | You want compile-time reactivity + minimal runtime; smaller bundles. | You need the ecosystem / component library depth. |
| **Angular** | You're in a large enterprise that wants opinionated, batteries-included framework with TypeScript-first. | You want flexibility / smaller learning curve / smaller bundle. |
| **SolidJS** | You want fine-grained reactivity (no virtual DOM) + React-like JSX. | Ecosystem is much smaller. |
| **Preact** | You need a 3KB React-compatible runtime for embedded / widgets. | You need React 19 features (Server Components etc.). |
| **Qwik** | You want resumability + zero-JS-by-default + best possible TTFB. | Ecosystem and tooling are younger. |
| **Astro / islands architecture** | You're building mostly static content with selective interactivity. | You're building a heavy SPA. |

## Sources

- [React Official Site (react.dev)](https://react.dev/) — 2026
- [React Learn](https://react.dev/learn) — 2026
- [React Hooks Reference](https://react.dev/reference/react/hooks) — 2026
- [React Blog — React 19 (Dec 2024)](https://react.dev/blog/2024/12/05/react-19) — 2024-12
- [React GitHub (facebook/react)](https://github.com/facebook/react) — 2026
- [React Versioning Policy](https://github.com/facebook/react/wiki/Versioning-Policy) — 2026
- [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/technology/) — 2024
- [State of JS](https://stateofjs.com/) — 2024+
- [Next.js Blog](https://nextjs.org/blog) — 2026
- [Server Components Reference](https://react.dev/reference/rsc/server-components) — 2026
- ["use client" Directive](https://react.dev/reference/rsc/use-client) — 2026
- [react on npm](https://www.npmjs.com/package/react) — 2026