---
name: System Design
category: system-design
status: researched
last-updated: 2026-07-30
sources:
  - https://github.com/donnemartin/system-design-primer
  - https://github.com/karanpratapsingh/system-design
  - https://github.com/checkcheckzz/system-design-interview
  - https://blog.bytebytego.com/
  - https://github.com/ByteByteGoHq/system-design-101
  - https://github.com/system-design-newsletter/system-design-interview
  - https://aws.amazon.com/architecture/
  - https://learn.microsoft.com/en-us/azure/architecture/
  - https://cloud.google.com/architecture
  - https://martinfowler.com/
  - https://martinfowler.com/articles/data-mesh-principles.html
  - https://martinfowler.com/articles/microservices.html
  - https://www.nginx.com/resources/glossary/
  - https://redis.io/docs/
  - https://kafka.apache.org/documentation/
  - https://www.haproxy.org/
tags: [system-design, architecture, distributed-systems, scaling, caching, load-balancing, cap-theorem, sharding, microservices, queue]
---

# System Design

## One-liner

How to design systems that scale, stay available, and handle failure — the practice that separates senior engineers from juniors, and the core skill behind every tech interview at top companies.

## What It Is

System design is the discipline of making architectural decisions for systems that need to handle real-world load, fault tolerance, and growth. It covers:

1. **Requirements** — clarify functional + non-functional (scale, latency, availability, consistency).
2. **Capacity estimation** — back-of-envelope math (QPS, storage, bandwidth).
3. **High-level architecture** — clients, load balancers, app servers, databases, caches, queues.
4. **Data model** — schema, access patterns, indexes.
5. **Component deep-dives** — specific design decisions for each piece.
6. **Scaling strategies** — vertical vs horizontal; sharding; caching; async.
7. **Failure modes** — what happens when each component fails; how do you detect + recover.

The 2026 canon (resources) includes:

| Resource | Notes |
|----------|-------|
| **[System Design Primer (donnemartin)](https://github.com/donnemartin/system-design-primer)** | The classic; covers caching, sharding, CAP, etc. |
| **[System Design (karanpratapsingh)](https://github.com/karanpratapsingh/system-design)** | Modern; well-organized; cheat sheets. |
| **[ByteByteGo System Design 101](https://github.com/ByteByteGoHq/system-design-101)** | Visual; based on Alex Xu's books. |
| **[ByteByteGo Blog](https://blog.bytebytego.com/)** | Authoritative; updated weekly. |
| **[System Design Newsletter](https://github.com/system-design-newsletter/system-design-interview)** | Real-world architectures. |
| **[Designing Data-Intensive Applications (Kleppmann)](https://dataintensive.net/)** | The bible of data systems. |
| **[Martin Fowler](https://martinfowler.com/)** | Patterns of enterprise architecture. |

## Core Concepts

### CAP Theorem (Eric Brewer, 2000)
In a distributed system with network partitions (P — inevitable), you must choose between:
- **CP** — Consistency over Availability. Examples: HBase, MongoDB (default), ZooKeeper.
- **AP** — Availability over Consistency. Examples: Cassandra, DynamoDB, CouchDB.
- **CA** — only works in single-node systems (no partition tolerance). Examples: traditional RDBMS.

In practice: most modern systems are AP (eventual consistency) and offer tunable consistency.

### Consistency models
| Model | Description | Example |
|-------|-------------|---------|
| **Strong** | All reads see the latest write. | RDBMS, Zookeeper |
| **Causal** | Causally-related ops are ordered; concurrent may diverge. | Some NoSQL systems |
| **Read-your-writes** | User sees their own writes immediately. | Most apps |
| **Monotonic reads** | User never sees older data after newer. | Session-based systems |
| **Eventual** | All replicas converge eventually. | DynamoDB, Cassandra |

### Caching strategies
| Strategy | Description | When to use |
|----------|-------------|-------------|
| **Cache-aside (lazy)** | App reads from cache; on miss, reads DB + populates cache. | Default for most apps. |
| **Write-through** | App writes to cache + DB synchronously. | Strong consistency needed. |
| **Write-behind (write-back)** | App writes to cache; cache writes to DB async. | High write throughput. |
| **Refresh-ahead** | Cache refreshes before TTL expiry. | Latency-sensitive reads. |

Cache invalidation: **TTL** (time-to-live), **event-based** (invalidate on write), **versioned keys**.

### Load balancing
| Algorithm | Description |
|-----------|-------------|
| **Round-robin** | Cycle through servers. |
| **Least connections** | Send to server with fewest active connections. |
| **Weighted** | More traffic to more powerful servers. |
| **IP hash** | Same client → same server (session affinity). |
| **Consistent hashing** | Add/remove servers without remapping all keys. |

Layer 4 (TCP) vs Layer 7 (HTTP) — L4 is faster; L7 is smarter (URL routing, header-based).

### Database scaling
- **Vertical** — bigger server. Limits hit fast.
- **Read replicas** — read scaling; eventual consistency.
- **Sharding (horizontal partitioning)** — split data across N DBs.
  - **Range-based** — by date or ID range.
  - **Hash-based** — `hash(user_id) % N`.
  - **Directory-based** — lookup table.
- **Federation** — split by feature (users DB, orders DB).
- **Denormalization** — accept redundancy for query speed.

### Consistency patterns for distributed data
- **Quorum** — write to W of N replicas; read from R of N; W + R > N for strong consistency.
- **Vector clocks** — DynamoDB-style conflict resolution.
- **CRDTs** — conflict-free replicated data types.
- **Two-phase commit (2PC)** — distributed transaction; expensive.
- **Saga pattern** — sequence of local transactions + compensating transactions.

### Message queues
For async work:
- **Kafka** — high-throughput event streaming; durable log.
- **RabbitMQ** — traditional message broker; rich routing.
- **AWS SQS / SNS** — managed.
- **Redis Streams** — lightweight.
- **NATS** — modern, simple, JetStream for persistence.

### Failure handling
- **Circuit breaker** — fail fast when downstream is sick.
- **Retry with exponential backoff + jitter**.
- **Bulkhead** — isolate resources per tenant.
- **Timeout** — every remote call.
- **Idempotency keys** — safe retries.

## When To Use It

- **You're designing any system that needs to scale** — beyond prototype.
- **You're interviewing for senior+ roles** — system design is the differentiator.
- **You're migrating from monolith to distributed** — patterns matter.
- **You're debugging a production incident** — knowing the patterns helps you reason about failure modes.
- **You want to communicate architectural decisions** — system design vocabulary.
- **You're choosing between databases / caches / queues** — the trade-offs are all system design topics.

## When NOT To Use It

- **Tiny prototype** — single-server, single-DB is fine.
- **You're at single-digit QPS** — premature optimization.
- **You don't know the access patterns yet** — over-engineering wastes time.
- **You can use a managed service** (Vercel, Firebase, Supabase, Neon) — system design is built-in.

## Why It Matters in 2026

Three forces:

1. **AI-assisted coding requires system design judgment.** Copilot / Cursor can write the code; you decide the architecture. System design skill is the differentiator.
2. **Distributed systems are now default.** Every "modern" app is distributed (microservices, multi-region, serverless). Knowing the patterns is non-optional.
3. **Interviews still gate careers.** System design is the senior / staff / principal interview filter at every top company.

Practitioner playbook in 2026:
1. **Master the basics** — caching, sharding, CAP, queues, load balancing.
2. **Read real architectures** — High Scalability blog, ByteByteGo, AWS Architecture Blog, Netflix / Uber / Discord engineering blogs.
3. **Build something distributed** — even a simple chat app with Pub/Sub + cache + DB teaches you.
4. **Practice interviews** — System Design Primer, Alex Xu books, Hello Interview, Codemia.
5. **Stay current** — the patterns evolve slowly; new DBs / queues appear.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years of distributed systems research; core patterns are settled. |
| Community | 100 | Massive; every senior engineer writes about it; entire interview industry. |
| Learning curve | 50 | Many concepts; each is learnable but mastery takes years. |
| Performance | N/A | It's a design discipline, not a tool. |
| Cost | N/A | Free knowledge; paid courses optional. |
| DX | N/A | Design work, not implementation. |
| Production readiness | 100 | Every production system uses these patterns. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Just use managed services** | You're not at scale; you want to ship fast. | You need control; you're at scale; cost matters. |
| **Microservices** | Large team; independent deployability. | Small team; monolith is simpler. |
| **Serverless only** | Event-driven; spiky load. | Predictable load; long-running; cost-sensitive. |
| **Single-node / monolith** | Single team; <100 QPS. | Multi-region; >1K QPS. |
| **Blockchain / decentralized** | Trustless consensus. | Performance; most apps don't need it. |

## Sources

- [System Design Primer (donnemartin)](https://github.com/donnemartin/system-design-primer) — 2026
- [System Design (karanpratapsingh)](https://github.com/karanpratapsingh/system-design) — 2026
- [System Design Interview (checkcheckzz)](https://github.com/checkcheckzz/system-design-interview) — 2026
- [ByteByteGo Blog](https://blog.bytebytego.com/) — 2026
- [ByteByteGo System Design 101](https://github.com/ByteByteGoHq/system-design-101) — 2026
- [System Design Newsletter](https://github.com/system-design-newsletter/system-design-interview) — 2026
- [AWS Architecture Center](https://aws.amazon.com/architecture/) — 2026
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) — 2026
- [Google Cloud Architecture](https://cloud.google.com/architecture) — 2026
- [Martin Fowler](https://martinfowler.com/) — 2026
- [Martin Fowler — Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html) — 2026
- [Martin Fowler — Microservices](https://martinfowler.com/articles/microservices.html) — 2014+
- [NGINX Glossary](https://www.nginx.com/resources/glossary/) — 2026
- [Redis Docs](https://redis.io/docs/) — 2026
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/) — 2026
- [HAProxy](https://www.haproxy.org/) — 2026