---
name: Code Review
category: qa-testing
status: researched
last-updated: 2026-07-30
sources:
  - https://google.github.io/eng-practices/review/
  - https://martinfowler.com/articles/codeAsDocumentation.html
  - https://www.pullrequest.com/blog/code-review-best-practices
  - https://roadmap.sh/code-review
  - https://conventionalcomments.org/
  - https://en.wikipedia.org/wiki/Code_review
  - https://smartbear.com/learn/code-review/
  - https://www.codereviewacademy.com/
  - https://github.com/features/code-review
  - https://docs.github.com/en/pull-requests
tags: [code-review, pull-request, conventional-comments, code-quality, engineering-culture]
---

# Code Review

## One-liner

The practice of having peers examine code changes before merge — the highest-leverage quality + mentorship practice in software engineering; Google's research shows it catches defects early and spreads knowledge across teams.

## What It Is

[Code review](https://en.wikipedia.org/wiki/Code_review) is the systematic examination of code changes by peers before they are merged into a shared codebase. Done well, it catches bugs early, shares knowledge, enforces standards, and mentors junior engineers.

The 2026 best practices (per [Google Engineering Practices](https://google.github.io/eng-practices/review/), [Conventional Comments](https://conventionalcomments.org/)):

| Principle | Description |
|-----------|-------------|
| **Fast** | Review within 24h; unblocks teammates. |
| **Small PRs** | <400 lines; easier to review thoroughly. |
| **Constructive** | Suggest + explain; never just criticize. |
| **LGTM with comments** | Approve + leave learning notes. |
| **Code as documentation** | PRs explain *why*; not just *what*. |
| **Automated checks first** | CI runs lint/test/security; human reviews design. |
| **Conventional Comments** | `praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:` — labeled feedback. |
| **Self-review** | Author reviews their own diff before requesting review. |
| **Two-reviewer rule** | At least 2 approvals for sensitive code. |
| **Reviewer rotation** | Spread knowledge; don't bottleneck on one reviewer. |

Adoption: Code review is universal in professional engineering. PRs + reviews are the default workflow at every serious company.

## When To Use It

- **Every PR** — period.
- **Sensitive code** — security, payments, infra — extra rigor.
- **Junior engineers** — mentorship opportunity.

## When NOT To Use It

- **Trivial changes** — typos, one-line.
- **Generated code** — review the generator, not the output.

## Why It Matters in 2026

Three forces: (1) AI-generated code makes review more important (humans verify AI output); (2) PR workflow is universal; (3) Conventional Comments + structured review reduce friction.

Practitioner playbook: (1) Small PRs; (2) Self-review first; (3) Conventional Comments; (4) Fast turnaround (24h); (5) Focus on design + correctness; let CI catch style + tests; (6) Be kind.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years. |
| Community | 100 | Universal; well-studied. |
| Learning curve | 70 | Easy to start; nuanced takes years. |
| Performance | N/A | Practice. |
| Cost | 95 | Free (just time). |
| DX | 80 | GitHub / GitLab PR UX is excellent. |
| Production readiness | 100 | Every team. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No code review** | Throwaway. | Production. |
| **Pair programming** | Real-time; complex code. | Async teams. |
| **Mob programming** | Critical code. | Routine work. |
| **Formal inspections** | Safety-critical. | Most apps. |
| **AI code review** | Catch patterns. | Design judgment. |

## Sources

- [Google Engineering Practices — Code Review](https://google.github.io/eng-practices/review/) — 2026
- [Martin Fowler — Code as Documentation](https://martinfowler.com/articles/codeAsDocumentation.html) — 2026
- [PullRequest.com — Code Review Best Practices](https://www.pullrequest.com/blog/code-review-best-practices) — 2026
- [roadmap.sh/code-review](https://roadmap.sh/code-review) — 2026
- [Conventional Comments](https://conventionalcomments.org/) — 2026
- [Wikipedia — Code Review](https://en.wikipedia.org/wiki/Code_review) — 2026
- [SmartBear — Code Review](https://smartbear.com/learn/code-review/) — 2026
- [Code Review Academy](https://www.codereviewacademy.com/) — 2026
- [GitHub Code Review](https://github.com/features/code-review) — 2026
- [GitHub Pull Requests Docs](https://docs.github.com/en/pull-requests) — 2026