---
name: Kubernetes
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://kubernetes.io/
  - https://kubernetes.io/docs/home/
  - https://kubernetes.io/docs/concepts/overview/
  - https://github.com/kubernetes/kubernetes
  - https://kubernetes.io/docs/concepts/containers/
  - https://aws.amazon.com/eks/
  - https://cloud.google.com/kubernetes-engine
  - https://azure.microsoft.com/en-us/products/kubernetes-service
  - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
  - https://cloud.google.com/run
  - https://fly.io/
  - https://k3s.io/
  - https://k3d.io/
  - https://kind.sigs.k8s.io/
  - https://www.cncf.io/projects/
  - https://argo-cd.readthedocs.io/
  - https://helm.sh/
tags: [kubernetes, k8s, eks, gke, aks, containers, orchestration, devops, helm, argocd]
---

# Kubernetes

## One-liner

Google's open-source container orchestration platform — the de-facto standard for running containerized workloads at scale, with a steep learning curve and a vast ecosystem.

## What It Is

Kubernetes (K8s) is a declarative container orchestrator: you describe the **desired state** of your application (containers, replicas, networking, storage), and the control plane continuously reconciles the actual state to match. It handles scheduling, scaling, self-healing, rolling updates, service discovery, config / secret management, and storage orchestration.

The 2026 ecosystem splits into three layers:

| Layer | Examples |
|-------|----------|
| **Managed K8s** | [Amazon EKS](https://aws.amazon.com/eks/), [Google GKE](https://cloud.google.com/kubernetes-engine), [Azure AKS](https://azure.microsoft.com/en-us/products/kubernetes-service), DigitalOcean DOKS, Linode LKE, Vultr VK8s |
| **Lightweight K8s (local / edge)** | [k3s](https://k3s.io/), [k3d](https://k3d.io/), [kind](https://kind.sigs.k8s.io/), MicroK8s |
| **K8s-adjacent tooling** | [Helm](https://helm.sh/) (package manager), [Argo CD](https://argo-cd.readthedocs.io/) (GitOps), Istio / Linkerd (service mesh), cert-manager, ExternalDNS, Kustomize |
| **"Kubernetes but simpler" alternatives** | [AWS ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) / Fargate, [Google Cloud Run](https://cloud.google.com/run), [Fly.io](https://fly.io/), Nomad, Heroku-style PaaS |

Core primitives (per [Kubernetes docs](https://kubernetes.io/docs/concepts/overview/)):
- **Pod** — smallest deployable unit (1+ containers sharing network/storage).
- **Deployment** — declarative replica set + rolling updates.
- **Service** — stable network endpoint for a set of pods.
- **Ingress** — HTTP/S routing into the cluster.
- **ConfigMap / Secret** — config injection.
- **StatefulSet** — for stateful workloads (databases, queues).
- **DaemonSet** — one pod per node.
- **Job / CronJob** — batch workloads.

Adoption: Kubernetes is the **#1 container orchestrator**; CNCF's flagship project. Used by >90% of large organizations running containers. Most "cloud-native" tooling assumes K8s.

## When To Use It

- **You have ≥10 services / ≥100 pods / multi-region / multi-team** — K8s pays off.
- **You need polyglot infra** (some services Java, some Python, some Go) — K8s handles them uniformly.
- **You need advanced deployment patterns** (canary, blue/green, GitOps via Argo CD).
- **You want portability** — K8s runs on any cloud, on-prem, hybrid.
- **You're a platform team** building internal infrastructure.
- **You have a heavy stateful workload** that benefits from StatefulSets + Operators (e.g., Kafka, Postgres operators).

## When NOT To Use It

- **You have 1–5 services and a small team.** ECS / Cloud Run / Fly / Render / Railway is 10× simpler.
- **You're a solo founder or 2-person startup.** Don't.
- **You have no dedicated platform / DevOps engineer.** K8s ops is a full-time job.
- **Your workload is event-driven / spiky** — serverless platforms (Lambda, Cloud Run, Cloudflare Workers) are simpler and cheaper.
- **You need sub-second cold starts.** K8s pods take 5–30s to start; use serverless.
- **You're prototyping** — PaaS / Heroku-style is faster.

## Why It Matters in 2026

Three forces:

1. **Managed K8s got good.** EKS, GKE, and AKS all ship with sensible defaults, autoscaling, and managed control planes. The "you must run your own control plane" horror story is mostly over.
2. **GitOps became the default deploy pattern.** Argo CD + Flux + Helm/Kustomize = commit-to-deploy. The "kubectl apply" cowboy era ended.
3. **"Simpler than K8s" alternatives matured.** AWS ECS, Google Cloud Run, Fly.io, Render all handle 80% of K8s use cases with 20% of the ops cost. The "you must use K8s" reflex is dying.

Practitioner defaults in 2026:
- **Greenfield at small scale** → ECS Fargate or Cloud Run.
- **Greenfield at medium scale** → managed K8s (EKS/GKE/AKS).
- **Greenfield at large scale** → managed K8s + Argo CD + Helm + Istio (if mesh needed).
- **Local dev** → k3d or Docker Desktop's K8s.
- **Stateful** → StatefulSets + Operators (Postgres Operator, Kafka Operator).
- **GPU / ML** → K8s + NVIDIA device plugin or KubeRay.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 11+ years old (Google, 2014); CNCF graduated 2018; the standard. |
| Community | 95 | Largest cloud-native ecosystem; CNCF's flagship; huge provider / tooling support. |
| Learning curve | 40 | Steep — networking, RBAC, operators, Helm, GitOps, security. Months to proficiency. |
| Performance | 85 | Excellent at scale; cold start slower than serverless; resource efficiency improving. |
| Cost | 50 | Managed K8s is "cheap per node" but ops cost is real; managed control planes add up. |
| DX (developer experience) | 65 | Powerful but complex; Lens / k9s + GitOps help a lot. |
| Production readiness | 95 | Battle-tested at every hyperscaler; the default for serious scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **AWS ECS / Fargate** | You're on AWS; you want simpler than K8s; you don't need K8s APIs. | You need multi-cloud portability or K8s-specific tooling. |
| **Google Cloud Run** | You're on GCP; you have stateless containers; you want scale-to-zero. | You need StatefulSets / long-running stateful workloads. |
| **Fly.io** | You want simple deploy + global edge + VMs (not just containers). | You have a huge existing K8s ecosystem dependency. |
| **Nomad** | You want simpler orchestration with K8s-like features + non-container workloads. | You need the K8s ecosystem / tooling. |
| **Heroku / Render / Railway** | You want git-push-to-deploy; you're a small team. | You need fine-grained control or scale beyond PaaS limits. |
| **Docker Swarm** | You want simple Docker-native orchestration. | You need the K8s ecosystem. |
| **Serverless (Lambda, Workers)** | Event-driven, spiky, sub-second cold start. | Long-running, stateful, predictable cost. |

## Sources

- [Kubernetes Official Site](https://kubernetes.io/) — 2026
- [Kubernetes Docs](https://kubernetes.io/docs/home/) — 2026
- [Kubernetes Concepts Overview](https://kubernetes.io/docs/concepts/overview/) — 2026
- [Kubernetes GitHub (kubernetes/kubernetes)](https://github.com/kubernetes/kubernetes) — 2026
- [Containers in K8s Concepts](https://kubernetes.io/docs/concepts/containers/) — 2026
- [Amazon EKS](https://aws.amazon.com/eks/) — 2026
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) — 2026
- [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service) — 2026
- [AWS ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) — 2026
- [Google Cloud Run](https://cloud.google.com/run) — 2026
- [Fly.io](https://fly.io/) — 2026
- [k3s](https://k3s.io/) — 2026
- [k3d](https://k3d.io/) — 2026
- [kind (Kubernetes IN Docker)](https://kind.sigs.k8s.io/) — 2026
- [CNCF Projects](https://www.cncf.io/projects/) — 2026
- [Argo CD](https://argo-cd.readthedocs.io/) — 2026
- [Helm](https://helm.sh/) — 2026