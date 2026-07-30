---
name: PostgreSQL
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://www.postgresql.org/docs/
  - https://www.postgresql.org/about/
  - https://www.postgresql.org/docs/17/release-17.html
  - https://github.com/postgres/postgres
  - https://pganalyze.com/webinars/hands-on-postgres-17
  - https://medium.com/@CodingWithAbhi/postgresql-17-performance-upgrade-2026-f4222e71f577
  - https://devstarsj.github.io/database/postgresql/backend/2026/03/16/postgresql17-features-you-should-use-2026/
  - https://www.postgresql.fastware.com/blog/postgresql-17-and-trends-and-innovations-to-watch
  - https://www.instaclustr.com/education/postgresql/best-managed-postgresql-solutions-top-5-in-2026/
  - https://wiki.postgresql.org/wiki/Performance_Optimization
  - https://github.com/electric-sql/pglite
  - https://supabase.com/docs
  - https://neon.tech/
  - https://www.prisma.io/
  - https://orm.drizzle.team/
tags: [postgresql, sql, database, orm, prisma, drizzle, supabase, neon, pgvector]
---

# PostgreSQL

## One-liner

The world's most advanced open-source relational database — the default OLTP choice for serious web apps in 2026, with vector search, JSONB, and a 35-year extension track record.

## What It Is

PostgreSQL (often "Postgres") is an open-source object-relational database system with 35+ years of active development. It runs SQL (the standard relational query language) with deep extensions: JSONB for document-style data, full-text search, geospatial (PostGIS), time-series, vector search (pgvector), and a programmable extension system that lets the community add capabilities without forking.

The 2026 baseline is **PostgreSQL 17** (released Sept 2024) and **PG 18** (in beta in 2026). Key v17 features (per [PG 17 release notes](https://www.postgresql.org/docs/17/release-17.html), [pgAnalyze webinar](https://pganalyze.com/webinars/hands-on-postgres-17), [PG17 features article](https://devstarsj.github.io/database/postgresql/backend/2026/03/16/postgresql17-features-you-should-use-2026/)):

- **Streaming I/O** with `io_combine_limit` — async reads for sequential scans and ANALYZE; big win for large tables.
- **Faster B-tree scans** — improvements to bulk-read performance.
- **Adaptive VACUUM** — better autovacuum tuning; less manual intervention.
- **Incremental sorting** — "free performance" for many queries.
- **Improved logical replication** — failover slots, better upgrade paths.
- **`JSON_TABLE`** for SQL/JSON path queries.

PostgreSQL ecosystem in 2026:

| Extension / Project | What it adds |
|---------------------|--------------|
| **pgvector** | Vector similarity search inside Postgres — same DB for relational + embeddings. |
| **PostGIS** | Geospatial data types + queries. |
| **pg_trgm / fuzzystrmatch** | Fuzzy text search. |
| **pg_stat_statements** | Query performance monitoring. |
| **Citus / Hydra** | Distributed Postgres for horizontal scale. |
| **TimescaleDB** | Time-series extension. |
| **Postgres + pg_cron** | Scheduled jobs inside the DB. |
| **pglite** ([electric-sql/pglite](https://github.com/electric-sql/pglite)) | Postgres compiled to WASM — runs in browser, edge, or Node with zero install. |
| **Supabase** ([supabase.com](https://supabase.com/docs)) | Managed Postgres + auth + realtime + storage + edge functions. |
| **Neon** ([neon.tech](https://neon.tech/)) | Serverless Postgres with branching, scale-to-zero, instant restore. |
| **Drizzle ORM** ([orm.drizzle.team](https://orm.drizzle.team/)) / **Prisma** ([prisma.io](https://www.prisma.io/)) | TS-first ORMs for Postgres. |

Adoption (per Stack Overflow surveys + DB-Engines ranking):
- PostgreSQL is the **#1 most-loved database** in Stack Overflow surveys since 2018+.
- It overtook MySQL in DB-Engines ranking in 2023 and continues to grow.
- Major users: Apple, Instagram, Spotify, Reddit, GitHub, Notion, Stripe, Figma, every serious SaaS startup.

## When To Use It

- **Default relational database for any web app.** Postgres is the safe, capable, extensible choice.
- **You need JSON / document storage alongside relational.** JSONB is excellent.
- **You need full-text search** without a separate Elasticsearch.
- **You need geospatial** — PostGIS is best-in-class.
- **You need vector search** alongside relational — pgvector kills the "two databases" pattern.
- **You need strong consistency + ACID transactions** — Postgres is rock-solid.
- **You want a single database that grows with you** — single-node → Citus → managed Neon / Supabase / RDS.

## When NOT To Use It

- **You need extreme write throughput at massive scale** — Cassandra, ScyllaDB, ClickHouse (for analytics) may fit better.
- **You need OLAP at petabyte scale** — ClickHouse, Snowflake, BigQuery are purpose-built.
- **You need a simple key-value store** — Redis, DynamoDB are simpler.
- **You're on SQLite and your data fits in one file** — SQLite is faster for single-user / embedded.
- **Your team has zero SQL experience and you're building a tiny project** — Firestore / MongoDB might be easier.

## Why It Matters in 2026

Three forces:

1. **The "one database" story won.** pgvector + JSONB + full-text + PostGIS mean most apps don't need a separate vector DB, document store, or search engine. The pattern: Postgres for everything, add Redis if you need caching.
2. **Serverless Postgres matured.** Neon, Supabase, and the new wave of branching/auto-scaling Postgres providers changed the dev experience. You can spin up a Postgres in 5 seconds; branch it like Git; scale to zero.
3. **WASM Postgres (pglite) opened new surfaces.** Postgres-in-the-browser for local-first apps, in-browser analytics, embedded testing — all real in 2026.

Practitioner defaults in 2026:
- **Greenfield app** → **Neon** or **Supabase** (managed) + **Drizzle ORM** (TS-first) or Prisma.
- **Self-hosted** → Postgres 17 + pgvector + PostGIS as needed.
- **Schema migrations** → Drizzle Kit, Prisma Migrate, or Atlas.
- **Connection pooling** → PgBouncer for high-concurrency; built-in poolers in Neon / Supabase.
- **Monitoring** → pg_stat_statements + pganalyze / pgwatch / Datadog.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 35+ years old; the most mature OSS database. |
| Community | 100 | #1 most-loved DB in Stack Overflow surveys; massive ecosystem; PGConf global. |
| Learning curve | 65 | SQL basics easy; advanced features (window functions, CTEs, EXPLAIN ANALYZE, JSONB operators) take time. |
| Performance | 95 | Excellent for OLTP; v17 streaming I/O is another big leap; rivals commercial DBs. |
| Cost | 95 | OSS free; managed starts cheap (Neon free tier, Supabase free tier); enterprise options available. |
| DX (developer experience) | 90 | psql is great; pgcli is better; GUI tools (TablePlus, DBeaver, pgAdmin) excellent; ORM story mature. |
| Production readiness | 100 | Battle-tested at every scale; the default for serious SaaS. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **MySQL / MariaDB** | You have a legacy MySQL investment; your team knows MySQL better. | You need advanced features (JSONB, pgvector, PostGIS). |
| **SQLite** | Single-user / embedded / mobile / local-first; smaller than ~100GB. | Multi-writer, high-concurrency, network-accessed. |
| **MongoDB** | Truly schemaless documents; you genuinely don't know the schema. | You want strong consistency + relational joins. |
| **DynamoDB** | Extreme scale + single-region AWS; serverless. | You need queries beyond key-value / GSI patterns. |
| **ClickHouse** | OLAP / analytics at petabyte scale. | OLTP / row-level reads. |
| **Cassandra / ScyllaDB** | Massive write throughput; multi-region active-active. | You need strong consistency or complex queries. |
| **CockroachDB** | Global distributed SQL with strong consistency. | Single-region OLTP — overkill. |

## Sources

- [PostgreSQL Official Docs](https://www.postgresql.org/docs/) — 2026
- [PostgreSQL About](https://www.postgresql.org/about/) — 2026
- [PostgreSQL 17 Release Notes](https://www.postgresql.org/docs/17/release-17.html) — 2024
- [PostgreSQL GitHub (postgres/postgres)](https://github.com/postgres/postgres) — 2026
- [pgAnalyze — Hands on Postgres 17](https://pganalyze.com/webinars/hands-on-postgres-17) — 2024
- [Medium — PostgreSQL 17 Performance Upgrade 2026](https://medium.com/@CodingWithAbhi/postgresql-17-performance-upgrade-2026-f4222e71f577) — 2026
- [DevStarsJ — PostgreSQL 17 Features You Should Actually Be Using](https://devstarsj.github.io/database/postgresql/backend/2026/03/16/postgresql17-features-you-should-use-2026/) — 2026-03
- [PostgreSQL.fastware — Coming up in Postgres 17](https://www.postgresql.fastware.com/blog/postgresql-17-and-trends-and-innovations-to-watch) — 2024-09
- [Instaclustr — Best Managed PostgreSQL Solutions 2026](https://www.instaclustr.com/education/postgresql/best-managed-postgresql-solutions-top-5-in-2026/) — 2026
- [PostgreSQL Wiki — Performance Optimization](https://wiki.postgresql.org/wiki/Performance_Optimization) — 2026
- [pglite (electric-sql/pglite)](https://github.com/electric-sql/pglite) — 2026
- [Supabase Docs](https://supabase.com/docs) — 2026
- [Neon](https://neon.tech/) — 2026
- [Prisma](https://www.prisma.io/) — 2026
- [Drizzle ORM](https://orm.drizzle.team/) — 2026