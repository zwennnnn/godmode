---
name: Terraform
category: infra-tools
status: researched
last-updated: 2026-07-30
sources:
  - https://developer.hashicorp.com/terraform
  - https://developer.hashicorp.com/terraform/docs
  - https://developer.hashicorp.com/terraform/intro
  - https://github.com/hashicorp/terraform
  - https://opentofu.org/
  - https://github.com/opentofu/opentofu
  - https://developer.hashicorp.com/terraform/language
  - https://registry.terraform.io/
  - https://developer.hashicorp.com/terraform/cloud
  - https://www.terraform-best-practices.com/
  - https://github.com/hashicorp/tfenv
tags: [terraform, opentofu, iac, hcl, infrastructure-as-code, devops, aws, gcp, azure]
---

# Terraform

## One-liner

HashiCorp's declarative infrastructure-as-code tool (HCL) — the standard for provisioning cloud infrastructure as versioned code; OpenTofu is the open-source fork after HashiCorp's 2023 license change.

## What It Is

[Terraform](https://developer.hashicorp.com/terraform) is HashiCorp's infrastructure-as-code tool that lets you define cloud + on-prem resources in declarative HCL configuration files, then provision them via `terraform init / plan / apply`. The state file tracks real-world resources; modules enable reuse.

The 2026 ecosystem:

| Component | Description |
|-----------|-------------|
| **Terraform** | HashiCorp's tool; BSL-licensed since 2023. |
| **[OpenTofu](https://opentofu.org/)** | OSS fork; same APIs; actively developed by Linux Foundation. |
| **Providers** | AWS, GCP, Azure, Kubernetes, GitHub, Cloudflare, 3000+. |
| **Modules** | Reusable infra packages (Terraform Registry). |
| **State** | Local or remote (S3, GCS, Terraform Cloud). |
| **Terraform Cloud** | Managed SaaS (HashiCorp); Atlantis / Spacelift for self-host CI. |
| **CDKTF** | Use TS / Python / Go / Java to compose Terraform. |
| **Terraform MCP** | 2025+; MCP servers for Terraform operations. |

Adoption: Terraform is the **#1 IaC tool** by usage. Every major cloud + every CNCF project supports it.

## When To Use It

- **Default for any multi-cloud or single-cloud IaC** in 2026.
- **You want the largest provider ecosystem.**
- **You prefer declarative config** over code.
- **OpenTofu over Terraform** if you care about open-source governance.

## When NOT To Use It

- **You need complex logic** — Pulumi's real languages are easier.
- **You want first-class testing** — Pulumi's TS / Python is more testable.

## Why It Matters in 2026

Three forces: (1) OpenTofu 1.0 (2024) stabilized the OSS fork; (2) Provider ecosystem matured; (3) Terraform + AI agents = generate HCL via prompts + Claude Code.

Practitioner defaults: **OpenTofu** for OSS / cost; **Terraform Cloud** for enterprise; modules for reuse; remote state in S3 + DynamoDB lock; pre-commit hooks (`tflint`, `tfsec`, `checkov`).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 11+ years old; battle-tested. |
| Community | 95 | Largest IaC ecosystem; 3000+ providers. |
| Learning curve | 60 | HCL easy; state + modules + drift take months. |
| Performance | 80 | Plan/apply slow on huge stacks. |
| Cost | 85 | OSS free; Terraform Cloud paid. |
| DX | 75 | HCL less ergonomic than real languages. |
| Production readiness | 95 | Industry standard. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **OpenTofu** | OSS / governance. | Vendor ecosystem matters. |
| **Pulumi** | Real languages; complex logic. | You want largest ecosystem. |
| **Pulumi Crossplane** | K8s as control plane. | You don't run K8s. |
| **AWS CDK / CDKTF** | You're already in CDK. | Multi-cloud. |

## Sources

- [Terraform](https://developer.hashicorp.com/terraform) — 2026
- [Terraform Docs](https://developer.hashicorp.com/terraform/docs) — 2026
- [Terraform Intro](https://developer.hashicorp.com/terraform/intro) — 2026
- [Terraform GitHub (hashicorp/terraform)](https://github.com/hashicorp/terraform) — 2026
- [OpenTofu](https://opentofu.org/) — 2026
- [OpenTofu GitHub (opentofu/opentofu)](https://github.com/opentofu/opentofu) — 2026
- [Terraform Language](https://developer.hashicorp.com/terraform/language) — 2026
- [Terraform Registry](https://registry.terraform.io/) — 2026
- [Terraform Cloud](https://developer.hashicorp.com/terraform/cloud) — 2026
- [Terraform Best Practices](https://www.terraform-best-practices.com/) — 2026
- [tfenv (Terraform version manager)](https://github.com/hashicorp/tfenv) — 2026