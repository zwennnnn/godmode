---
name: Redis
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://redis.io/
  - https://redis.io/docs/
  - https://github.com/redis/redis
  - https://redis.io/docs/latest/develop/
  - https://redis.io/docs/latest/operate/
  - https://redis.io/redis-enterprise/
  - https://redis.io/docs/latest/develop/data-types/
  - https://redis.io/glossary/
  - https://github.com/redis/ioredis
  - https://github.com/redis/node-redis
  - https://redis-py.readthedocs.io/
  - https://github.com/redis/redis-py
  - https://github.com/upstash/upstash-redis
  - https://upstash.com/
  - https://github.com/redis/node-redis
  - https://docs.redisvl.com/
tags: [redis, in-memory, cache, pub-sub, streams, vector-search, sessions, leaderboard, rate-limiting]
---

# Redis

## One-liner

The world's most popular in-memory data store — used as a cache, message broker, session store, leaderboard, rate limiter, pub/sub channel, and now vector database — all in one.

## What It Is

Redis (REmote DIctionary Server) is an in-memory key-value store that supports many data structures: strings, hashes, lists, sets, sorted sets, bitmaps, HyperLogLog, streams, and (new) JSON + vector search. Optional persistence (RDB snapshots, AOF log) lets it survive restarts; replication + clustering for HA.

The 2026 baseline is **Redis 8.x** with:

- **Redis 8** (May 2025) — license change back to AGPLv3 (from SSPL/RSALv2); unified open-source + commercial code.
- **Redis Stack** — adds RedisJSON, RediSearch, RedisGraph, RedisTimeSeries, RedisBloom, RedisVL (vector).
- **Redis 8 Streams** — Kafka-like log abstraction.
- **Redis Functions** — server-side Lua scripting.
- **RedisVL** — vector search client; competes with pgvector / Pinecone.
- **Cluster mode** — sharded across N masters.

### Common patterns

| Pattern | Use case |
|---------|----------|
| **Cache** | Read-through, write-through, write-behind; reduces DB load. |
| **Session store** | Web sessions; OAuth tokens; JWT blacklist. |
| **Rate limiting** | Sliding window / token bucket. |
| **Leaderboard** | Sorted sets (`ZADD`, `ZREVRANGE`). |
| **Pub/Sub** | Real-time notifications; chat; presence. |
| **Streams** | Event log; Kafka-like. |
| **Distributed locks** | `SET NX` + expiry (Redlock). |
| **Task queue** | `LPUSH` / `BRPOP` (basic) or Streams. |
| **Vector search** | RedisVL; embed + `KNN`. |
| **Geo queries** | `GEOADD`, `GEORADIUS`. |
| **Counters** | `INCR`, `INCRBY`. |
| **Bloom filter** | `BF.ADD`, `BF.EXISTS`. |

Adoption: Redis is **ubiquitous** — used by Twitter, GitHub, Stack Overflow, Snap, Pinterest, Craigslist, every modern web app. >100M Docker pulls; the default cache.

## When To Use It

- **Caching anything** — sessions, DB queries, computed values, API responses.
- **Rate limiting** — token bucket, sliding window.
- **Leaderboards / sorted data** — gaming, social feeds.
- **Pub/Sub for real-time** — chat, notifications, presence.
- **Streams for event sourcing / logs** — Kafka-lite.
- **Distributed locks** — Redlock or single-instance `SET NX`.
- **Session storage** — fast ephemeral state.
- **Vector search** — with Redis Stack + RedisVL.
- **Task queue** — simple; for serious throughput use Kafka / SQS.

## When NOT To Use It

- **You need durable storage** — Postgres + S3 are durable; Redis is ephemeral by design.
- **You need complex queries** — no joins; limited query power.
- **Your data set is huge and you don't have RAM** — Redis is in-memory; cost = RAM cost.
- **You need strict consistency across nodes** — Redis is AP (eventually consistent).
- **You're storing large blobs** — use S3 / object storage.

## Why It Matters in 2026

Three forces:

1. **Redis is now a multi-paradigm store.** Cache + queue + leaderboard + pub/sub + vector search + JSON + streams — all in one. Reduces stack complexity.
2. **Redis 8 license restored open source.** After the 2024 SSPL/RSALv2 controversy that forked the community (Linux Foundation Valkey), Redis Inc. returned to AGPLv3 in May 2025. Redis remains the most-popular in-memory store.
3. **Valkey is the open-source fork.** Linux Foundation's Valkey (compatible drop-in) is the fully-open alternative. Same APIs; OSS governance.

Practitioner playbook in 2026:
1. **Cache** — the default pattern; read-through with TTL.
2. **Sessions** — Redis or Upstash Redis (serverless).
3. **Rate limiting** — token bucket via Redis.
4. **Pub/Sub** — for in-process notifications (cross-process = Kafka / NATS).
5. **Vector search** — RedisVL if you want one store for both.
6. **Managed**: **Upstash** (serverless, edge-friendly) or **Redis Cloud** (full Redis).
7. **Open-source alternative**: **Valkey** (Linux Foundation).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 15+ years old (2009); battle-tested at every scale. |
| Community | 100 | Massive; the default in-memory store. |
| Learning curve | 85 | Easy to start; data structures + cluster mode + Redis Stack take study. |
| Performance | 100 | Sub-millisecond p99; the fastest. |
| Cost | 70 | RAM is expensive; Upstash pay-per-request is great for low volume. |
| DX | 90 | Excellent client libraries; redis-cli; RedisInsight. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Memcached** | Pure cache; no persistence. | You need data structures / pub-sub / streams. |
| **Valkey** | Fully open-source; same APIs. | You want commercial Redis features. |
| **Memcached + Postgres** | Pure cache; simple. | You need Redis features. |
| **Hazelcast / Apache Ignite** | Distributed in-memory compute. | You don't need a full grid. |
| **Dragonfly** | Modern Redis-compatible (faster on multi-core). | Ecosystem is younger. |
| **KeyDB** | Redis-compatible fork; multi-threaded. | Niche. |

## Sources

- [Redis](https://redis.io/) — 2026
- [Redis Docs](https://redis.io/docs/) — 2026
- [Redis GitHub (redis/redis)](https://github.com/redis/redis) — 2026
- [Redis Develop Docs](https://redis.io/docs/latest/develop/) — 2026
- [Redis Operate Docs](https://redis.io/docs/latest/operate/) — 2026
- [Redis Enterprise](https://redis.io/redis-enterprise/) — 2026
- [Redis Data Types](https://redis.io/docs/latest/develop/data-types/) — 2026
- [Redis Glossary](https://redis.io/glossary/) — 2026
- [ioredis (GitHub redis/ioredis)](https://github.com/redis/ioredis) — 2026
- [node-redis (GitHub redis/node-redis)](https://github.com/redis/node-redis) — 2026
- [redis-py Docs](https://redis-py.readthedocs.io/) — 2026
- [redis-py GitHub (redis/redis-py)](https://github.com/redis/redis-py) — 2026
- [Upstash Redis (upstash-redis)](https://github.com/upstash/upstash-redis) — 2026
- [Upstash](https://upstash.com/) — 2026
- [RedisVL Docs](https://docs.redisvl.com/) — 2026