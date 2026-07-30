---
name: DevOps + Cloud
slug: devops-cloud
source: https://roadmap.sh/devops + https://roadmap.sh/cloud
last-updated: 2026-07-30
tech-count: 10
status: in-progress
---

# DevOps + Cloud Roadmap

> **Category:** Technologies for shipping, deploying, scaling, and operating production systems — covering containers, orchestration, IaC, cloud platforms, CI/CD, observability, serverless, secrets, networking, and incident management.
> **Sources:** [roadmap.sh/devops](https://roadmap.sh/devops), [roadmap.sh/cloud](https://roadmap.sh/cloud), [roadmap.sh/backend](https://roadmap.sh/backend) (deployment section)

This roadmap covers the operational stack for any serious production system in 2026. The 10 picks below are the ones that decide your deploy velocity, your MTTR (mean time to recovery), your cloud bill, and your weekend pager duty.

---

## Technologies (all researched 2026-07-30)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Docker & Containers | [docker-containers.md](docker-containers.md) | researched |
| 2 | Kubernetes & Container Orchestration | [kubernetes.md](kubernetes.md) | researched |
| 3 | Infrastructure as Code (Terraform / OpenTofu / Pulumi) | [infrastructure-as-code.md](infrastructure-as-code.md) | researched |
| 4 | Cloud Providers (AWS / GCP / Azure + specialty) | [cloud-providers.md](cloud-providers.md) | researched |
| 5 | CI/CD (GitHub Actions / GitLab CI / Argo CD) | [ci-cd.md](ci-cd.md) | researched |
| 6 | Observability (OpenTelemetry + Prometheus + Grafana) | [observability.md](observability.md) | researched |
| 7 | Serverless (Lambda / Cloudflare Workers / Cloud Run) | [serverless.md](serverless.md) | researched |
| 8 | Secrets Management (Vault / Doppler / AWS Secrets Manager) | [secrets-management.md](secrets-management.md) | researched |
| 9 | CDN & Edge Networking (Cloudflare / Fastly / Bunny) | [cdn-edge.md](cdn-edge.md) | researched |
| 10 | Logging & Incident Management (Loki / ELK / PagerDuty / incident.io) | [logging-incident.md](logging-incident.md) | researched |

---

## Quick Decision Guide

### If you're shipping an MVP / small web app

**Don't reach for Kubernetes.** The default 2026 stack:

- **Containers**: Docker + multi-stage builds + distroless images.
- **Hosting**: Vercel / Netlify / Fly / Render (git-push-to-deploy).
- **Database**: Neon / Supabase / PlanetScale (managed, free tiers).
- **CI/CD**: GitHub Actions (built-in).
- **CDN**: Cloudflare (free tier).
- **Secrets**: Doppler / Infisical (dev-first).
- **Observability**: Skip until you have users; then add Sentry for errors.
- **Logging**: Cloud-native (CloudWatch / Cloud Logging).

### If you're shipping a production web app

- **Containers**: Docker + multi-stage; push to managed registry (ECR / GHCR).
- **Orchestration**: **ECS Fargate** or **Cloud Run** (skip K8s unless you have a K8s team).
- **IaC**: **OpenTofu** (OSS) or Terraform + S3 backend.
- **Cloud**: AWS / GCP / Azure depending on team familiarity.
- **CI/CD**: GitHub Actions for CI + **Argo CD** for K8s deploy (or just GitHub Actions for ECS/Cloud Run).
- **Observability**: LGTM self-hosted OR Grafana Cloud OR Datadog.
- **Secrets**: Cloud-native secret manager + Doppler for dev.
- **CDN**: Cloudflare (paid for serious traffic) or CloudFront (AWS-native).
- **Logging**: Loki + Grafana OR Cloud-native.
- **Incidents**: PagerDuty OR incident.io.

### If you're at scale / regulated

- **K8s**: Managed (EKS / GKE / AKS) + Argo CD + Helm/Kustomize.
- **IaC**: OpenTofu + Atlantis or Terraform Cloud + Sentinel policies.
- **Cloud**: Multi-account AWS / GCP organization setup.
- **CI/CD**: GitHub Actions + Argo CD + Drift Detection.
- **Observability**: Datadog OR Grafana Cloud (managed LGTM).
- **Secrets**: HashiCorp Vault + cloud-native.
- **CDN**: Cloudflare Enterprise / Fastly / Akamai.
- **Logging**: Splunk / Elastic Cloud / ClickHouse-based.
- **Incidents**: PagerDuty + dedicated SRE on-call + SLOs / error budgets.

---

## Cross-references

- For the application layer, see [`../frontend-backend/README.md`](../frontend-backend/README.md).
- For AI/ML workloads, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- For mobile deployment, see [`../mobile/README.md`](../mobile/README.md) (Phase 5).

---

## Build progress

**Phase 4 complete** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`. Next: Phase 5 (mobile roadmap).

---

## Cross-references

- For the application layer, see [`../frontend-backend/README.md`](../frontend-backend/README.md).
- For AI/ML workloads, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- For mobile deployment, see [`../mobile/README.md`](../mobile/README.md) (Phase 5).

---

## Build progress

**Phase 4 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.