---
name: MongoDB
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://www.mongodb.com/
  - https://www.mongodb.com/docs/
  - https://github.com/mongodb/mongo
  - https://www.mongodb.com/docs/atlas/
  - https://www.mongodb.com/docs/manual/
  - https://www.mongodb.com/docs/drivers/
  - https://www.mongodb.com/basics
  - https://www.prisma.io/docs/orm/overview/databases/mongodb
  - https://docs.mongodb.com/manual/aggregation/
  - https://www.mongodb.com/docs/atlas/search/
  - https://www.mongodb.com/docs/atlas/vector-search/
  - https://www.timescale.com/
  - https://github.com/Automattic/mongoose
  - https://mongoosejs.com/
  - https://www.cockroachlabs.com/
  - https://www.couchbase.com/
tags: [mongodb, document-database, nosql, atlas, mongoose, aggregation, vector-search]
---

# MongoDB

## One-liner

The world's most popular document database — JSON-like documents, flexible schema, horizontal scaling, and a managed Atlas service that handles ops for you.

## What It Is

MongoDB stores records as **BSON documents** (binary JSON) grouped into **collections** (analogous to tables). Documents can have different fields — schema is flexible. Indexed; queryable with a rich JSON-based query language; aggregate framework for analytics; ACID transactions since 4.0.

The 2026 baseline is **MongoDB 8.x** with:

- **Atlas** — the managed cloud service (free tier available; the default way to use MongoDB).
- **Atlas Vector Search** — native vector search for AI / RAG.
- **Atlas Search** — full-text + faceted search.
- **Aggregation Framework** — pipelines that look like Unix pipes.
- **Change Streams** — CDC out of MongoDB.
- **Time Series collections** — purpose-built for time-series.
- **Queryable Encryption** — search encrypted data.
- **Aggregation $lookup + $facet** — join-like operations.

### Drivers / ORM

| Tool | Language |
|------|----------|
| **Official drivers** | Node.js, Python, Java, Go, C#, Ruby, PHP, Rust. |
| **Mongoose** | Node.js ODM (most popular). |
| **Prisma** | TS / Node.js ORM. |
| **Motor** | Async Python driver. |
| **Mongoengine** | Python ODM. |

Adoption: MongoDB is the **#1 document database** by usage. Per [DB-Engines](https://db-engines.com/en/ranking/document+store), it's consistently in the top 5 databases overall. Used by Adobe, Google, eBay, Cisco, Sega, Forbes, Toyota, Verizon, ~30K+ customers.

## When To Use It

- **Document data with flexible / evolving schema** — products with varying attributes, content with mixed structure.
- **You don't know the schema upfront** — startup iterating fast.
- **Hierarchical data** — natural JSON representation; no joins needed.
- **Mobile apps + IoT** — flexible schema suits varied device data.
- **AI / RAG** — Atlas Vector Search is built-in.
- **Real-time analytics on operational data** — aggregation framework + change streams.
- **You want managed cloud** — Atlas handles sharding, backups, monitoring.

## When NOT To Use It

- **You need strong ACID transactions across documents** — Postgres is better.
- **You have highly relational data** — joins are awkward in MongoDB.
- **You need ad-hoc SQL queries** — MongoDB's query language is JSON, not SQL.
- **You have fixed-schema + analytics workload** — Postgres + dbt + Snowflake.
- **You're at extreme write scale** — Cassandra / ScyllaDB.

## Why It Matters in 2026

Three forces:

1. **Vector search became built-in.** Atlas Vector Search makes MongoDB a serious RAG backend (alongside Postgres + pgvector). Document DB + vector DB in one.
2. **Managed Atlas is the default.** Most teams use Atlas, not self-hosted. Free tier + auto-scaling.
3. **Flexible schema matches modern apps.** Microservices, mobile apps, AI features all have variable data shapes.

Practitioner playbook in 2026:
1. **Use Atlas** — free tier is generous; ops handled.
2. **Schema design** — embed vs reference decision (most data should be embedded).
3. **Indexes** — critical for performance; understand B-tree vs multikey vs text.
4. **Aggregation framework** — for analytics.
5. **Vector Search** — for AI / RAG.
6. **Change streams** — for CDC + real-time.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 15+ years old (2009); battle-tested at scale. |
| Community | 95 | Massive; the default document DB. |
| Learning curve | 80 | Easy to start; aggregation framework + indexing take study. |
| Performance | 85 | Indexed queries fast; joins slow; write throughput excellent. |
| Cost | 80 | Atlas reasonable; self-host is fine for ops teams. |
| DX | 90 | Mongoose / drivers are excellent; Atlas UI great. |
| Production readiness | 95 | Used at every scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **PostgreSQL (JSONB)** | You want SQL + transactions + joins. | Document-first workflow. |
| **Couchbase** | You need mobile sync + offline-first. | Pure document store. |
| **DynamoDB** | AWS-native; extreme scale; single-region. | Multi-region; complex queries. |
| **Cassandra** | Multi-region write scale; time-series. | You need transactions. |
| **Firebase Firestore** | Mobile-first; realtime. | Server-side complex queries. |

## Sources

- [MongoDB](https://www.mongodb.com/) — 2026
- [MongoDB Docs](https://www.mongodb.com/docs/) — 2026
- [MongoDB GitHub (mongodb/mongo)](https://github.com/mongodb/mongo) — 2026
- [MongoDB Atlas](https://www.mongodb.com/docs/atlas/) — 2026
- [MongoDB Manual](https://www.mongodb.com/docs/manual/) — 2026
- [MongoDB Drivers](https://www.mongodb.com/docs/drivers/) — 2026
- [MongoDB Basics](https://www.mongodb.com/basics) — 2026
- [Prisma MongoDB](https://www.prisma.io/docs/orm/overview/databases/mongodb) — 2026
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/) — 2026
- [Atlas Search](https://www.mongodb.com/docs/atlas/search/) — 2026
- [Atlas Vector Search](https://www.mongodb.com/docs/atlas/vector-search/) — 2026
- [Timescale](https://www.timescale.com/) — 2026
- [Mongoose (Automattic)](https://github.com/Automattic/mongoose) — 2026
- [Mongoose](https://mongoosejs.com/) — 2026
- [CockroachDB](https://www.cockroachlabs.com/) — 2026
- [Couchbase](https://www.couchbase.com/) — 2026