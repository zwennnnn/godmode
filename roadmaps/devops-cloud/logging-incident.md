---
name: Logging and Incident Management
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://www.elastic.co/logging
  - https://www.elastic.co/elasticsearch
  - https://www.elastic.co/
  - https://grafana.com/oss/loki/
  - https://www.datadoghq.com/product/log-management/
  - https://www.pagerduty.com/
  - https://www.pagerduty.com/platform/
  - https://docs.pagerduty.com/
  - https://incident.io/
  - https://www.atlassian.com/software/jira/opensource/opsgenie
  - https://www.splunk.com/
  - https://www.sre.google/
  - https://sre.google/sre-book/
  - https://www.honeycomb.io/
  - https://vector.dev/
  - https://github.com/vectordotdev/vector
  - https://opentelemetry.io/docs/collector/
tags: [logging, elk, loki, datadog, pagerduty, incident, opsgenie, splunk, incident.io, sre]
---

# Logging and Incident Management (ELK / Datadog / PagerDuty / Splunk)

## One-liner

Centralized logging for forensics + on-call alerting + incident response when things break at 3 AM.

## What It Is

Two distinct (but related) domains:

1. **Logging** — collect, store, search, and visualize log events from all your services.
2. **Incident management** — get the right people paged at the right time, run incident response, learn from post-mortems.

### Logging landscape (2026)

| Tool | Positioning |
|------|-------------|
| **[Elastic Stack (ELK)](https://www.elastic.co/)** | Elasticsearch + Logstash + Kibana. The classic; powerful search; ops-heavy. |
| **[Grafana Loki](https://grafana.com/oss/loki/)** | Prometheus-for-logs; cheap; pairs with Grafana. |
| **[Datadog Log Management](https://www.datadoghq.com/product/log-management/)** | Part of Datadog suite; great DX; expensive. |
| **[Splunk](https://www.splunk.com/)** | Enterprise log analytics; powerful queries; very expensive. |
| **[Vector](https://vector.dev/)** | Log / event pipeline; Rust-based; replaces Logstash / Fluentd. |
| **Cloud-native**: CloudWatch (AWS), Cloud Logging (GCP), Azure Monitor | Default for each cloud; tight integration. |
| **ClickHouse-based** (Quickwit, HyperDX) | Newer; SQL-native; cost-effective. |

### Incident management landscape (2026)

| Tool | Positioning |
|------|-------------|
| **[PagerDuty](https://www.pagerduty.com/)** | The 800-lb gorilla; on-call schedules + alerting + incident response. |
| **[incident.io](https://incident.io/)** | Modern Slack-first incident management; loved by startups. |
| **[Opsgenie (Atlassian)](https://www.atlassian.com/software/jira/opensource/opsgenie)** | Atlassian-integrated; on-call + alerting. |
| **FireHydrant** | SRE-focused incident response. |
| **Grafana Incident** | New (2024+); integrated with Grafana. |
| **GitHub / GitLab / Linear** | Many teams use issue trackers for low-severity incident tracking. |
| **Self-hosted** (Squadcast, ilert) | European / data-residency focused. |

### SRE practices (per [Google SRE Book](https://sre.google/sre-book/))
- **SLIs / SLOs / Error budgets** — define what "reliable" means quantitatively.
- **Blameless post-mortems** — every incident is a learning, not a finger-pointing session.
- **On-call rotations** — shared burden; documented runbooks.
- **Runbooks** — for every alert.
- **Chaos engineering** (optional) — Netflix-style controlled failure testing.

## When To Use It

### Logging
- **Cloud-native + Grafana** → **Loki** (default; cheap).
- **Powerful search + analytics** → **Elastic** or **Splunk**.
- **All-in-one observability** → **Datadog** (logs + metrics + traces in one bill).
- **High-volume + cost-sensitive** → ClickHouse-based (Quickwit, HyperDX) or Loki.
- **AWS-only** → **CloudWatch**.

### Incident management
- **Default for most teams** → **PagerDuty** (mature, integrations for everything).
- **Slack-first / startup** → **incident.io**.
- **Atlassian shop** → **Opsgenie**.
- **Grafana-native stack** → **Grafana Incident**.

## When NOT To Use It

### Elastic / Splunk
- **Cost-sensitive.** Splunk is famously expensive; Elastic is cheaper but still significant at scale.
- **You don't need full-text log search.** Loki / CloudWatch Logs may be enough.

### Datadog Logs
- **Cost-sensitive** — Datadog bills per GB ingested + per GB indexed. Often 3–10× self-hosted.
- **You don't need the rest of Datadog's suite.**

### PagerDuty
- **Tiny team** with no on-call rotation — Slack alerts + a shared phone may be enough.
- **You want a Slack-first UX** — incident.io.

### Self-hosted log stacks (ELK / Loki)
- **You don't have ops capacity.** Managed is cheaper than an SRE.

## Why It Matters in 2026

Three forces:

1. **Logs + observability converged.** Most teams run logs + metrics + traces from one platform (Datadog, Grafana Cloud, Elastic Observability). The "logs are separate from metrics" era is ending.
2. **Incident management got Slack-first.** incident.io showed the world that incident response can live where the team already works. Status quo PagerDuty + email is being challenged.
3. **SRE practices standardized.** SLIs / SLOs / error budgets are now baseline expectations at every serious company.

Practitioner defaults in 2026:
- **Logging**: **Loki + Grafana** (default for OSS) or **Datadog** (default for SaaS budget).
- **Incident**: **PagerDuty** (default) or **incident.io** (Slack-first).
- **Vector / Fluent Bit** as the log shipper (replaces Logstash / Fluentd).
- **SLOs in error budget policy** as part of on-call expectations.

## Scoring Matrix (0–100)

### Loki + Grafana
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 6+ years; CNCF incubating. |
| Community | 90 | Rapidly growing; default for cloud-native. |
| Learning curve | 75 | LogQL is similar to PromQL; Grafana UI excellent. |
| Performance | 90 | Cheap; scales horizontally. |
| Cost | 95 | Cheapest serious option. |
| DX | 85 | Grafana UI is best-in-class. |
| Production readiness | 90 | Used at scale; some edge cases still emerging. |

### PagerDuty
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 15+ years old; the standard. |
| Community | 95 | Integrations for everything. |
| Learning curve | 80 | Powerful; schedules / escalation policies / overrides take study. |
| Performance | 90 | Reliable; alert delivery is the product. |
| Cost | 75 | Per-user; adds up at scale. |
| DX | 85 | Mature UI; integrations galore. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Logging Alternative | Better when | Worse when |
|-------------------|-------------|------------|
| **Cloud-native (CloudWatch, etc.)** | Single cloud; tight integration. | Multi-cloud; cost-sensitive. |
| **ELK** | Powerful search; analytics. | Ops capacity; cost at scale. |
| **Loki** | Cheap; pairs with Grafana. | You need full-text SQL. |
| **Datadog** | All-in-one observability. | Cost-sensitive. |
| **Splunk** | Enterprise log analytics. | Most teams — too expensive. |
| **Quickwit / HyperDX** | High-volume + SQL + cost-effective. | You want mature ecosystem. |

| Incident Alternative | Better when | Worse when |
|---------------------|-------------|------------|
| **PagerDuty** | Default; integrations. | You want Slack-first. |
| **incident.io** | Slack-first; modern UX. | You need the deepest integrations. |
| **Opsgenie** | Atlassian shop. | You're not in Atlassian. |
| **Self-hosted (Squadcast, ilert)** | EU / data residency. | You want managed. |
| **No tool** | Tiny team. | Anything 24/7 / with users. |

## Sources

- [Elastic Logging](https://www.elastic.co/logging) — 2026
- [Elasticsearch](https://www.elastic.co/elasticsearch) — 2026
- [Elastic](https://www.elastic.co/) — 2026
- [Grafana Loki](https://grafana.com/oss/loki/) — 2026
- [Datadog Log Management](https://www.datadoghq.com/product/log-management/) — 2026
- [PagerDuty](https://www.pagerduty.com/) — 2026
- [PagerDuty Platform](https://www.pagerduty.com/platform/) — 2026
- [PagerDuty Docs](https://docs.pagerduty.com/) — 2026
- [incident.io](https://incident.io/) — 2026
- [Opsgenie (Atlassian)](https://www.atlassian.com/software/jira/opensource/opsgenie) — 2026
- [Splunk](https://www.splunk.com/) — 2026
- [Google SRE](https://www.sre.google/) — 2026
- [Google SRE Book](https://sre.google/sre-book/) — 2026
- [Honeycomb](https://www.honeycomb.io/) — 2026
- [Vector](https://vector.dev/) — 2026
- [Vector GitHub (vectordotdev/vector)](https://github.com/vectordotdev/vector) — 2026
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) — 2026