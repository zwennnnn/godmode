---
name: Observability
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://opentelemetry.io/
  - https://opentelemetry.io/docs/
  - https://prometheus.io/
  - https://prometheus.io/docs/
  - https://grafana.com/
  - https://grafana.com/docs/
  - https://grafana.com/oss/mimir/
  - https://grafana.com/oss/loki/
  - https://grafana.com/oss/tempo/
  - https://www.datadoghq.com/
  - https://docs.datadoghq.com/
  - https://www.elastic.co/observability
  - https://opentelemetry.io/blog/2025/state-of-opentelemetry/
  - https://clickhouse.com/resources/engineering/best-open-source-observability-solutions
  - https://www.jaegertracing.io/
  - https://www.elastic.co/
  - https://newrelic.com/
  - https://www.honeycomb.io/
  - https://www.dynatrace.com/
tags: [observability, opentelemetry, prometheus, grafana, datadog, loki, tempo, mimir, jaeger, tracing, metrics, logs]
---

# Observability (OpenTelemetry / Prometheus / Grafana)

## One-liner

The tools and practices that let you understand what's happening inside your running system — metrics, logs, traces, and the queries that turn them into answers.

## What It Is

Observability is the ability to ask arbitrary questions about your system's state from its outputs. The three pillars:

1. **Metrics** — numeric time-series (CPU%, request rate, p99 latency). Cheap to store; great for dashboards and alerts.
2. **Logs** — discrete events with structured or unstructured payloads. Expensive at scale; great for forensics.
3. **Traces** — request flows across services. Show where time is spent in a distributed request.

The 2026 stack (per [ClickHouse 2026 guide](https://clickhouse.com/resources/engineering/best-open-source-observability-solutions), [Metoro 2026 comparison](https://metoro.io/blog/best-observability-tools), and practitioner consensus):

### Open-source LGTM stack + OpenTelemetry

| Component | Purpose | Notes |
|-----------|---------|-------|
| **[OpenTelemetry (OTel)](https://opentelemetry.io/)** | Instrumentation standard | Vendor-neutral SDK + collector; the lingua franca for traces, metrics, logs. |
| **[Prometheus](https://prometheus.io/)** | Metrics storage + query | Pull-based scraping; PromQL; the de-facto metrics standard. |
| **[Grafana Mimir](https://grafana.com/oss/mimir/)** | Prometheus at scale | Horizontally scalable; replaces Prometheus for >10M series. |
| **[Grafana Loki](https://grafana.com/oss/loki/)** | Log aggregation | Like Prometheus but for logs; cheap. |
| **[Grafana Tempo](https://grafana.com/oss/tempo/)** | Distributed tracing | Object-store backed; cheap at scale. |
| **[Grafana](https://grafana.com/)** | Visualization + alerting | One UI for metrics + logs + traces. |
| **[Jaeger](https://www.jaegertracing.io/)** | Distributed tracing (alternative) | CNCF graduated; older but still common. |

### Managed SaaS alternatives

| Platform | Notes |
|----------|-------|
| **[Datadog](https://www.datadoghq.com/)** | The 800-lb gorilla; metrics + logs + traces + RUM + synthetics + APM + security; expensive but best-in-class DX. |
| **[New Relic](https://newrelic.com/)** | APM pioneer; now full-stack observability; pricing model improved. |
| **[Elastic Observability](https://www.elastic.co/observability)** | Built on Elasticsearch; great for log-heavy workloads. |
| **[Dynatrace](https://www.dynatrace.com/)** | Enterprise; AI-assisted root cause; expensive. |
| **[Honeycomb](https://www.honeycomb.io/)** | Tracing-first; high-cardinality; beloved by SREs. |
| **[Grafana Cloud](https://grafana.com/)** | Managed LGTM; OSS-friendly; great price/performance. |
| **[OpenObserve](https://openobserve.ai/)** | Self-hosted-friendly OSS alternative to Datadog. |

OpenTelemetry (OTel) is the critical piece in 2026: **vendor-neutral instrumentation**. You instrument your code once with the OTel SDK; then ship to Prometheus, Datadog, Honeycomb, Tempo — anyone. Lock-in is dead.

## When To Use It

### LGTM + OpenTelemetry (self-hosted)
- **Default for any K8s / cloud-native deployment.**
- **You want OSS + no per-host fees.**
- **You have ops capacity** to run Prometheus + Grafana.

### Grafana Cloud
- **You want managed LGTM** without running it yourself.
- **You're OSS-friendly** and don't want Datadog pricing.

### Datadog
- **You want best-in-class DX + everything in one place** (APM + logs + RUM + synthetics + security).
- **Budget allows** (Datadog is the most expensive option at scale).
- **Enterprise** that wants vendor consolidation.

### New Relic
- **APM-first**; you want strong APM + decent everything else.

### Honeycomb
- **Tracing-first**; high-cardinality debugging; you want to slice data any way.

### Elastic
- **Log-heavy workloads** (security, compliance, audit trails).

## When NOT To Use It

### LGTM self-hosted
- **You don't have ops capacity** — managed is cheaper than an SRE.
- **You need SaaS features** (RUM, synthetics, APM).

### Datadog
- **Cost-sensitive** — Datadog bills per host, per GB ingested, per indexed span. At scale it gets painful.
- **You don't use all features** — many teams pay for Datadog and only use 20% of it.

### Honeycomb
- **You're not tracing-first** — Honeycomb's strength is high-cardinality traces.

### Elastic
- **You don't have a log-heavy workload** — ELK is overkill for metrics-only setups.

## Why It Matters in 2026

Three forces:

1. **OpenTelemetry became the standard instrumentation layer.** Vendor lock-in on instrumentation is essentially over. Every major backend (Datadog, Honeycomb, Grafana, Tempo, Jaeger) accepts OTLP.
2. **LGTM stack ate the metrics+logs+traces market for OSS.** Prometheus + Loki + Tempo + Grafana + Mimir is the default K8s stack in 2026.
3. **AI-assisted observability matured.** Datadog Bits AI, Dynatrace Davis, Honeycomb Query Assistant — natural-language queries against telemetry are real.

Practitioner defaults in 2026:
- **K8s / cloud-native**: LGTM + OTel, self-hosted or Grafana Cloud.
- **Enterprise / budget**: Datadog or New Relic.
- **Tracing-first**: Honeycomb.
- **Log-heavy / security**: Elastic.
- **Multi-cloud hybrid**: Datadog or Grafana Cloud.

## Scoring Matrix (0–100)

### LGTM Stack + OpenTelemetry
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | Prometheus 11+ years; Grafana 10+ years; OTel CNCF graduated 2024. |
| Community | 100 | The de-facto OSS stack. |
| Learning curve | 65 | PromQL takes practice; OTel SDKs easy; Loki/Tempo have their own query langs. |
| Performance | 90 | Excellent at scale with Mimir; Tempo's object-store backend is cheap. |
| Cost | 90 | OSS free; you pay for storage and compute. |
| DX | 80 | Grafana UI is excellent; PromQL is the rough edge. |
| Production readiness | 95 | Used at every cloud-native company. |

### Datadog
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 10+ years; the SaaS observability leader. |
| Community | 90 | Large; excellent docs; many integrations. |
| Learning curve | 75 | Easy to start; advanced features (notebooks, workflows) take study. |
| Performance | 95 | Best-in-class SaaS observability. |
| Cost | 40 | Expensive at scale; pay-per-host + per-GB. |
| DX | 95 | Best DX in observability; integrations for everything. |
| Production readiness | 100 | Battle-tested at every scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Self-hosted LGTM** | You have ops capacity; you want OSS; cost-sensitive. | You want SaaS simplicity. |
| **Datadog** | You want everything + best DX + budget allows. | Cost-sensitive; you don't use all features. |
| **New Relic** | APM-first; pricing model appeals to you. | You want OSS. |
| **Honeycomb** | Tracing-first; high-cardinality debugging. | You want metrics + logs primarily. |
| **Elastic** | Log-heavy / security / compliance. | Metrics-only setups. |
| **Dynatrace** | Enterprise; AI root-cause. | Most teams — overkill + expensive. |
| **No observability** | Throwaway. | Anything in production. |

## Sources

- [OpenTelemetry](https://opentelemetry.io/) — 2026
- [OpenTelemetry Docs](https://opentelemetry.io/docs/) — 2026
- [Prometheus](https://prometheus.io/) — 2026
- [Prometheus Docs](https://prometheus.io/docs/) — 2026
- [Grafana](https://grafana.com/) — 2026
- [Grafana Docs](https://grafana.com/docs/) — 2026
- [Grafana Mimir](https://grafana.com/oss/mimir/) — 2026
- [Grafana Loki](https://grafana.com/oss/loki/) — 2026
- [Grafana Tempo](https://grafana.com/oss/tempo/) — 2026
- [Datadog](https://www.datadoghq.com/) — 2026
- [Datadog Docs](https://docs.datadoghq.com/) — 2026
- [Elastic Observability](https://www.elastic.co/observability) — 2026
- [OpenTelemetry Blog — State of OTel 2025](https://opentelemetry.io/blog/2025/state-of-opentelemetry/) — 2025
- [ClickHouse — Best OSS Observability 2026](https://clickhouse.com/resources/engineering/best-open-source-observability-solutions) — 2025-11
- [Jaeger](https://www.jaegertracing.io/) — 2026
- [Elastic](https://www.elastic.co/) — 2026
- [New Relic](https://newrelic.com/) — 2026
- [Honeycomb](https://www.honeycomb.io/) — 2026
- [Dynatrace](https://www.dynatrace.com/) — 2026