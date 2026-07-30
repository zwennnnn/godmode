---
name: Docker and Containers
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://docs.docker.com/
  - https://docs.docker.com/build/building/multi-stage/
  - https://docs.docker.com/build/building/best-practices/
  - https://docs.docker.com/engine/swarm/
  - https://www.docker.com/products/docker-desktop
  - https://github.com/moby/moby
  - https://github.com/containerd/containerd
  - https://opencontainers.org/
  - https://northflank.com/blog/docker-build-and-buildx-best-practices-for-optimized-builds
  - https://www.blacksmith.sh/blog/understanding-multi-stage-docker-builds
  - https://oneuptime.com/blog/post/2026-02-02-docker-multi-stage-builds/view
  - https://podman.io/
  - https://github.com/containers/podman
  - https://github.com/GoogleContainerTools/distroless
  - https://www.cncf.io/
tags: [docker, containers, dockerfile, buildx, podman, containerd, oci, devops]
---

# Docker and Containers

## One-liner

The standard for packaging an application + its dependencies into a portable, reproducible image that runs identically across laptop, CI, staging, and production.

## What It Is

Docker is a containerization platform that packages an application, its runtime, libraries, and OS-level dependencies into a single image. The image runs as an **isolated process** on a shared OS kernel via Linux namespaces + cgroups (or Windows equivalents). Containers start in milliseconds, ship as layered filesystems, and are reproducible across environments.

The 2026 ecosystem:

| Layer | Tech | Notes |
|-------|------|-------|
| **Image format** | OCI (Open Container Initiative) | The standard; Docker images are OCI-compatible. |
| **Container runtime** | `containerd` (Docker's default), `CRI-O` | The thing that actually runs containers. |
| **Build tool** | Docker Buildx (BuildKit), [Podman](https://podman.io/), [Buildah](https://github.com/containers/buildah) | Modern builders with caching, multi-arch, rootless modes. |
| **Registry** | Docker Hub, GHCR, ECR, GCR, ACR | Where images are stored and pulled from. |
| **Local dev** | [Docker Desktop](https://www.docker.com/products/docker-desktop), Podman Desktop, Rancher Desktop | Multi-container local dev with Compose / Kind / Kubernetes. |
| **Compose** | Docker Compose, Compose Spec | Multi-container local + simple prod orchestration. |
| **Rootless** | Podman, Buildah, rootless Docker | Run without root for better security. |
| **Distroless / minimal base images** | [Google's distroless](https://github.com/GoogleContainerTools/distroless), `alpine`, `scratch` | Tiny images (10–100MB vs 1GB+ for full base); smaller attack surface. |

### Why multi-stage builds are the default in 2026

Per [Docker's multi-stage docs](https://docs.docker.com/build/building/multi-stage/), [Northflank 2026 guide](https://northflank.com/blog/docker-build-and-buildx-best-practices-for-optimized-builds), and [OneUptime 2026 guide](https://oneuptime.org/blog/post/2026-02-02-docker-multi-stage-builds/view):

- Separate **build stage** (with full toolchain) from **runtime stage** (minimal base).
- Final image contains only the built artifact + runtime deps — typically 10× smaller.
- Better security (fewer tools in the final image = smaller attack surface).
- Required for any production-grade Node.js / Go / Rust / Python / Java image.

Example:
```dockerfile
# Build stage — full toolchain
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Runtime stage — minimal
FROM gcr.io/distroless/nodejs22-debian12
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
EXPOSE 3000
CMD ["dist/server.js"]
```

Adoption: Docker is the de-facto container format; >90% of cloud-native workloads run on containers; OCI is the standard. Docker Desktop has >20M installs; Docker Hub hosts millions of public images.

## When To Use It

- **Any production web service / API / worker** — package once, run anywhere.
- **Any CI/CD pipeline** that needs reproducible builds.
- **Local dev that mirrors prod** — same image on laptop and in K8s.
- **Microservices** — each service gets its own image.
- **Multi-language polyglot environments** — each team picks its own image.
- **You need to ship ML models with their Python/CUDA deps** — Docker image = portable model package.

## When NOT To Use It

- **You can deploy to Vercel / Netlify / Cloudflare Pages** — serverless platform handles packaging.
- **You have a tiny single-binary Go / Rust app** — just copy the binary.
- **You need bare-metal performance** — containers have ~1–3% overhead vs native; usually negligible, but matters for some HPC.
- **You have a Windows-only legacy app** — possible but painful.
- **You don't have ops capacity to maintain a container pipeline** — fall back to PaaS.

## Why It Matters in 2026

Three forces:

1. **The "container image as the deployment unit" won.** Every major cloud + every major PaaS accepts container images. The debate is no longer "containers vs VMs" but "which orchestrator / which PaaS."
2. **Multi-stage + distroless became the default production pattern.** 5 years ago you could ship a 1GB image with full Node + dev tools. Today that's malpractice.
3. **Rootless containers matured.** Podman + rootless Docker + Buildah enable running containers without root, which is the new security baseline.

Practitioner defaults in 2026:
- **Base image**: `distroless` (Google) or `alpine` for Go/Rust; `node:22-alpine` or distroless Node for Node apps; `python:3.13-slim` for Python.
- **Multi-stage builds** for anything non-trivial.
- **BuildKit / Buildx** for caching + parallelism.
- **Image scanning** in CI (Trivy, Snyk, Docker Scout).
- **Pin base image digests**, not tags.
- **Non-root user** in the final image.
- **`.dockerignore`** is non-optional.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 12+ years old (Docker, Inc. 2013); OCI standard since 2015; production-default. |
| Community | 100 | The default container ecosystem; >20M Docker Desktop installs; millions of public images. |
| Learning curve | 75 | Dockerfile basics easy; multi-stage + caching + scanning + orchestration takes practice. |
| Performance | 90 | Negligible overhead (1–3%); fast startup; efficient layering. |
| Cost | 95 | Docker Desktop free for personal/small business; OSS engine free; Docker Hub has free tier. |
| DX (developer experience) | 95 | Excellent; BuildKit fast; Compose for local dev; VS Code / Cursor integration. |
| Production readiness | 100 | Standard for production deployments. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Podman** | You want rootless / daemonless / Docker-compatible CLI. | You depend on Docker Desktop-specific features (Kubernetes in DD). |
| **Buildah** | You want fine-grained image building in scripts / CI without Docker daemon. | You want the simplest DX. |
| **Native packages (deb / rpm)** | Bare-metal / VM deployments with no orchestration. | Anything cloud-native. |
| **Serverless (Lambda / Cloud Functions / Cloudflare Workers)** | You don't want to manage containers at all. | You need long-running processes or custom runtimes. |
| **PaaS (Heroku, Render, Fly)** | You want git-push-to-deploy with no container knowledge. | You need full container control. |
| **Unikernels / Firecracker microVMs** | You want VM-level isolation with container-level speed. | Most apps — overkill. |
| **WebAssembly modules** | Edge compute, browser, plugin systems. | You need full POSIX / Linux. |

## Sources

- [Docker Official Docs](https://docs.docker.com/) — 2026
- [Docker — Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/) — 2026
- [Docker — Build Best Practices](https://docs.docker.com/build/building/best-practices/) — 2026
- [Docker Swarm](https://docs.docker.com/engine/swarm/) — 2026
- [Docker Desktop](https://www.docker.com/products/docker-desktop) — 2026
- [Moby GitHub (moby/moby)](https://github.com/moby/moby) — 2026
- [containerd GitHub (containerd/containerd)](https://github.com/containerd/containerd) — 2026
- [Open Container Initiative](https://opencontainers.org/) — 2026
- [Northflank — Docker Build & Buildx Best Practices 2026](https://northflank.com/blog/docker-build-and-buildx-best-practices-for-optimized-builds) — 2026-01
- [Blacksmith — Multi-Stage Docker Builds](https://www.blacksmith.sh/blog/understanding-multi-stage-docker-builds) — 2024
- [OneUptime — Multi-Stage Docker Builds 2026](https://oneuptime.org/blog/post/2026-02-02-docker-multi-stage-builds/view) — 2026-02
- [Podman](https://podman.io/) — 2026
- [Podman GitHub (containers/podman)](https://github.com/containers/podman) — 2026
- [Distroless (GoogleContainerTools/distroless)](https://github.com/GoogleContainerTools/distroless) — 2026
- [CNCF](https://www.cncf.io/) — 2026