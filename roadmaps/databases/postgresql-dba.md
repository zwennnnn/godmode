---
name: PostgreSQL DBA
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://www.postgresql.org/docs/
  - https://www.postgresql.org/docs/17/release-17.html
  - https://www.postgresql.org/docs/current/runtime-config.html
  - https://wiki.postgresql.org/wiki/Performance_Optimization
  - https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server
  - https://www.postgresql.org/docs/current/wal.html
  - https://www.postgresql.org/docs/current/replication.html
  - https://www.postgresql.org/docs/current/backup.html
  - https://www.postgresql.org/docs/current/pgstatstatements.html
  - https://www.postgresql.org/docs/current/using-explain.html
  - https://github.com/PostgREST/postgrest
  - https://github.com/supabase/supabase
  - https://www.pgbouncer.org/
  - https://github.com/pgbouncer/pgbouncer
  - https://github.com/CrunchyData/postgres-operator
  - https://github.com/zalando/spilo
  - https://github.com/pgbackrest/pgbackrest
  - https://pgbackrest.org/
  - https://github.com/patroni/patroni
tags: [postgresql, dba, replication, backup, performance-tuning, monitoring, wal, vacuum, partitioning, connection-pooling]
---

# PostgreSQL DBA

## One-liner

Operating PostgreSQL in production — replication, backups, performance tuning, monitoring, vacuum, connection pooling, partitioning, and the day-2 operations that keep Postgres healthy at scale.

## What It Is

PostgreSQL DBA is the practice of running Postgres reliably in production. Postgres has the most operational depth of any open-source RDBMS, and "default Postgres" is rarely enough for production at scale. This entry covers the day-2 concerns.

The 2026 baseline (PostgreSQL 17+) ops areas:

| Area | Topic |
|------|-------|
| **Replication** | Streaming (async/sync), logical, physical; HA setups (Patroni). |
| **Backups** | pg_dump, pg_basebackup, pgBackRest, Barman, WAL archiving, PITR. |
| **Performance tuning** | `shared_buffers`, `work_mem`, `effective_cache_size`, `maintenance_work_mem`, `wal_*` settings. |
| **Vacuum + Autovacuum** | Dead tuples; bloat; transaction ID wraparound. |
| **Indexing** | B-tree, Hash, GIN, GiST, BRIN, partial, expression, covering. |
| **Query analysis** | `EXPLAIN ANALYZE`, `EXPLAIN (ANALYZE, BUFFERS)`, pg_stat_statements. |
| **Monitoring** | pg_stat_statements, pg_stat_activity, pg_locks; Datadog / pgwatch / pganalyze. |
| **Connection pooling** | PgBouncer, pgcat, Odyssey. |
| **Security** | RBAC, row-level security, pgaudit, SSL. |
| **Partitioning** | Native (PG 10+), declarative partitioning, partition pruning. |
| **Extensions** | pg_stat_statements, pgcrypto, PostGIS, pgvector, pg_trgm. |
| **HA / Failover** | Patroni + etcd/Consul; pg_auto_failover; cloud-managed (RDS, Aurora, Cloud SQL, Neon). |
| **Migration tools** | pg_dump, pgloader, pgcopydb, Bucardo, logical replication. |
| **Observability** | pg_stat_statements, auto_explain, log_min_duration_statement. |
| **Logical replication** | For selective table sync, zero-downtime migrations. |

### Critical configurations

| Setting | Default | Recommended (typical) |
|---------|---------|----------------------|
| `shared_buffers` | ~128MB | 25% of system RAM |
| `effective_cache_size` | ~4GB | 70–75% of RAM |
| `work_mem` | 4MB | Per-query sort/hash; tune by workload |
| `maintenance_work_mem` | 64MB | 1–2GB for vacuum / index creation |
| `wal_buffers` | -1 (auto) | 16MB |
| `max_connections` | 100 | 100–200 + PgBouncer |
| `checkpoint_completion_target` | 0.5 | 0.9 |
| `random_page_cost` | 4.0 | 1.1 (for SSD) |

### Top tools (2026)

| Tool | Purpose |
|------|---------|
| **pgBackRest** | Best-in-class backup + WAL archiving + PITR. |
| **Patroni** | HA / failover; etcd/Consul-backed. |
| **PgBouncer** | Connection pooling. |
| **pg_stat_statements** | Query stats (built-in). |
| **pgwatch2 / pganalyze / Datadog** | Monitoring. |
| **Postgres Operator (Crunchy / Zalando)** | K8s operator. |
| **pgAudit** | Audit logging. |
| **Barman** | Backup manager. |

Adoption: PostgreSQL is the **#1 most-loved database** in Stack Overflow surveys; every production system has a Postgres DBA story. AWS RDS / Aurora, Google Cloud SQL, Azure Database for Postgres, Neon, Supabase all wrap it.

## When To Use It

- **You're running Postgres in production** — period.
- **You need replication + HA** — Patroni + etcd.
- **You need backups + PITR** — pgBackRest.
- **You have slow queries** — `EXPLAIN ANALYZE` + index review.
- **You have bloat issues** — vacuum tuning.
- **You have connection storms** — PgBouncer.
- **You're scaling to multi-TB** — partitioning + connection pooling + monitoring.

## When NOT To Use It

- **You don't run Postgres** — not applicable.
- **Tiny hobby project** — managed service (Neon, Supabase) handles it.
- **You don't care about ops** — use a managed service.
- **You want zero ops** — RDS / Neon / Supabase.

## Why It Matters in 2026

Three forces:

1. **PostgreSQL is the default production database.** More apps run on PG than any other. Mastering DBA skills = mastering production reliability.
2. **Self-hosting PG is real.** Cost-conscious teams run their own PG; managed is expensive at scale. DBA skills pay off.
3. **Open-source extensions matured.** pgvector for AI, PostGIS for geo, pg_trgm for fuzzy search, pgcrypto — the extension ecosystem is best-in-class.

Practitioner playbook in 2026:
1. **Backups**: pgBackRest with WAL archiving + PITR.
2. **HA**: Patroni + etcd for self-host; or managed (RDS Multi-AZ, Aurora, Neon).
3. **Connection pooling**: PgBouncer.
4. **Monitoring**: pg_stat_statements + pgwatch2 or pganalyze or Datadog.
5. **Tuning**: start with `shared_buffers = 25% RAM`, `effective_cache_size = 70% RAM`, tune from there based on `EXPLAIN ANALYZE`.
6. **Vacuum**: tune autovacuum per workload; watch for wraparound.

## Scoring Matrix (0–100)

### PostgreSQL (the DB)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 35+ years old; the standard. |
| Community | 100 | Massive. |
| Learning curve | 70 | SQL easy; tuning + replication + vacuum take study. |
| Performance | 95 | Excellent; tuning gets you 10× speedups. |
| Cost | 95 | Free; managed tier reasonable. |
| DX | 85 | psql + pgcli; mature tooling. |
| Production readiness | 100 | Battle-tested. |

### pgBackRest / Patroni / PgBouncer
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | All 5+ years; battle-tested. |
| Community | 90 | Strong; core PG ecosystem. |
| Learning curve | 60 | pgBackRest config + Patroni consensus take study. |
| Performance | 95 | Industry standard. |
| Cost | 95 | Free; managed alternatives exist. |
| DX | 80 | Excellent for what they do. |
| Production readiness | 100 | Production everywhere. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Managed PG (RDS / Cloud SQL / Neon)** | Zero ops; cost is OK. | Cost-sensitive; you have ops capacity. |
| **MySQL / MariaDB** | You have a MySQL team. | You need extensions / modern SQL. |
| **CockroachDB** | Multi-region distributed SQL. | Single-region; cost-sensitive. |
| **YugabyteDB** | Distributed SQL; PG-compatible. | Single-region. |

## Sources

- [PostgreSQL Docs](https://www.postgresql.org/docs/) — 2026
- [PostgreSQL 17 Release Notes](https://www.postgresql.org/docs/17/release-17.html) — 2024
- [PostgreSQL Runtime Config](https://www.postgresql.org/docs/current/runtime-config.html) — 2026
- [PostgreSQL Wiki — Performance Optimization](https://wiki.postgresql.org/wiki/Performance_Optimization) — 2026
- [PostgreSQL Wiki — Tuning Your PostgreSQL Server](https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server) — 2026
- [WAL Documentation](https://www.postgresql.org/docs/current/wal.html) — 2026
- [Replication Documentation](https://www.postgresql.org/docs/current/replication.html) — 2026
- [Backup Documentation](https://www.postgresql.org/docs/current/backup.html) — 2026
- [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) — 2026
- [EXPLAIN Docs](https://www.postgresql.org/docs/current/using-explain.html) — 2026
- [PostgREST GitHub (PostgREST/postgrest)](https://github.com/PostgREST/postgrest) — 2026
- [Supabase GitHub (supabase/supabase)](https://github.com/supabase/supabase) — 2026
- [PgBouncer](https://www.pgbouncer.org/) — 2026
- [PgBouncer GitHub (pgbouncer/pgbouncer)](https://github.com/pgbouncer/pgbouncer) — 2026
- [Crunchy Postgres Operator](https://github.com/CrunchyData/postgres-operator) — 2026
- [Zalando Spilo](https://github.com/zalando/spilo) — 2026
- [pgBackRest GitHub (pgbackrest/pgbackrest)](https://github.com/pgbackrest/pgbackrest) — 2026
- [pgBackRest](https://pgbackrest.org/) — 2026
- [Patroni GitHub (patroni/patroni)](https://github.com/patroni/patroni) — 2026