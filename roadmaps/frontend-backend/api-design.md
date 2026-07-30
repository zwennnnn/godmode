---
name: API Design
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://restfulapi.net/
  - https://swagger.io/specification/
  - https://spec.graphql.org/
  - https://graphql.org/learn/
  - https://trpc.io/
  - https://trpc.io/docs
  - https://docs.grouparoo.com/docs/runbook/operations/api-design
  - https://www.postman.com/api-platform/api-design/
  - https://stoplight.io/api-design-guidelines/
  - https://github.com/OAI/OpenAPI-Specification
  - https://relay.dev/
  - https://www.apollographql.com/
  - https://docs.tigrisdata.com/docs/grpc/
  - https://protobuf.dev/
tags: [api-design, rest, graphql, trpc, grpc, openapi, swagger, postman]
---

# API Design (REST / GraphQL / tRPC / gRPC)

## One-liner

The patterns for how your frontend talks to your backend — the contract that determines whether your product feels fast, consistent, and evolvable.

## What It Is

An API design choice decides the **shape of the contract** between client and server: what endpoints exist, what they accept, what they return, how errors flow, how evolution works. The four dominant paradigms in 2026:

| Paradigm | Style | Best for |
|----------|-------|----------|
| **REST + JSON** | Resources at URLs; HTTP verbs; stateless | CRUD, public APIs, simple client-server, broad compatibility |
| **GraphQL** | Single endpoint; client queries for exactly what it needs | Complex relational data; mobile clients; aggregating multiple sources; evolving schemas |
| **tRPC** | Type-safe RPC with zero schema/code-gen; TS-only | TS monorepos; internal APIs; full-stack Next.js / Remix |
| **gRPC** | Binary protobuf over HTTP/2; strongly typed | Microservice-to-microservice; low-latency; streaming; polyglot services |

### REST
- **Resources** at URLs (`/users/42`), **HTTP verbs** (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), **stateless**.
- **OpenAPI 3.x** (formerly Swagger) is the canonical schema format — generates clients, servers, docs.
- **Pros**: simple, cacheable, well-understood, browser-friendly, HTTP-native.
- **Cons**: over-fetching, under-fetching, version churn (`/v1/`, `/v2/`), N+1 queries for complex screens.

### GraphQL
- **Single endpoint** (`/graphql`); client sends a query describing exactly what fields it needs; server returns JSON of the same shape.
- **Schema-first**: SDL (Schema Definition Language) defines types; resolvers fetch data.
- **Federation / Apollo Federation** — multiple GraphQL services compose into one graph.
- **Relay-style cursor pagination** is the standard for lists.
- **Pros**: no over/under-fetching; single round-trip for complex screens; great DX; evolving schemas via deprecation.
- **Cons**: complex caching (POST not GET); N+1 query problems (mitigated by DataLoader); harder for non-TS backends; steeper ops curve.

### tRPC
- **Type-safe RPC** between TS clients and servers — no schema, no codegen, just TS types.
- **v11** (2024+) added React Query integration, subscriptions, and procedure middleware.
- **Pros**: end-to-end type safety; zero schema maintenance; perfect DX for monorepos.
- **Cons**: TS-only; tight coupling between client + server; not for public APIs; not great for non-TS clients.

### gRPC
- **Protocol Buffers** schema; binary over HTTP/2; strongly typed; streaming support.
- **Pros**: fast, efficient, great for polyglot microservices, streaming.
- **Cons**: not browser-native (needs grpc-web); binary = hard to debug; steeper learning curve.

## When To Use It

### REST
- **Public API** (3rd-party developers).
- **CRUD-heavy, simple client-server**.
- **Browser-only consumers** with no build step.
- **You want HTTP caching** (CDN-friendly).

### GraphQL
- **Complex relational data** (social graphs, content sites, dashboards).
- **Multiple client types** (mobile, web, partner) with different data needs.
- **You want to ship client-first features** without backend round-trips.
- **You have a small team of full-stack TS devs** who can maintain the schema.

### tRPC
- **TS monorepo with Next.js / Remix / SvelteKit**.
- **Internal API** between your own frontend and backend.
- **You want full type safety** with zero schema overhead.
- **You're moving fast** and don't want to maintain OpenAPI / GraphQL schemas.

### gRPC
- **Microservice-to-microservice** in a polyglot environment.
- **Low-latency / high-throughput** internal services.
- **Streaming** (server streaming, client streaming, bidirectional).

## When NOT To Use It

### REST
- **Complex relational data** where over/under-fetching is killing perf — GraphQL or tRPC better.
- **You need end-to-end type safety** without manual schema — tRPC.

### GraphQL
- **Simple CRUD** — REST is simpler, more cacheable.
- **Public API for non-TS clients** — REST/OpenAPI is more accessible.
- **Your team is small and not full-stack TS** — ops cost of GraphQL is real.

### tRPC
- **Public API** — REST/OpenAPI is the standard.
- **Non-TS clients** (mobile native, Python data science).
- **Multiple teams on different stacks** — REST/GraphQL/gRPC decouple better.

### gRPC
- **Browser-first public APIs** — REST/GraphQL.
- **Small projects** — the protobuf + codegen overhead is not worth it.
- **You need easy debugging** — JSON is easier to inspect than protobuf.

## Why It Matters in 2026

Three forces:

1. **Type-safe everything is the new default.** tRPC + Zod / Valibot on the edge; OpenAPI + generated TS clients; GraphQL Code Generator. Manual typing of API contracts is dying.
2. **Server Components changed the calculus.** With React Server Components, you can fetch data on the server and never expose a separate REST/GraphQL API for internal use. tRPC is even more relevant in this world (call your server function directly, get types).
3. **Edge runtimes push for HTTP/REST.** Edge functions (Cloudflare Workers, Vercel Edge, Deno Deploy) are HTTP-first; complex GraphQL servers are harder to deploy at the edge. Hono + REST (or tRPC over fetch) is the edge-native pattern.

Practitioner defaults in 2026:
- **Public API** → REST + OpenAPI.
- **TS monorepo, internal** → tRPC.
- **Complex public data API** → GraphQL (with Federation if multi-service).
- **Internal microservices** → gRPC (or REST if simpler).
- **AI app with mixed consumers** → REST + tRPC hybrid (REST for third-party, tRPC for internal).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | REST: 25+ years. GraphQL: 10+ years. tRPC: 5+ years. gRPC: 10+ years. All battle-tested. |
| Community | 95 | REST/OpenAPI: universal. GraphQL: huge. tRPC: rapidly growing. gRPC: massive in microservices. |
| Learning curve | 70 | REST easy; GraphQL moderate; tRPC easy (if TS); gRPC steeper. |
| Performance | 85 | REST OK (HTTP/2 helps); GraphQL overhead but eliminates over-fetch; tRPC low overhead; gRPC fastest. |
| Cost | 85 | All free; ops cost varies (GraphQL > REST, gRPC > REST for tooling). |
| DX (developer experience) | 90 | OpenAPI tooling excellent; GraphQL tools mature; tRPC best-in-class for TS; gRPC strong for services. |
| Production readiness | 95 | All used at massive scale by every major company. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **WebSockets / Server-Sent Events** | Real-time push (chat, presence, live data). | Request/response APIs. |
| **JSON-RPC / XML-RPC** | Legacy systems. | Greenfield; better options exist. |
| **Falcor / OData** | Niche legacy Microsoft / Netflix stacks. | Almost never the right choice in 2026. |
| **Direct DB access** (e.g. Supabase client-side) | Simple apps with row-level security. | Complex business logic; multi-tenant. |
| **Webhook (push from server to server)** | Server-to-server event delivery. | Synchronous client-server. |

## Sources

- [RESTfulAPI.net](https://restfulapi.net/) — 2026
- [OpenAPI Specification (Swagger)](https://swagger.io/specification/) — 2026
- [GraphQL Spec](https://spec.graphql.org/) — 2026
- [GraphQL Learn](https://graphql.org/learn/) — 2026
- [tRPC](https://trpc.io/) — 2026
- [tRPC Docs](https://trpc.io/docs) — 2026
- [Grouparoo API Design Guide](https://docs.grouparoo.com/docs/runbook/operations/api-design) — 2026
- [Postman API Design](https://www.postman.com/api-platform/api-design/) — 2026
- [Stoplight API Design Guidelines](https://stoplight.io/api-design-guidelines/) — 2026
- [OpenAPI Specification GitHub (OAI/OpenAPI-Specification)](https://github.com/OAI/OpenAPI-Specification) — 2026
- [Relay (GraphQL client)](https://relay.dev/) — 2026
- [Apollo GraphQL](https://www.apollographql.com/) — 2026
- [Tigris — gRPC Docs](https://docs.tigrisdata.com/docs/grpc/) — 2026
- [Protobuf Docs](https://protobuf.dev/) — 2026