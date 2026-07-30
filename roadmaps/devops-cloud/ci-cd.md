---
name: CI/CD
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://docs.github.com/en/actions
  - https://github.com/features/actions
  - https://docs.gitlab.com/ee/ci/
  - https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/
  - https://circleci.com/docs/
  - https://www.jenkins.io/doc/
  - https://www.jenkins.io/
  - https://buildkite.com/docs
  - https://buildkite.com/
  - https://www.drone.io/
  - https://docs.dagger.io/
  - https://dagger.io/
  - https://github.com/argoproj/argo-workflows
  - https://argo-cd.readthedocs.io/
  - https://fluxcd.io/
  - https://spinnaker.io/
tags: [ci-cd, github-actions, gitlab-ci, circleci, jenkins, buildkite, argo, flux, devops]
---

# CI/CD (GitHub Actions / GitLab CI / CircleCI)

## One-liner

The pipeline that turns every code commit into tested, deployable artifacts — and ships them to staging or production on demand or automatically.

## What It Is

CI/CD (Continuous Integration / Continuous Deployment) is the automation that runs on every code change:

- **CI (Continuous Integration)** — every commit triggers: lint → test → build → artifact (container image, binary, package).
- **CD (Continuous Deployment / Delivery)** — every successful main commit (or every PR) deploys to staging/production, with approvals for prod.

The 2026 tool landscape:

| Tool | Type | Best for |
|------|------|----------|
| **[GitHub Actions](https://docs.github.com/en/actions)** | Hosted CI for GitHub repos | Default for GitHub-hosted projects; massive marketplace. |
| **[GitLab CI](https://docs.gitlab.com/ee/ci/)** | Integrated with GitLab | Self-host or SaaS; strong for enterprises / regulated. |
| **[CircleCI](https://circleci.com/docs/)** | Hosted CI | Mature; good DX; cloud + self-hosted. |
| **[Jenkins](https://www.jenkins.io/)** | Self-hosted | The original; massive plugin ecosystem; ops-heavy. |
| **[Buildkite](https://buildkite.com/docs)** | Hybrid (your agents, their orchestration) | Build on your own infra; scale without limits. |
| **[Drone](https://www.drone.io/)** | Container-native CI | Lightweight; YAML pipelines. |
| **[Dagger](https://docs.dagger.io/)** | CI/CD as code (Go / TS / Python) | Pipeline defined in code; runs anywhere. |
| **[Argo Workflows](https://github.com/argoproj/argo-workflows)** | K8s-native workflows | Kubernetes-step pipelines. |
| **[Argo CD](https://argo-cd.readthedocs.io/) + [Flux CD](https://fluxcd.io/)** | GitOps deploy | Pull-based deploy from Git → K8s. |
| **[Spinnaker](https://spinnaker.io/)** | Multi-cloud CD | Netflix-grade; enterprise CD. |

### GitHub Actions (the 2026 default)
- **Workflows** in YAML under `.github/workflows/`.
- **Runners**: GitHub-hosted (Linux / macOS / Windows) or self-hosted.
- **Marketplace**: >20,000 pre-built actions.
- **Matrix builds** for multi-OS / multi-version testing.
- **Reusable workflows** + composite actions.
- **OIDC** for short-lived cloud credentials (no static secrets).
- **Free tier**: 2,000 min/month for private repos; unlimited for public.

### GitLab CI
- **`.gitlab-ci.yml`** in repo root.
- **Runners** (shared or specific).
- **Built-in**: container registry, security scanning, environments, releases, pages.
- **Auto DevOps** for sensible defaults.

## When To Use It

### GitHub Actions
- **Your code is on GitHub.** Default.
- **You want zero-setup CI** with massive marketplace.
- **You want matrix builds, reusable workflows, OIDC** out of the box.

### GitLab CI
- **Your code is on GitLab** (self-host or SaaS).
- **You want an integrated DevOps platform** (issues + CI + CD + security + registry).
- **Enterprise / regulated** with self-hosted requirements.

### CircleCI
- **You want mature CI** with great DX, parallelism, orbs.
- **Legacy migrations** from Jenkins.

### Jenkins
- **You have an existing Jenkins investment.**
- **You need a plugin that's only on Jenkins.**
- **Self-hosted + on-prem** with strict data residency.

### Buildkite
- **You want CI on your own infrastructure** (no SaaS), with their orchestration UX.
- **High-security / regulated** (your build doesn't touch third-party).

### Dagger
- **You want pipelines defined in real code** (Go / TS / Python), not YAML.
- **Local + CI parity** (run the same pipeline locally).

### Argo CD / Flux CD
- **You're on Kubernetes** and want GitOps.

### Argo Workflows
- **You're on K8s** and want to orchestrate complex pipelines / ML workflows as K8s resources.

## When NOT To Use It

### GitHub Actions
- **Your code is on GitLab / Bitbucket.** Use the native CI.
- **You need on-prem build agents** for security. Self-hosted runners are an option but Jenkins/Buildkite are simpler.

### GitLab CI
- **You're all-in on GitHub.**

### Jenkins
- **New project in 2026.** The ops overhead is real; only choose if you have a specific Jenkins-only plugin or hard on-prem requirement.

### Buildkite
- **You don't have ops capacity** to run your own agents.

### Argo CD
- **You're not on Kubernetes.**

### Dagger
- **Your team can't / won't learn Go / TS / Python** for pipeline code.

## Why It Matters in 2026

Three forces:

1. **GitHub Actions became the de-facto default.** Most open-source repos, most startups, most SaaS demos use Actions. The marketplace + OIDC + free tier for public repos is hard to beat.
2. **GitOps (Argo CD / Flux CD) became the deploy default for K8s.** Commit to Git → cluster syncs. No more kubectl apply.
3. **CI/CD-as-code (Dagger) emerged.** Pipelines defined in TS/Python/Go = type-checked, testable, reusable across local + CI.

Practitioner defaults in 2026:
- **GitHub repo** → **GitHub Actions** with reusable workflows.
- **GitLab repo** → **GitLab CI**.
- **K8s production** → **Argo CD** for deploy; **GitHub Actions** for CI.
- **Self-hosted build** → **Buildkite** or self-hosted runners.
- **On-prem legacy** → **Jenkins** (if you must) or migrate.

## Scoring Matrix (0–100)

### GitHub Actions
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 6+ years old; battle-tested; huge ecosystem. |
| Community | 100 | The default for new repos; >20K marketplace actions. |
| Learning curve | 75 | YAML workflows easy; advanced features (composite actions, OIDC) take study. |
| Performance | 85 | Fast hosted runners; matrix builds excellent. |
| Cost | 90 | Generous free tier; pay-as-you-go beyond. |
| DX | 90 | Best-in-class for most teams. |
| Production readiness | 95 | Used by every major OSS project. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **GitLab CI** | GitLab repo; integrated platform. | GitHub repo. |
| **CircleCI** | Mature SaaS CI; great parallelism. | You're on GitHub. |
| **Jenkins** | Plugin you can't get elsewhere; legacy. | New project. |
| **Buildkite** | Your own infra; high security. | You want SaaS simplicity. |
| **Drone** | Container-native CI; lightweight. | You need the largest marketplace. |
| **Dagger** | Pipeline-as-code in TS/Go/Python. | Team can't write pipeline code. |
| **Argo CD / Flux** | K8s GitOps deploy. | Not on K8s. |
| **Spinnaker** | Enterprise multi-cloud CD. | Most teams — overkill. |

## Sources

- [GitHub Actions Docs](https://docs.github.com/en/actions) — 2026
- [GitHub Actions Features](https://github.com/features/actions) — 2026
- [GitLab CI Docs](https://docs.gitlab.com/ee/ci/) — 2026
- [GitLab — Continuous Integration](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/) — 2026
- [CircleCI Docs](https://circleci.com/docs/) — 2026
- [Jenkins Docs](https://www.jenkins.io/doc/) — 2026
- [Jenkins](https://www.jenkins.io/) — 2026
- [Buildkite Docs](https://buildkite.com/docs) — 2026
- [Buildkite](https://buildkite.com/) — 2026
- [Drone](https://www.drone.io/) — 2026
- [Dagger Docs](https://docs.dagger.io/) — 2026
- [Dagger](https://dagger.io/) — 2026
- [Argo Workflows](https://github.com/argoproj/argo-workflows) — 2026
- [Argo CD](https://argo-cd.readthedocs.io/) — 2026
- [Flux CD](https://fluxcd.io/) — 2026
- [Spinnaker](https://spinnaker.io/) — 2026