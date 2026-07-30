---
name: Databases
slug: databases
source: https://roadmap.sh/postgresql-dba + https://roadmap.sh/mongodb + https://roadmap.sh/redis + https://roadmap.sh/elasticsearch + https://roadmap.sh/sql + https://roadmap.sh/python-data-analysis
last-updated: 2026-07-30
tech-count: 6
status: in-progress
---

# Databases

> **Category:** Specific databases, query languages, and data stores beyond the PostgreSQL / SQL basics covered in `frontend-backend/`. Each entry covers the dominant use case, when to pick it, and the 2026 alternatives.
> **Sources:** [roadmap.sh/postgresql-dba](https://roadmap.sh/postgresql-dba), [roadmap.sh/mongodb](https://roadmap.sh/mongodb), [roadmap.sh/redis](https://roadmap.sh/redis), [roadmap.sh/elasticsearch](https://roadmap.sh/elasticsearch), [roadmap.sh/sql](https://roadmap.sh/sql)

This roadmap covers the data storage layer in depth: document databases, in-memory stores, search engines, column-oriented analytics DBs, SQL deep-dive, and PostgreSQL administration.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | SQL (Deep Dive) | [sql.md](sql.md) | placeholder |
| 2 | MongoDB | [mongodb.md](mongodb.md) | placeholder |
| 3 | Redis | [redis.md](redis.md) | placeholder |
| 4 | Elasticsearch | [elasticsearch.md](elasticsearch.md) | placeholder |
| 5 | ClickHouse | [clickhouse.md](clickhouse.md) | placeholder |
| 6 | PostgreSQL DBA | [postgresql-dba.md](postgresql-dba.md) | placeholder |

---

## Quick Decision Guide

### For relational data

- **Default**: **PostgreSQL** ([`../frontend-backend/postgresql.md`](../frontend-backend/postgresql.md) for basics, [postgresql-dba.md](postgresql-dba.md) for production ops).
- **Master SQL** ([sql.md](sql.md)) — window functions, CTEs, indexing, query plans.

### For specific data shapes

| Need | Pick |
|------|------|
| Document / schemaless / variable schema | [mongodb.md](mongodb.md) — MongoDB + Atlas |
| Cache / sessions / leaderboards / pub-sub / vector search | [redis.md](redis.md) — Redis (or Valkey) |
| Full-text + faceted search / log analytics / SIEM | [elasticsearch.md](elasticsearch.md) — Elasticsearch (or OpenSearch) |
| OLAP at scale / real-time analytics / time-series | [clickhouse.md](clickhouse.md) — ClickHouse |
| Operate Postgres in production | [postgresql-dba.md](postgresql-dba.md) — pgBackRest, Patroni, PgBouncer |

### Decision tree

```
What kind of data?
├── Relational / tabular      → Postgres + SQL
├── Document / variable       → MongoDB
├── Cache / ephemeral        → Redis
├── Search / logs            → Elasticsearch (or OpenSearch)
└── Analytics at scale       → ClickHouse
```

For the same project, you often combine 2–3 of these (e.g. Postgres + Redis + Elasticsearch is a classic).

---

## Cross-references

- For PostgreSQL basics, see [`../frontend-backend/postgresql.md`](../frontend-backend/postgresql.md).
- For vector databases, see [`../ai-ml-llm/vector-databases.md`](../ai-ml-llm/vector-databases.md).
- For analytics workloads, see [`../data-ai/README.md`](../data-ai/README.md).

---

## Build progress

**Phase 9 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.