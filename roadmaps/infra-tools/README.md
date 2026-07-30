---
name: Infrastructure Tools
slug: infra-tools
source: https://roadmap.sh/terraform + https://roadmap.sh/linux + https://roadmap.sh/shell-bash + https://roadmap.sh/git-github
last-updated: 2026-07-30
tech-count: 6
status: in-progress
---

# Infrastructure Tools

> **Category:** The OS + tooling layer that every engineer needs — Git, Linux, shell scripting, reverse proxies, configuration management, and Terraform for declarative infra.
> **Sources:** [roadmap.sh/terraform](https://roadmap.sh/terraform), [roadmap.sh/linux](https://roadmap.sh/linux), [roadmap.sh/shell-bash](https://roadmap.sh/shell-bash), [roadmap.sh/git-github](https://roadmap.sh/git-github)

This roadmap covers the foundational infrastructure tools that complement the broader DevOps + Cloud topics in [`../devops-cloud/`](../devops-cloud/). Where that roadmap focuses on containers, K8s, IaC *as a discipline*, this one covers the OS-level + tooling-level basics.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Terraform (deep) | [terraform.md](terraform.md) | placeholder |
| 2 | Ansible (config management) | [ansible.md](ansible.md) | placeholder |
| 3 | Git and GitHub | [git-github.md](git-github.md) | placeholder |
| 4 | Linux | [linux.md](linux.md) | placeholder |
| 5 | Shell / Bash | [shell-bash.md](shell-bash.md) | placeholder |
| 6 | NGINX (reverse proxy / LB) | [nginx.md](nginx.md) | placeholder |

---

## Quick Decision Guide

### If you provision cloud infra

**[Terraform](terraform.md)** — declarative HCL; OpenTofu for OSS.

### If you configure servers at scale

**[Ansible](ansible.md)** — agentless; YAML playbooks over SSH.

### If you version code

**[Git + GitHub](git-github.md)** — the default; universal.

### If you deploy on Linux

**[Linux](linux.md)** — know the basics (processes, networking, FS).

### If you automate tasks

**[Shell / Bash](shell-bash.md)** — the scripting language of Unix.

### If you terminate TLS / reverse proxy

**[NGINX](nginx.md)** — the default; Caddy for auto-HTTPS.

---

## Cross-references

- For containers, K8s, IaC philosophy, see [`../devops-cloud/`](../devops-cloud/).
- For CI/CD, see [`../devops-cloud/ci-cd.md`](../devops-cloud/ci-cd.md).
- For observability, see [`../devops-cloud/observability.md`](../devops-cloud/observability.md).

---

## Build progress

**Phase 16 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.