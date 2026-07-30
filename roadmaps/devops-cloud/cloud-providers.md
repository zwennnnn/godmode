---
name: Cloud Providers (AWS / GCP / Azure)
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://aws.amazon.com/
  - https://docs.aws.amazon.com/
  - https://cloud.google.com/
  - https://cloud.google.com/docs
  - https://azure.microsoft.com/en-us/
  - https://learn.microsoft.com/en-us/azure/
  - https://www.cncf.io/
  - https://www.gartner.com/en/newsroom/press-releases/2024-11-13-gartner-identifies-the-top-strategic-technology-trends-for-2025
  - https://www.statista.com/topics/2531/public-cloud-services/
  - https://fly.io/
  - https://www.digitalocean.com/
  - https://www.alibabacloud.com/
  - https://cloud.oracle.com/
  - https://www.ibm.com/cloud
  - https://www.linode.com/
  - https://www.vultr.com/
tags: [aws, gcp, azure, cloud, cloud-providers, digitalocean, fly, linode, alibaba, oracle, ibm]
---

# Cloud Providers (AWS / GCP / Azure)

## One-liner

The hyperscale public clouds (AWS, Google Cloud, Azure) plus the long tail of specialty providers (DigitalOcean, Fly, Linole, Oracle, IBM, Alibaba) — choosing where your workloads run.

## What It Is

A cloud provider rents compute, storage, networking, and managed services on demand. The hyperscalers (AWS, GCP, Azure) offer 200+ services each; specialty providers focus on simpler / cheaper / specific niches.

### Hyperscalers (the big three)

| Provider | Strengths | Notes |
|----------|-----------|-------|
| **[AWS](https://aws.amazon.com/)** | Largest service catalog; deepest ecosystem; default for enterprise; most job openings. | 200+ services; complex; pricing can be confusing; ~33% market share. |
| **[Google Cloud (GCP)](https://cloud.google.com/)** | Best-in-class data / ML / Kubernetes (GKE is the original); BigQuery; strong networking (premium tier). | ~10% market share; smaller service catalog than AWS; loved by data teams. |
| **[Microsoft Azure](https://azure.microsoft.com/en-us/)** | Default for Microsoft shops (Active Directory, Windows Server, Office 365); strong enterprise compliance; hybrid (Arc). | ~23% market share; deepest enterprise penetration; complex but powerful. |

### Specialty / regional providers

| Provider | Sweet spot |
|----------|-----------|
| **[DigitalOcean](https://www.digitalocean.com/)** | Simple, cheap VMs (Droplets); beloved by startups; great docs; App Platform for PaaS. |
| **[Fly.io](https://fly.io/)** | Global edge + simple git-deploy; Firecracker microVMs; loved for global apps. |
| **[Linode (Akamai)](https://www.linode.com/)** | Cheap VMs; simple; long-running favorite for indie devs. |
| **[Vultr](https://www.vultr.com/)** | Cheap VMs in 30+ locations; bare-metal options. |
| **[Oracle Cloud](https://cloud.oracle.com/)** | Free tier is generous; strong in database (Oracle) shops. |
| **[IBM Cloud](https://www.ibm.com/cloud)** | Enterprise hybrid; mainframes; Watson AI. |
| **[Alibaba Cloud](https://www.alibabacloud.com/)** | Dominant in APAC (especially China); strong in China for compliance. |
| **[Hetzner](https://www.hetzner.com/)** | Cheapest in EU; bare-metal + cloud; great for self-hosted. |

Market share (2024–2025 estimates from [Gartner](https://www.gartner.com/), [Statista](https://www.statista.com/topics/2531/public-cloud-services/)):
- AWS: ~33%
- Azure: ~23%
- GCP: ~10%
- Others: ~34% (mostly Alibaba, Tencent, Oracle, IBM, specialty)

## When To Use It

### AWS
- **Default for serious enterprise / regulated industries.**
- **You need the broadest service catalog** (200+ services).
- **You're optimizing for the largest talent pool** of cloud engineers.

### GCP
- **Data / ML / analytics-heavy workloads** (BigQuery is best-in-class).
- **You want GKE** (the original managed K8s).
- **You use Google's developer tools** (Firebase, etc.).

### Azure
- **You're a Microsoft shop** (Active Directory, Office 365, Windows).
- **Enterprise compliance** requirements.
- **Hybrid cloud** with on-prem Windows.

### DigitalOcean / Linode / Vultr
- **Indie / startup / side project.**
- **Cheap VMs**, simple UI, no enterprise complexity.
- **You don't need 200 services.**

### Fly.io
- **Global edge apps** that need low latency worldwide.
- **You want git-push-to-deploy** with no Kubernetes.

### Hetzner
- **EU-based, cheapest VMs.**
- **GDPR / data residency** in EU.

### Alibaba Cloud
- **You operate in China** or APAC.
- **ICP compliance** in China.

## When NOT To Use It

### AWS
- **You want simplicity.** Specialty providers are easier.
- **You're cost-sensitive at small scale** — AWS pricing is opaque.

### GCP / Azure
- **You need AWS-specific integrations** (most third-party tools integrate with AWS first).
- **You're optimizing for the largest talent pool.**

### Any hyperscaler
- **Tiny project** — specialty provider (DO / Fly / Hetzner) is 1/10 the cost and 10× simpler.
- **Strict data residency / sovereignty** — on-prem or regional provider.
- **Workload is steady-state, not bursty** — cheaper to self-host on Hetzner / OVH.

## Why It Matters in 2026

Three forces:

1. **The "multi-cloud" hype faded.** Most serious shops in 2026 are single-cloud (or cloud + on-prem). Multi-cloud adds cost without proportional benefit unless you have specific compliance / vendor-lock-in concerns.
2. **Specialty providers grew.** Fly, DigitalOcean, Hetzner, Vercel, Render, Railway all carved real niches. The "default to AWS" reflex is dying for new projects.
3. **Edge compute is a category.** Fly.io, Cloudflare, Vercel Edge, Fastly all offer compute at the edge — challenging the "everything in us-east-1" default.

Practitioner defaults in 2026:
- **Serious enterprise / regulated** → AWS (or Azure for Microsoft shops).
- **Data / ML / analytics** → GCP.
- **Startup / indie / MVP** → Vercel + Neon + Upstash + specialty providers (avoid AWS until you need it).
- **Global edge app** → Fly.io + Cloudflare.
- **Cost-sensitive EU** → Hetzner / OVH.
- **China** → Alibaba Cloud / Tencent Cloud.

## Scoring Matrix (0–100)

### AWS
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 19+ years old (2006); the original hyperscaler. |
| Community | 100 | Largest ecosystem; most certifications; most jobs. |
| Learning curve | 50 | 200+ services; massive; certifications take months. |
| Performance | 95 | Excellent; global edge; specialized hardware (Trainium, Graviton). |
| Cost | 60 | Pay-per-use can be cheap at scale; opaque; data egress is the killer. |
| DX | 80 | Excellent once you learn it; AWS Console is dated; CDK / Terraform are better. |
| Production readiness | 100 | Battle-tested at every scale. |

### GCP
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 18+ years old; well-established. |
| Community | 75 | Smaller than AWS but very loyal. |
| Learning curve | 65 | Cleaner console than AWS; fewer services. |
| Performance | 95 | Premium network tier; BigQuery is best-in-class. |
| Cost | 70 | Often cheaper than AWS at comparable scale; sustained-use discounts. |
| DX | 90 | Best cloud console; clean APIs. |
| Production readiness | 95 | Battle-tested. |

### Azure
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 16+ years old; dominant in enterprise. |
| Community | 85 | Microsoft ecosystem; huge in enterprise. |
| Learning curve | 55 | Complex; huge service catalog; portal is dense. |
| Performance | 90 | Excellent; strong hybrid. |
| Cost | 65 | Enterprise pricing; can be negotiated. |
| DX | 75 | Portal is improving; CLI is good. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Specialty providers (DO, Fly, Hetzner)** | Simple / cheap / indie workloads. | Enterprise compliance / scale. |
| **Self-hosted (bare metal + k3s)** | Strict cost / data sovereignty. | You don't have ops capacity. |
| **Colocation** | You want full control without hyperscaler lock-in. | You want managed services. |
| **Vercel / Netlify / Render** | Frontend + simple backend. | Complex backend infra. |
| **On-prem (private cloud)** | Compliance; mature data center. | You don't have a data center. |

## Sources

- [AWS](https://aws.amazon.com/) — 2026
- [AWS Docs](https://docs.aws.amazon.com/) — 2026
- [Google Cloud](https://cloud.google.com/) — 2026
- [Google Cloud Docs](https://cloud.google.com/docs) — 2026
- [Azure](https://azure.microsoft.com/en-us/) — 2026
- [Azure Docs](https://learn.microsoft.com/en-us/azure/) — 2026
- [CNCF](https://www.cncf.io/) — 2026
- [Gartner Top Strategic Tech Trends 2025](https://www.gartner.com/en/newsroom/press-releases/2024-11-13-gartner-identifies-the-top-strategic-technology-trends-for-2025) — 2024-11
- [Statista — Public Cloud Services](https://www.statista.com/topics/2531/public-cloud-services/) — 2025+
- [Fly.io](https://fly.io/) — 2026
- [DigitalOcean](https://www.digitalocean.com/) — 2026
- [Alibaba Cloud](https://www.alibabacloud.com/) — 2026
- [Oracle Cloud](https://cloud.oracle.com/) — 2026
- [IBM Cloud](https://www.ibm.com/cloud) — 2026
- [Linode (Akamai)](https://www.linode.com/) — 2026
- [Vultr](https://www.vultr.com/) — 2026