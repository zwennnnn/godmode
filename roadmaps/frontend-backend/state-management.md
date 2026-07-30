---
name: State Management
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://zustand.docs.pmnd.rs/
  - https://github.com/pmndrs/zustand
  - https://redux-toolkit.js.org/
  - https://redux.js.org/
  - https://github.com/reduxjs/redux-toolkit
  - https://jotai.org/
  - https://github.com/pmndrs/jotai
  - https://valtio.pmnd.rs/
  - https://github.com/pmndrs/valtio
  - https://tanstack.com/query/latest
  - https://github.com/TanStack/query
  - https://react.dev/reference/react/useState
  - https://react.dev/reference/react/useReducer
  - https://swr.vercel.app/
  - https://mobx.js.org/
  - https://legendapp.com/
tags: [state-management, react, zustand, redux, jotai, valtio, tanstack-query, swr, mobx]
---

# State Management (Zustand / Redux Toolkit / Jotai)

## One-liner

How React components share and persist data — local state, server cache, and cross-component state all need different solutions.

## What It Is

"State" in a React app falls into four categories, each with a different best-fit solution:

1. **Local UI state** — form values, toggle, hover. `useState` / `useReducer`.
2. **Server state** — data fetched from APIs that someone else owns (your backend, third-party APIs). **TanStack Query / SWR** (not Redux).
3. **Cross-component client state** — current user, theme, modal open state, selected items. **Zustand / Jotai / Redux Toolkit / Valtio / Context**.
4. **URL state** — current route, search params. **Next.js router / React Router**.

The 2026 leaderboard (per [State of JS](https://stateofjs.com/) and practitioner consensus):

| Tool | Category | Mental model | Bundle |
|------|----------|--------------|--------|
| **[Zustand](https://zustand.docs.pmnd.rs/)** | Cross-component client state | Single store, hook-based | ~3KB |
| **[Redux Toolkit](https://redux-toolkit.js.org/)** | Cross-component client state | Slices + reducers + RTK Query | ~12KB |
| **[Jotai](https://jotai.org/)** | Cross-component client state | Atomic (per-piece-of-state) | ~3KB |
| **[Valtio](https://valtio.pmnd.rs/)** | Cross-component client state | Proxy-based mutable | ~3KB |
| **[TanStack Query](https://tanstack.com/query/latest)** | **Server state** | Cache + invalidation + sync | ~13KB |
| **[SWR](https://swr.vercel.app/)** | Server state | Stale-while-revalidate | ~4KB |
| **Context API + useReducer** | Cross-component client state | React built-in | 0 |
| **[MobX](https://mobx.js.org/)** | Cross-component client state | Observable | ~16KB |

The big 2024–2026 insight: **server state and client state are different problems.** Don't put server data in Redux. Don't put form state in TanStack Query. Most teams that "hate Redux" were using it for the wrong thing.

## When To Use It

### Local state
- **Single component, no sharing** → `useState`.
- **Multiple sub-components from same parent, complex transitions** → `useReducer`.

### Server state (the right tool 80%+ of the time)
- **Anything fetched from an API** → TanStack Query or SWR. Period.
- **You want caching, dedup, background refresh, optimistic updates** → TanStack Query.
- **You're on Next.js / Vercel** → SWR (built by Vercel, integrates perfectly).

### Cross-component client state
- **Small global state (user, theme, sidebar open)** → Zustand or Jotai. Both are excellent.
- **You want the simplest API** → Zustand.
- **You want atomic / derived state** → Jotai.
- **You want proxy-based "just mutate"** → Valtio.
- **You have a large team that benefits from explicit actions + reducers** → Redux Toolkit.
- **You're modernizing a legacy Redux app** → Redux Toolkit (RTK Query replaces much of the old middleware).
- **You want zero deps** → Context API + useReducer (with care — Context has perf caveats).

### URL state
- **Current filters, search, pagination, modal** → Next.js `useSearchParams` / React Router.

## When NOT To Use It

### Zustand / Jotai / Valtio
- **Server data** — use TanStack Query, not Zustand.
- **You need time-travel debugging** — Redux DevTools is still better.

### Redux Toolkit
- **Tiny app with no global state.** Add it when you actually need it.
- **Server data.** Use TanStack Query, not Redux.
- **You're building a fresh app in 2026 and have no team constraint toward Redux.** Zustand or Jotai is simpler.

### TanStack Query
- **Pure client state.** Use Zustand / Jotai.
- **Static data that never changes.** Use `useState` + fetch once.

### Context API
- **High-frequency updates** (per keystroke, per animation frame). Context re-renders all consumers; use Zustand / Jotai.
- **You find yourself memoizing everything** — that's a sign you need a real state library.

### MobX
- **New project in 2026** — the community moved to Zustand / Jotai. MobX is still great but ecosystem is smaller.

## Why It Matters in 2026

Three forces:

1. **The "TanStack Query for everything server-side" consensus is complete.** Redux is no longer recommended for server cache. Every serious React app uses TanStack Query or SWR. The 2024 release of TanStack Query v5 solidified this.
2. **Zustand + Jotai ate Redux's lunch for small-to-medium apps.** Redux still wins for very large teams needing strict action discipline; Zustand / Jotai win everywhere else. The 2024–2026 trend is Zustand's continued dominance.
3. **Server Components reduced the surface area for state management.** With RSC, much "state" is server-derived and never hits the client. Client state is genuinely smaller; the libraries are simpler.

Practitioner defaults in 2026:
- **Default stack**: TanStack Query (server) + Zustand (small global) + `useState` (local).
- **Heavy data + optimistic UI**: TanStack Query v5.
- **Atomic / derived**: Jotai.
- **Legacy / very large team**: Redux Toolkit + RTK Query.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | Redux 10+ years; TanStack Query 8+ years; Zustand / Jotai 4+ years. |
| Community | 95 | All have huge communities; Redux the largest historically; Zustand / TanStack Query the fastest growing. |
| Learning curve | 70 | Zustand: 5 minutes. Jotai: 15 minutes. TanStack Query: 1 hour. Redux Toolkit: 2 hours. |
| Performance | 90 | All fine for normal apps; TanStack Query's caching is the main perf win. |
| Cost | 95 | All free OSS. |
| DX (developer experience) | 90 | Zustand / TanStack Query best; Redux Toolkit much better than old Redux. |
| Production readiness | 95 | All battle-tested at scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Just `useState` everywhere** | Tiny app / prototype. | Multiple components need the same state. |
| **Recoil** | You want Facebook-blessed atomic state. | Project is in maintenance mode (deprecated in favor of Jotai). |
| **Apollo Client / urql** | GraphQL server with cache normalization. | REST API — TanStack Query is simpler. |
| **Legend State / Signals** | You want the fastest possible reactivity (Solid-style). | You're not on Solid / Qwik; React's signals story is still settling. |
| **XState** | You have a real state machine (multi-step forms, wizards, auth flows). | You just have a flag toggle. |

## Sources

- [Zustand Docs](https://zustand.docs.pmnd.rs/) — 2026
- [Zustand GitHub (pmndrs/zustand)](https://github.com/pmndrs/zustand) — 2026
- [Redux Toolkit Docs](https://redux-toolkit.js.org/) — 2026
- [Redux Docs](https://redux.js.org/) — 2026
- [Redux Toolkit GitHub (reduxjs/redux-toolkit)](https://github.com/reduxjs/redux-toolkit) — 2026
- [Jotai](https://jotai.org/) — 2026
- [Jotai GitHub (pmndrs/jotai)](https://github.com/pmndrs/jotai) — 2026
- [Valtio](https://valtio.pmnd.rs/) — 2026
- [Valtio GitHub (pmndrs/valtio)](https://github.com/pmndrs/valtio) — 2026
- [TanStack Query](https://tanstack.com/query/latest) — 2026
- [TanStack Query GitHub (TanStack/query)](https://github.com/TanStack/query) — 2026
- [React useState Reference](https://react.dev/reference/react/useState) — 2026
- [React useReducer Reference](https://react.dev/reference/react/useReducer) — 2026
- [SWR](https://swr.vercel.app/) — 2026
- [MobX](https://mobx.js.org/) — 2026
- [Legend State](https://legendapp.com/) — 2026