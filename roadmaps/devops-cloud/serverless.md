---
name: Serverless
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://aws.amazon.com/lambda/
  - https://docs.aws.amazon.com/lambda/
  - https://cloud.google.com/functions
  - https://learn.microsoft.com/en-us/azure/azure-functions/
  - https://workers.cloudflare.com/
  - https://developers.cloudflare.com/workers/
  - https://vercel.com/docs/functions
  - https://deno.com/deploy
  - https://docs.aws.amazon.com/apigateway/
  - https://supabase.com/docs/guides/functions
  - https://fly.io/docs/launch/
  - https://www.netlify.com/products/functions/
  - https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html
  - https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
  - https://cloud.google.com/workflows
tags: [serverless, lambda, cloud-functions, workers, edge, faas, vercel, deno-deploy, cloudflare]
---

# Serverless (Lambda / Cloud Functions / Cloudflare Workers)

## One-liner

Functions-as-a-Service — upload code, the cloud runs it on demand, scales to zero when idle, and bills per millisecond. No servers to manage.

## What It Is

Serverless computing (FaaS — Functions as a Service) lets you deploy individual functions triggered by events (HTTP request, queue message, cron, file upload, webhook). The cloud provider:

- **Starts your function** when triggered.
- **Scales horizontally** to thousands of concurrent invocations.
- **Scales to zero** when idle — no cost when not running.
- **Bills per millisecond** of execution time + per invocation.

The 2026 platform landscape:

### Hyperscaler FaaS
| Platform | Notes |
|----------|-------|
| **[AWS Lambda](https://aws.amazon.com/lambda/)** | The original (2014); broadest integration with AWS ecosystem; Node/Python/Go/Java/Ruby/.NET/Custom. |
| **[Google Cloud Functions](https://cloud.google.com/functions)** | 1st / 2nd gen; event-driven; ties into GCP ecosystem. |
| **[Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)** | Strong in Microsoft shops; C# first-class; Durable Functions for stateful workflows. |

### Edge-first / modern
| Platform | Notes |
|----------|-------|
| **[Cloudflare Workers](https://workers.cloudflare.com/)** | Runs at the edge (300+ POPs); V8 isolate (not a container); sub-millisecond cold start; loved for global apps. |
| **[Vercel Functions](https://vercel.com/docs/functions)** | Tight Next.js integration; edge + serverless; zero-config. |
| **[Deno Deploy](https://deno.com/deploy)** | Deno-native; edge; great for TS/JS. |
| **[Netlify Functions](https://www.netlify.com/products/functions/)** | Netlify ecosystem; AWS Lambda under the hood. |
| **[Supabase Edge Functions](https://supabase.com/docs/guides/functions)** | Deno-based; Postgres integration; great for Supabase apps. |
| **[Fly.io](https://fly.io/docs/launch/)** | Not strictly FaaS but closest to "git push to a global app". |

### Patterns
- **HTTP API** → FaaS behind API Gateway / Cloudflare / Vercel routing.
- **Event-driven** → FaaS triggered by S3 / EventBridge / Pub/Sub / Kafka / queues.
- **Cron** → Scheduled FaaS invocations.
- **Workflow orchestration** → AWS Step Functions / Google Workflows / Azure Durable Functions.
- **Stream processing** → Lambda + Kinesis / Pub/Sub + Dataflow.

## When To Use It

### Cloudflare Workers
- **Global edge apps** that need <50ms response worldwide.
- **API gateways / middleware / auth** that benefits from edge execution.
- **You want V8 isolates** (no container cold start; sub-millisecond).

### AWS Lambda
- **You're on AWS** and want FaaS that integrates with every AWS service.
- **You need the broadest runtime support.**
- **Event-driven architectures** (S3 → Lambda → DynamoDB, etc.).

### Vercel Functions
- **You're on Next.js / Vercel.** Default.
- **You want zero-config deploy + preview deployments.**

### GCP / Azure Functions
- **You're already in those ecosystems.**

### Edge functions generally
- **CDN logic** (auth, redirects, A/B testing, geo-routing).
- **Lightweight API endpoints** that need to be globally fast.
- **Webhooks** from third parties.

## When NOT To Use It

### Any FaaS
- **Long-running processes** (>15 min on Lambda; even Cloudflare has limits).
- **Heavy compute** — GPU, ML training, big data transforms.
- **Sub-millisecond latency** with cold start risk — use warm provisioned concurrency (Lambda) or edge isolates (Workers).
- **Stateful workflows** without orchestration — use Step Functions / Workflows / Temporal.
- **You need full control of the runtime** — Lambda custom runtimes exist but are awkward.

### Lambda specifically
- **You have a multi-cloud strategy.** Lambda is AWS-only.

### Cloudflare Workers
- **You need Node-native APIs** (Workers uses V8 isolates, not full Node). Some packages don't work.

### Edge functions generally
- **You're processing large payloads** — edge runtimes have memory limits.

## Why It Matters in 2026

Three forces:

1. **Edge FaaS matured.** Cloudflare Workers + Durable Objects, Vercel Edge, Deno Deploy make global sub-50ms APIs routine. The "serverless = slow cold start" perception is dead for edge runtimes.
2. **Cost economics shifted.** Always-on servers are expensive; serverless scales to zero. For spiky / event-driven / unpredictable loads, serverless is materially cheaper.
3. **Lambda + AI agents converged.** LLM-powered agents that run on Lambda invocations are a real pattern in 2026. AWS Lambda response streaming makes long-running LLM calls viable.

Practitioner defaults in 2026:
- **Global edge API** → Cloudflare Workers.
- **Next.js app** → Vercel Functions.
- **AWS event-driven** → Lambda + EventBridge.
- **Cron jobs** → Cloudflare Workers Cron Triggers / Lambda + EventBridge.
- **Webhooks** → Cloudflare Workers / Lambda.

## Scoring Matrix (0–100)

### Lambda
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 11+ years old; the original FaaS. |
| Community | 95 | Massive; every AWS tutorial uses Lambda. |
| Learning curve | 70 | Easy to start; cold start tuning + IAM + event sources take study. |
| Performance | 85 | Cold starts <1s; Provisioned Concurrency eliminates them. |
| Cost | 75 | Cheap at low scale; can get expensive at high scale. |
| DX | 80 | SAM / CDK / Terraform; AWS console dated. |
| Production readiness | 100 | Battle-tested at every scale. |

### Cloudflare Workers
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | 7+ years old; rapidly evolving. |
| Community | 85 | Growing fast; loved by perf-focused devs. |
| Learning curve | 75 | Easy for JS devs; V8 isolates vs Node mental model. |
| Performance | 100 | Sub-millisecond cold start; 300+ POPs. |
| Cost | 90 | Free tier generous; cheap paid. |
| DX | 85 | Wrangler CLI excellent; Dashboard great. |
| Production readiness | 90 | Used at massive scale; Durable Objects are the new hotness. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Containers (ECS / Cloud Run)** | Long-running services; stateful workloads; custom runtimes. | Spiky / event-driven / cost-sensitive at low scale. |
| **Kubernetes** | Multi-service / multi-team / complex orchestration. | Single-purpose functions. |
| **VPS (DO, Hetzner)** | Steady-state workloads; you can predict load. | Spiky load where idle cost matters. |
| **Edge containers (Fly, Railway)** | You want containers but with git-push deploy + global. | You want pure FaaS simplicity. |
| **PaaS (Heroku, Render)** | You want git-push-to-deploy for always-on apps. | Event-driven / spiky. |

## Sources

- [AWS Lambda](https://aws.amazon.com/lambda/) — 2026
- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/) — 2026
- [Google Cloud Functions](https://cloud.google.com/functions) — 2026
- [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/) — 2026
- [Cloudflare Workers](https://workers.cloudflare.com/) — 2026
- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/) — 2026
- [Vercel Functions](https://vercel.com/docs/functions) — 2026
- [Deno Deploy](https://deno.com/deploy) — 2026
- [AWS API Gateway](https://docs.aws.amazon.com/apigateway/) — 2026
- [Supabase Edge Functions](https://supabase.com/docs/guides/functions) — 2026
- [Fly.io Launch](https://fly.io/docs/launch/) — 2026
- [Netlify Functions](https://www.netlify.com/products/functions/) — 2026
- [AWS S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) — 2026
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) — 2026
- [Google Cloud Workflows](https://cloud.google.com/workflows) — 2026