---
name: Infrastructure as Code
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://developer.hashicorp.com/terraform
  - https://developer.hashicorp.com/terraform/docs
  - https://developer.hashicorp.com/terraform/intro
  - https://github.com/hashicorp/terraform
  - https://opentofu.org/
  - https://github.com/opentofu/opentofu
  - https://www.pulumi.com/
  - https://github.com/pulumi/pulumi
  - https://www.pulumi.com/docs/
  - https://www.ansible.com/
  - https://github.com/ansible/ansible
  - https://www.cdktf.io/
  - https://developer.hashicorp.com/packer
  - https://github.com/hashicorp/packer
  - https://github.com/aws-cloudformation/cfn-lint
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
  - https://spacelift.io/blog/terraform-vs-pulumi
tags: [terraform, opentofu, pulumi, ansible, iac, devops, infrastructure, cloudformation]
---

# Infrastructure as Code (Terraform / Pulumi / Ansible)

## One-liner

Defining your infrastructure — servers, networks, databases, IAM — in versioned, reviewable code instead of clicking through a cloud console.

## What It Is

Infrastructure as Code (IaC) means your cloud resources (VMs, databases, networking, IAM, S3 buckets, DNS) live in declarative config files, not in a cloud console. The benefits:

- **Reproducibility** — `terraform apply` produces the same result every time.
- **Version control** — see what changed, when, and why.
- **Code review** — PRs for infrastructure changes.
- **Disaster recovery** — rebuild your entire stack from code.
- **Documentation** — the code IS the docs.

The 2026 tool landscape:

| Tool | Language | Notes |
|------|----------|-------|
| **[Terraform](https://developer.hashicorp.com/terraform)** | HCL (HashiCorp Configuration Language) | The standard; ~70% market share; massive provider ecosystem. |
| **[OpenTofu](https://opentofu.org/) | HCL | Open-source fork of Terraform (after HashiCorp's license change to BSL in 2023); drop-in compatible. |
| **[Pulumi](https://www.pulumi.com/)** | TS / Python / Go / .NET / Java | Real programming languages instead of HCL; better for complex logic. |
| **[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)** | YAML / JSON | AWS-only; tightly integrated; verbose. |
| **[Ansible](https://www.ansible.com/)** | YAML (playbooks) | Configuration management + orchestration; agentless; great for VM bootstrap. |
| **[Packer](https://developer.hashicorp.com/packer)** | HCL / JSON | Build golden VM/container images; pairs with Terraform. |
| **[CDK for Terraform (CDKTF)](https://www.cdktf.io/)** | TS / Python / Go / Java | CDK-style use of Terraform; synth to HCL. |
| **Crossplane** | YAML / Go | Kubernetes-native IaC; manages cloud resources via K8s CRDs. |

### Terraform / OpenTofu
- **Workflow**: `init` → `plan` (preview) → `apply`.
- **State file**: tracks real-world resources; stored locally or remotely (S3, GCS, Terraform Cloud).
- **Modules**: reusable infrastructure packages.
- **Providers**: AWS, GCP, Azure, Kubernetes, GitHub, Cloudflare, 3000+.
- **OpenTofu** (forked 2023) is the open-source continuation; Terraform is now BSL-licensed (source-available, not OSI-open).

### Pulumi
- **Real programming languages** (TS, Python, Go, .NET, Java) → IDE support, type checking, tests, loops, conditionals — all native.
- **State**: Pulumi Cloud (managed) or self-hosted (S3 / Azure Blob / local).
- **Pulumi + K8s**: native K8s provider; crosswalk for AWS.

### Ansible
- **Agentless** (uses SSH / WinRM).
- **Playbooks** in YAML; declarative but with procedural capability.
- **Roles** for reusability; **collections** for packaging.
- **Use case**: configuration management, software provisioning, app deployment. Complements Terraform — Terraform creates infra, Ansible configures it.

## When To Use It

### Terraform / OpenTofu
- **Default for any multi-cloud or single-cloud IaC** in 2026.
- **You want the largest provider ecosystem.**
- **You prefer declarative config** over code.
- **OpenTofu over Terraform** if you care about open-source governance.

### Pulumi
- **You want to write infra in TS / Python / Go** (testable, IDE-supported, loops/conditionals).
- **You're a software team** that prefers real languages over DSLs.
- **You need complex logic** (e.g., conditional resource creation based on data).

### Ansible
- **VM / bare-metal configuration management** (not cloud provisioning).
- **Application deployment** (Ansible playbooks can deploy apps after Terraform creates infra).
- **Network device configuration** (Cisco, Juniper — Ansible is the standard).

### CloudFormation
- **You're all-in on AWS** and prefer their native tooling.
- **You need AWS-specific features** no other tool exposes.

### CDKTF / Crossplane
- **CDKTF**: you're already in CDK-land for AWS.
- **Crossplane**: you're a platform team using K8s as your control plane for everything.

## When NOT To Use It

### Terraform / OpenTofu
- **You need complex logic** — Pulumi's real languages are easier.
- **You want first-class testing** — Pulumi's TS/Python is more testable.

### Pulumi
- **Your team doesn't know TS / Python / Go** — Terraform's HCL is easier to learn.
- **You depend on a niche Terraform provider** that Pulumi doesn't have a mapping for.

### Ansible
- **Cloud provisioning** — Terraform is the standard.
- **Stateful orchestration at scale** — Ansible's stateless model has limits.

### CloudFormation
- **Multi-cloud** — Terraform / OpenTofu.

## Why It Matters in 2026

Three forces:

1. **OpenTofu matured into the open-source default.** After HashiCorp's license change to BSL in 2023, OpenTofu became the actively-developed open-source Terraform. Many enterprises migrated; new projects default to OpenTofu for open governance.
2. **Pulumi + AI-assisted IaC is the new killer combo.** Real languages + AI code generation = you describe the infra in comments, the model writes the Pulumi code. This is meaningfully better than asking a model to write HCL.
3. **Policy-as-code matured.** OPA (Open Policy Agent) + Sentinel + Conftest + Pulumi CrossGuard let you enforce "no public S3 buckets" / "all EC2 must have tags" automatically in CI.

Practitioner defaults in 2026:
- **Greenfield**: **OpenTofu** (open-source) or **Terraform** (HashiCorp ecosystem / Terraform Cloud).
- **TS-heavy team**: **Pulumi**.
- **VM config**: **Ansible** (after Terraform).
- **AWS-only enterprise**: CloudFormation or CDKTF.
- **State backend**: S3 + DynamoDB lock (AWS), GCS (GCP), or Terraform Cloud / Pulumi Cloud (managed).

## Scoring Matrix (0–100)

### Terraform / OpenTofu
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | Terraform 11+ years; OpenTofu 2+ years; both battle-tested. |
| Community | 95 | Largest IaC ecosystem; 3000+ providers; thousands of modules. |
| Learning curve | 60 | HCL is easy to start; state management + module design + drift detection takes months. |
| Performance | 80 | Plan/apply can be slow on huge stacks; improvements every release. |
| Cost | 85 | OSS free; Terraform Cloud paid (or self-host). |
| DX | 75 | HCL is less ergonomic than real languages; but excellent tooling (terraform fmt, validate). |
| Production readiness | 95 | Standard. |

### Pulumi
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 75 | 7+ years; smaller provider coverage than Terraform. |
| Community | 75 | Growing fast; loved by TS devs. |
| Learning curve | 70 | Easier if you know TS/Python; harder if not. |
| Performance | 85 | Fast; state operations efficient. |
| Cost | 75 | OSS free; Pulumi Cloud paid for teams. |
| DX | 90 | Real languages = real IDE support, testing, refactoring. |
| Production readiness | 90 | Used by many enterprises; Pulumi Cloud is solid. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **ClickOps (console clicking)** | Truly throwaway. | Anything you care about reproducibility for. |
| **Pulumi** | You want real languages; complex logic; AI-assisted. | You want the largest provider ecosystem. |
| **CloudFormation** | AWS-only; need AWS-specific features. | Multi-cloud. |
| **Crossplane** | K8s as your control plane; you want K8s-native APIs. | You don't already run K8s. |
| **AWS CDK** | You're on AWS; you love CDK. | Multi-cloud. |
| **Bicep / ARM templates** | Azure-only. | Multi-cloud. |
| **Chef / Puppet** | Legacy config management shops. | New projects — Ansible is the default. |

## Sources

- [Terraform Official Site](https://developer.hashicorp.com/terraform) — 2026
- [Terraform Docs](https://developer.hashicorp.com/terraform/docs) — 2026
- [Terraform Intro](https://developer.hashicorp.com/terraform/intro) — 2026
- [Terraform GitHub (hashicorp/terraform)](https://github.com/hashicorp/terraform) — 2026
- [OpenTofu](https://opentofu.org/) — 2026
- [OpenTofu GitHub (opentofu/opentofu)](https://github.com/opentofu/opentofu) — 2026
- [Pulumi](https://www.pulumi.com/) — 2026
- [Pulumi GitHub (pulumi/pulumi)](https://github.com/pulumi/pulumi) — 2026
- [Pulumi Docs](https://www.pulumi.com/docs/) — 2026
- [Ansible](https://www.ansible.com/) — 2026
- [Ansible GitHub (ansible/ansible)](https://github.com/ansible/ansible) — 2026
- [CDK for Terraform](https://www.cdktf.io/) — 2026
- [Packer](https://developer.hashicorp.com/packer) — 2026
- [Packer GitHub (hashicorp/packer)](https://github.com/hashicorp/packer) — 2026
- [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) — 2026
- [Spacelift — Terraform vs Pulumi](https://spacelift.io/blog/terraform-vs-pulumi) — 2026