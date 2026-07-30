---
name: Software Architecture
category: system-design
status: researched
last-updated: 2026-07-30
sources:
  - https://martinfowler.com/
  - https://martinfowler.com/articles/microservices.html
  - https://martinfowler.com/articles/data-mesh-principles.html
  - https://martinfowler.com/bliki/CQRS.html
  - https://martinfowler.com/eaaCatalog/
  - https://microservices.io/
  - https://microservices.io/patterns/index.html
  - https://12factor.net/
  - https://learn.microsoft.com/en-us/azure/architecture/guide/
  - https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aws-foundations/welcome.html
  - https://cloud.google.com/architecture/framework
  - https://www.thoughtworks.com/radar
  - https://martinfowler.com/articles/dddStart.html
  - https://www.eventstore.com/event-sourcing/
  - https://microservices.io/patterns/data/event-sourcing.html
  - https://martinfowler.com/bliki/PolyglotPersistence.html
tags: [architecture, microservices, monolith, cqrs, event-sourcing, ddd, serverless, hexagonal, clean, event-driven]
---

# Software Architecture

## One-liner

The patterns that shape whole systems — monolith vs microservices, layered vs hexagonal, sync vs event-driven — and how to choose between them as your team and product grow.

## What It Is

Software architecture is the set of decisions that are **hard to change later**: the modularity boundaries, the data ownership, the deployment shape, the communication style between components. Architecture patterns give names to common shapes so teams can communicate and reason about trade-offs.

The 2026 canon of architectural patterns:

### Monolith vs Microservices

| Pattern | Description | When to use |
|---------|-------------|-------------|
| **Modular Monolith** | Single deployable, clear internal module boundaries. | Default for new apps; single team. |
| **Monolith** | Single deployable, no module boundaries. | Throwaway prototypes only. |
| **Microservices** | Many small services, independently deployable. | Multiple teams; need independent scaling per service. |
| **Modular Monolith → Microservices** | Start modular; extract services as needs justify. | Most production apps. |

### Architectural styles

| Style | Description | Best for |
|-------|-------------|----------|
| **Layered (n-tier)** | Presentation / business / data. | Simple CRUD apps. |
| **Hexagonal (Ports & Adapters)** | Domain at center; adapters for UI / DB / external. | Clean separation; testability. |
| **Clean Architecture** | Entities / use cases / interface adapters / frameworks. | Uncle Bob's stricter version of hexagonal. |
| **Event-driven** | Components communicate via events. | Loose coupling; async; audit trails. |
| **CQRS** | Separate read model + write model. | Different read/write load patterns. |
| **Event Sourcing** | State = sequence of events; rebuild by replaying. | Audit / time-travel / complex domain. |
| **Microkernel (plugin)** | Core + plugins. | Apps with pluggable modules. |
| **Serverless / FaaS** | Functions triggered by events. | Event-driven; spiky load. |
| **Space-based** | In-memory data grids; tuple spaces. | Extreme scale. |
| **Orchestration vs Choreography** | Central coordinator vs each-service-knows-its-job. | Distributed workflows. |

### Communication patterns

| Pattern | Description | When |
|---------|-------------|------|
| **Sync (REST / gRPC)** | Request-response. | Simple, immediate consistency needed. |
| **Async (message queue)** | Fire-and-forget. | Decoupling; eventual consistency; spikes. |
| **Event-driven (pub/sub)** | Producers emit events; consumers subscribe. | Fan-out; audit; loose coupling. |
| **Saga** | Distributed transaction via local txs + compensations. | Cross-service transactions. |

### Cross-cutting concerns

| Concern | Patterns |
|---------|----------|
| **Auth** | OAuth2, OIDC, JWT, mTLS, service mesh. |
| **Observability** | Logging, metrics, tracing; OpenTelemetry standard. |
| **Resilience** | Circuit breaker, retries, bulkheads, timeouts, idempotency. |
| **Configuration** | 12-factor; env vars + secret managers. |
| **Deployment** | Blue/green, canary, rolling, feature flags. |
| **Security** | Zero-trust, defense in depth, OWASP. |
| **Data** | Polyglot persistence; CQRS; data mesh; event sourcing. |

### Domain-driven design (DDD)
Eric Evans' classic; key concepts:
- **Bounded context** — a model's boundary.
- **Aggregate** — consistency boundary.
- **Entity** vs **Value Object**.
- **Domain event** — something that happened.
- **Repository**, **Factory**, **Service**.
- **Strategic patterns**: context map, anti-corruption layer, shared kernel.

## When To Use It

### Monolith (modular)
- **Default for new apps** — single team, <100 engineers, greenfield.
- **You want simple deployment** — one binary / container.

### Microservices
- **Multiple teams** that need to ship independently.
- **Different scaling requirements** per service.
- **You have the DevOps maturity** to operate many services.

### Event-driven
- **Loose coupling required** between components.
- **Audit trail** is important (every state change is an event).
- **Async work** is the norm (emails, notifications, analytics).

### CQRS
- **Read load** is very different from write load.
- **Read models** can be denormalized for query speed.
- **Complex domain** with different consistency needs.

### Event Sourcing
- **You need full audit history** (finance, healthcare).
- **You want time-travel debugging**.
- **Domain logic is complex** with many state transitions.

### Hexagonal / Clean
- **You want testable core logic**, decoupled from infrastructure.
- **You expect to swap DBs / UIs** without changing business logic.

### Serverless / FaaS
- **Event-driven; spiky load; sub-second cold start.**

## When NOT To Use It

### Microservices
- **Single team** — modular monolith is simpler.
- **You're at MVP** — premature distribution.
- **You don't have observability** — distributed debugging without tracing is hell.
- **You can't operate the overhead** — microservices add ops cost.

### Event Sourcing
- **Your domain is simple CRUD** — overkill.
- **You need simple queries** — replaying events is slow.
- **You can't model the events** upfront.

### CQRS
- **Read/write load is balanced** — single model is fine.
- **You're a small team** — adds complexity.

### Serverless
- **Long-running processes** (>15 min on Lambda).
- **Heavy compute** (GPU, ML training).
- **Predictable load** — servers are cheaper.

### Hexagonal / Clean
- **Tiny CRUD app** — over-engineering.

## Why It Matters in 2026

Three forces:

1. **AI-assisted coding shifts the value to architecture.** Cursor / Claude Code can write the code; the architecture decisions are what matter. System-level thinking is the differentiator.
2. **Cloud-native made distributed systems default.** Microservices, serverless, event-driven are no longer exotic; they're the assumed shape for new apps.
3. **DDD + CQRS + Event Sourcing matured.** The patterns that were "academic" in 2010 are now standard in event-driven microservices.

Practitioner playbook in 2026:
1. **Default**: **Modular Monolith** with clear bounded contexts.
2. **Extract microservices** only when needed (team size, scaling, deploy independence).
3. **Use event-driven** for cross-cutting concerns (audit, notifications, integrations).
4. **CQRS** when read load ≠ write load; **Event Sourcing** for audit-heavy domains.
5. **Serverless** for event-driven / spiky workloads.
6. **Always**: observability (tracing), resilience patterns (circuit breakers), automated deploy.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | Patterns are decades old; widely taught; battle-tested. |
| Community | 100 | Massive; books (Fowler, Kleppmann, Evans, Vernon) + conferences + blogs. |
| Learning curve | 50 | Many concepts; each is learnable but mastery takes years. |
| Performance | N/A | It's a design discipline. |
| Cost | N/A | Knowledge. |
| DX | N/A | Design work. |
| Production readiness | 100 | Every serious system uses these patterns. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Big ball of mud** | Never intentionally. | Always. |
| **Microservices-first** | Large orgs; clear domains. | Small teams; greenfield. |
| **Serverless-first** | Event-driven; spiky. | Long-running; heavy compute. |
| **No architecture (just hack)** | Throwaway. | Anything in production. |

## Sources

- [Martin Fowler](https://martinfowler.com/) — 2026
- [Martin Fowler — Microservices](https://martinfowler.com/articles/microservices.html) — 2014+
- [Martin Fowler — Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html) — 2026
- [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html) — 2011+
- [Martin Fowler — Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/) — 2002+
- [Microservices.io](https://microservices.io/) — 2026
- [Microservices Patterns](https://microservices.io/patterns/index.html) — 2026
- [12-Factor App](https://12factor.net/) — 2011+
- [Azure Architecture Guide](https://learn.microsoft.com/en-us/azure/architecture/guide/) — 2026
- [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aws-foundations/welcome.html) — 2026
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) — 2026
- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) — 2026
- [Martin Fowler — DDD](https://martinfowler.com/articles/dddStart.html) — 2003+
- [Event Store — Event Sourcing](https://www.eventstore.com/event-sourcing/) — 2026
- [Microservices.io — Event Sourcing Pattern](https://microservices.io/patterns/data/event-sourcing.html) — 2026
- [Martin Fowler — Polyglot Persistence](https://martinfowler.com/bliki/PolyglotPersistence.html) — 2006+