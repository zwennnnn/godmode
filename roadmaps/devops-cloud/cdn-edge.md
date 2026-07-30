---
name: CDN and Edge Networking
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://www.cloudflare.com/
  - https://developers.cloudflare.com/
  - https://www.fastly.com/
  - https://docs.fastly.com/
  - https://aws.amazon.com/cloudfront/
  - https://docs.aws.amazon.com/AmazonCloudFront/
  - https://cloud.google.com/cdn
  - https://azure.microsoft.com/en-us/products/cdn
  - https://bunny.net/
  - https://docs.bunny.net/
  - https://www.jsdelivr.com/
  - https://workers.cloudflare.com/
  - https://vercel.com/docs/edge-network
  - https://fly.io/docs/networking/
  - https://www.akamai.com/
  - https://www.keycdn.com/
tags: [cdn, edge, cloudflare, fastly, cloudfront, bunny, vercel, akamai, networking]
---

# CDN and Edge Networking

## One-liner

Caches and compute at hundreds of points of presence worldwide — making your site fast globally and resilient to traffic spikes.

## What It Is

A **CDN (Content Delivery Network)** caches your static and dynamic content at edge locations close to users, reducing latency and offloading your origin. **Edge compute** (Cloudflare Workers, Fastly Compute@Edge, CloudFront Functions) lets you run code at the edge — auth, redirects, A/B testing, geo-routing.

The 2026 landscape:

| Provider | Sweet spot | Notes |
|----------|------------|-------|
| **[Cloudflare](https://www.cloudflare.com/)** | Default for most; massive edge; Workers for compute; best free tier. | 300+ POPs; aggressive caching; Workers / Durable Objects; R2 (S3-compatible). |
| **[Fastly](https://www.fastly.com/)** | Compute@Edge (Wasm); best for dynamic content; instant purge. | Loved by DevOps / SRE teams; great for high-traffic media. |
| **[AWS CloudFront](https://aws.amazon.com/cloudfront/)** | AWS-native; Lambda@Edge; deep AWS integration. | Default if you're on AWS. |
| **[Google Cloud CDN](https://cloud.google.com/cdn)** | GCP-native; pairs with Cloud Armor. | |
| **[Azure CDN](https://azure.microsoft.com/en-us/products/cdn)** | Azure-native. | |
| **[Bunny CDN](https://bunny.net/)** | Cheapest; simple; great for indie. | Pay-per-GB; simple API. |
| **[jsDelivr](https://www.jsdelivr.com/)** | OSS / npm / GitHub asset delivery. | Free for OSS. |
| **[Akamai](https://www.akamai.com/)** | Enterprise CDN; legacy dominance; massive scale. | |
| **Vercel Edge Network** | Tight Next.js integration. | |
| **Fly.io** | Edge VMs + Workers. | |

### Edge compute (the 2026 hotness)
- **Cloudflare Workers** — V8 isolates; sub-ms cold start; Durable Objects for state.
- **Fastly Compute@Edge** — Wasm-based; powerful; loved for its VCL / Compute model.
- **CloudFront + Lambda@Edge** — AWS-native; Lambda at edge.
- **Vercel Edge Functions** — Next.js integration.

### Beyond CDNs: edge services
- **DNS**: Cloudflare DNS, Route 53, NS1, Bunny DNS.
- **DDoS protection**: Cloudflare, AWS Shield, Fastly.
- **WAF**: Cloudflare WAF, AWS WAF, Fastly Next-Gen WAF.
- **Bot management**: Cloudflare Bot Management, DataDome, Imperva.

## When To Use It

### Cloudflare
- **Default for most projects in 2026.** Free tier includes CDN + DNS + DDoS + basic Workers.
- **You want the best price/performance** in the market.
- **You want one vendor** for CDN + DNS + WAF + Workers + R2 + KV.

### Fastly
- **You need Compute@Edge** for complex edge logic (Wasm).
- **You have high-traffic media / streaming** and need instant purge.
- **You're a publisher** with strict cacheability requirements.

### AWS CloudFront
- **You're on AWS** and want native integration.

### Bunny CDN
- **Cost-sensitive indie / small project.**
- **You want simple pay-per-GB pricing.**

### Vercel Edge
- **Next.js + Vercel deploy.**

### Akamai
- **Enterprise** with massive global media needs.

## When NOT To Use It

### Cloudflare
- **You need a specific AWS-only feature** (Lambda@Edge with full Lambda capabilities).

### Fastly
- **Cost-sensitive** — Fastly is more expensive than Cloudflare / Bunny at small scale.
- **You want the simplest setup** — Cloudflare's free tier is simpler.

### CloudFront
- **You're not on AWS.**

### Bunny CDN
- **You need edge compute** — Bunny has limited compute.
- **Enterprise compliance** — Bunny is indie-friendly but not enterprise-certified.

## Why It Matters in 2026

Three forces:

1. **Edge compute became a first-class deployment target.** Cloudflare Workers + Durable Objects, Fastly Compute, CloudFront Functions are real production platforms, not toys.
2. **Cloudflare ate the SMB market.** Free CDN + DNS + DDoS + basic Workers is a complete package. The "you need AWS for CDN" reflex is dying.
3. **Bandwidth costs dropped; compute at edge grew.** Bunny, Cloudflare, and Fastly all compete on price/performance in ways they didn't 5 years ago.

Practitioner defaults in 2026:
- **Default**: **Cloudflare** (free + paid).
- **AWS-native**: **CloudFront + Lambda@Edge**.
- **Edge compute**: **Cloudflare Workers** (default) or **Fastly Compute** (advanced).
- **Media / streaming**: **Fastly** or **Akamai**.
- **Indie / cost**: **Bunny CDN**.

## Scoring Matrix (0–100)

### Cloudflare
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 15+ years old; the de-facto CDN. |
| Community | 95 | Massive; beloved by devs. |
| Learning curve | 85 | Free tier instant; Workers take some study. |
| Performance | 95 | 300+ POPs; aggressive caching. |
| Cost | 95 | Best free tier; cheap paid. |
| DX | 90 | Dashboard excellent; Workers CLI great. |
| Production readiness | 100 | Battle-tested at every scale. |

### Fastly
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 10+ years; enterprise standard. |
| Community | 75 | Smaller than Cloudflare; SRE-focused. |
| Learning curve | 65 | Compute@Edge is powerful but Wasm mental model. |
| Performance | 100 | Best edge performance for dynamic content. |
| Cost | 60 | More expensive than Cloudflare / Bunny at scale. |
| DX | 75 | Powerful; steep. |
| Production readiness | 95 | Used by major publishers. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Cloudflare** | Default for most. | AWS-only integration needs. |
| **Fastly** | Compute@Edge; high-traffic media; instant purge. | Cost-sensitive. |
| **CloudFront** | AWS-native. | Multi-cloud. |
| **Bunny CDN** | Cost-sensitive; simple. | Enterprise compliance; edge compute. |
| **Akamai** | Enterprise media. | Most teams — overkill. |
| **Self-hosted origin (no CDN)** | Local-only apps. | Public apps. |
| **Vercel / Netlify built-in** | Static sites on those platforms. | Custom backend. |

## Sources

- [Cloudflare](https://www.cloudflare.com/) — 2026
- [Cloudflare Developer Docs](https://developers.cloudflare.com/) — 2026
- [Fastly](https://www.fastly.com/) — 2026
- [Fastly Docs](https://docs.fastly.com/) — 2026
- [AWS CloudFront](https://aws.amazon.com/cloudfront/) — 2026
- [CloudFront Docs](https://docs.aws.amazon.com/AmazonCloudFront/) — 2026
- [Google Cloud CDN](https://cloud.google.com/cdn) — 2026
- [Azure CDN](https://azure.microsoft.com/en-us/products/cdn) — 2026
- [Bunny CDN](https://bunny.net/) — 2026
- [Bunny Docs](https://docs.bunny.net/) — 2026
- [jsDelivr](https://www.jsdelivr.com/) — 2026
- [Cloudflare Workers](https://workers.cloudflare.com/) — 2026
- [Vercel Edge Network](https://vercel.com/docs/edge-network) — 2026
- [Fly.io Networking](https://fly.io/docs/networking/) — 2026
- [Akamai](https://www.akamai.com/) — 2026
- [KeyCDN](https://www.keycdn.com/) — 2026