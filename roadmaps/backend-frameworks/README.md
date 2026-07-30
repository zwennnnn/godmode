---
name: Backend Frameworks
slug: backend-frameworks
source: https://roadmap.sh/python + https://roadmap.sh/nodejs + https://roadmap.sh/java + https://roadmap.sh/php + https://roadmap.sh/ruby + https://roadmap.sh/aspnet-core + https://roadmap.sh/golang + https://roadmap.sh/scala
last-updated: 2026-07-30
tech-count: 8
status: in-progress
---

# Backend Frameworks

> **Category:** The dominant server-side frameworks for each major language — Python, Node.js, Java, PHP, Ruby, C#, Go, Scala — with deep dives into the choices for each ecosystem in 2026.
> **Sources:** [roadmap.sh/python](https://roadmap.sh/python), [roadmap.sh/nodejs](https://roadmap.sh/nodejs), [roadmap.sh/java](https://roadmap.sh/java), [roadmap.sh/php](https://roadmap.sh/php), [roadmap.sh/ruby](https://roadmap.sh/ruby), [roadmap.sh/aspnet-core](https://roadmap.sh/aspnet-core), [roadmap.sh/golang](https://roadmap.sh/golang), [roadmap.sh/scala](https://roadmap.sh/scala)

This roadmap covers the server-side frameworks you reach for in each major language. Where [`../frontend-backend/nodejs-bun.md`](../frontend-backend/nodejs-bun.md) is about the runtime, this roadmap is about the HTTP / API / full-stack framework on top of it.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Django (Python) | [django.md](django.md) | placeholder |
| 2 | FastAPI (Python) | [fastapi.md](fastapi.md) | placeholder |
| 3 | Express (Node.js) | [express.md](express.md) | placeholder |
| 4 | NestJS (Node.js) | [nestjs.md](nestjs.md) | placeholder |
| 5 | Spring Boot (Java) | [spring-boot.md](spring-boot.md) | placeholder |
| 6 | Laravel (PHP) | [laravel.md](laravel.md) | placeholder |
| 7 | Ruby on Rails (Ruby) | [ruby-on-rails.md](ruby-on-rails.md) | placeholder |
| 8 | ASP.NET Core (C#) | [aspnet-core.md](aspnet-core.md) | placeholder |

---

## Quick Decision Guide

### If you're in Python

- **Full-stack web app with admin / CMS / ORM**: **[Django](django.md)**.
- **Pure API server, async-first, type-safe**: **[FastAPI](fastapi.md)**.

### If you're in Node.js / TypeScript

- **Minimal HTTP server with middleware ecosystem**: **[Express](express.md)**.
- **Opinionated + DI + microservices + GraphQL**: **[NestJS](nestjs.md)**.

### If you're in Java

- **Enterprise backend**: **[Spring Boot](spring-boot.md)** — the default.

### If you're in PHP

- **Web app / API with batteries-included**: **[Laravel](laravel.md)**.

### If you're in Ruby

- **Convention-over-configuration web app**: **[Ruby on Rails](ruby-on-rails.md)** — Rails 8 reasserts the lead.

### If you're in C# / .NET

- **Microsoft shop / cloud-native**: **[ASP.NET Core](aspnet-core.md)** — top of benchmarks.

---

## Cross-references

- For runtimes, see [`../programming-languages/README.md`](../programming-languages/README.md).
- For API design (REST / GraphQL / tRPC / gRPC), see [`../frontend-backend/api-design.md`](../frontend-backend/api-design.md).
- For databases, see [`../databases/README.md`](../databases/README.md).

---

## Build progress

**Phase 13 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.