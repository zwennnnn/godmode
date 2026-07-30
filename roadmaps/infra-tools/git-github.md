---
name: Git and GitHub
category: infra-tools
status: researched
last-updated: 2026-07-30
sources:
  - https://git-scm.com/
  - https://git-scm.com/doc
  - https://github.com/
  - https://docs.github.com/
  - https://docs.github.com/en/get-started
  - https://docs.github.com/en/repositories
  - https://docs.github.com/en/actions
  - https://cli.github.com/
  - https://docs.github.com/en/copilot
  - https://docs.github.com/en/pull-requests
  - https://learngitbranching.js.org/
tags: [git, github, version-control, pull-request, actions, copilot, cli, gitlab, devops]
---

# Git and GitHub

## One-liner

The distributed version control system + the world's largest code-hosting platform — Linus Torvalds' Git (2005) + GitHub (2008) — the default for every modern software project.

## What It Is

[Git](https://git-scm.com/) is the distributed version control system created by Linus Torvalds in 2005 for Linux kernel development. [GitHub](https://github.com/) is the cloud platform that hosts Git repositories + adds collaboration features.

The 2026 stack:

| Tool | Description |
|------|-------------|
| **Git** | CLI; the underlying VCS. |
| **[GitHub](https://github.com/)** | The dominant host (370M+ users). |
| **GitHub Actions** | CI/CD built in (see [`../devops-cloud/ci-cd.md`](../devops-cloud/ci-cd.md)). |
| **GitHub CLI (`gh`)** | Terminal workflow. |
| **GitHub Copilot** | AI pair programmer. |
| **GitHub Codespaces** | Cloud dev environments. |
| **GitHub Issues + Projects** | Lightweight PM. |
| **GitHub Actions + MCP** | Agent-driven CI. |
| **GitLab** | Open-source alternative; integrated CI/CD. |
| **Bitbucket** | Atlassian's Git host. |

Adoption: Git is **universal** (every developer uses it). GitHub is the dominant host (~370M users, ~90%+ of OSS). GitLab is #2 in enterprise.

## When To Use It

- **Any project** — period.
- **GitHub Actions for CI/CD** — integrated.
- **GitHub Copilot** for AI pair programming.
- **GitHub Codespaces** for cloud dev environments.

## When NOT To Use It

- **You want fully integrated PM + design + code** — Jira + Confluence + Git.
- **You want self-hosted only** — Gitea or GitLab Self-Managed.
- **You want a non-Git VCS** — rare.

## Why It Matters in 2026

Three forces: (1) GitHub Actions became the default for CI/CD; (2) Copilot + AI agents = GitHub as the AI-coding hub; (3) Codespaces + cloud dev environments normalized.

Practitioner playbook: (1) Git CLI basics (init / add / commit / push / pull / branch / merge); (2) PR workflow; (3) GitHub Actions for CI; (4) GitHub Copilot for AI; (5) Conventional Commits; (6) Trunk-based development for fast teams.

## Scoring Matrix (0–100)

### Git
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 20+ years; battle-tested. |
| Community | 100 | Universal. |
| Learning curve | 75 | Basics easy; rebasing / submodules / bisect take study. |
| Performance | 95 | Fast; scales to huge repos. |
| Cost | 100 | Free OSS. |
| DX | 90 | CLI is great; GUI clients available. |
| Production readiness | 100 | Universal. |

### GitHub
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 17+ years; the standard. |
| Community | 100 | Massive. |
| Learning curve | 80 | Easy; advanced features take study. |
| Performance | 90 | Fast UI; Actions scale. |
| Cost | 80 | Free for OSS; paid for private teams. |
| DX | 95 | Best-in-class. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **GitLab** | Open-source + integrated CI/CD. | You want largest ecosystem. |
| **Bitbucket** | Atlassian shop (Jira). | Modern DX matters. |
| **Gitea / Forgejo** | Self-hosted lightweight. | You want managed. |
| **SVN / Mercurial** | Legacy. | New project. |
| **Perforce Helix** | Massive monorepos / game dev. | Most software. |

## Sources

- [Git](https://git-scm.com/) — 2026
- [Git Documentation](https://git-scm.com/doc) — 2026
- [GitHub](https://github.com/) — 2026
- [GitHub Docs](https://docs.github.com/) — 2026
- [GitHub Get Started](https://docs.github.com/en/get-started) — 2026
- [GitHub Repositories](https://docs.github.com/en/repositories) — 2026
- [GitHub Actions](https://docs.github.com/en/actions) — 2026
- [GitHub CLI](https://cli.github.com/) — 2026
- [GitHub Copilot](https://docs.github.com/en/copilot) — 2026
- [GitHub Pull Requests](https://docs.github.com/en/pull-requests) — 2026
- [Learn Git Branching](https://learngitbranching.js.org/) — 2026