---
name: Secrets Management
category: devops-cloud
status: researched
last-updated: 2026-07-30
sources:
  - https://www.vaultproject.io/
  - https://developer.hashicorp.com/vault
  - https://github.com/hashicorp/vault
  - https://docs.aws.amazon.com/secretsmanager/
  - https://aws.amazon.com/secrets-manager/
  - https://cloud.google.com/secret-manager
  - https://learn.microsoft.com/en-us/azure/key-vault/
  - https://docs.doppler.com/
  - https://www.doppler.com/
  -https://infisical.com/
  - https://github.com/Infisical/infisical
  - https://github.com/bitnami-labs/sealed-secrets
  - https://www.sops.sh/
  - https://1password.com/
  - https://github.com/FiloSottile/age
  - https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
tags: [secrets, vault, secrets-manager, doppler, infisical, sops, sealed-secrets, devops, security]
---

# Secrets Management (Vault / AWS Secrets Manager / Doppler / Infisical)

## One-liner

How you store, distribute, rotate, and audit the API keys, DB passwords, certificates, and tokens your services need — without putting them in `.env` files in Git.

## What It Is

Secrets management is the discipline of keeping credentials out of source code, environment files in git, and unencrypted CI logs. Every serious production system needs:

- **A secret store** — encrypted-at-rest, access-controlled, auditable.
- **A distribution mechanism** — services fetch secrets at runtime, not at build time.
- **Rotation** — secrets change regularly without downtime.
- **Audit** — every access is logged.

The 2026 landscape:

### Self-hosted / OSS

| Tool | Notes |
|------|-------|
| **[HashiCorp Vault](https://www.vaultproject.io/)** | The standard; secret storage + dynamic secrets + leasing + PKI + transit encryption. Complex but powerful. |
| **[Infisical](https://infisical.com/)** | Modern OSS alternative to Vault; great DX; simpler to operate. |
| **SOPS (Mozilla)** | Encrypts YAML/JSON files in git; pairs with cloud KMS. |
| **Sealed Secrets (Bitnami)** | Kubernetes-specific; encrypted secrets in git. |

### Managed / cloud-native

| Tool | Notes |
|------|-------|
| **[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)** | AWS-native; automatic rotation for RDS / Redshift; tight IAM integration. |
| **[Google Secret Manager](https://cloud.google.com/secret-manager)** | GCP-native; versioning; IAM. |
| **[Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/)** | Azure-native; HSM-backed; certificates + keys + secrets. |
| **[Doppler](https://www.doppler.com/)** | Developer-first; sync across envs; loved by dev teams. |
| **1Password** | Great for team secrets + personal; CLI integrations. |
| **Aged / age** | Simple file encryption for small setups. |

## When To Use It

### HashiCorp Vault
- **Enterprise / regulated industries** with strict secret / PKI / dynamic-secret needs.
- **You need dynamic secrets** (Vault generates DB credentials on demand with TTL).
- **You have ops capacity** to run Vault HA clusters.

### AWS Secrets Manager / GCP Secret Manager / Azure Key Vault
- **You're on that cloud**; default for service-to-service auth.
- **You want managed; no ops.**

### Doppler / Infisical
- **Small-to-medium teams** that want dev-first DX.
- **You sync secrets across dev/staging/prod** with audit trail.

### SOPS / Sealed Secrets
- **You want secrets in git** (encrypted) — useful for K8s GitOps workflows.
- **You want a simple file-based approach.**

## When NOT To Use It

### Vault
- **You're a small team.** Operational complexity is real.
- **You don't have a secret-heavy workload.**

### Cloud-native secret managers
- **Multi-cloud.** You'd need one per cloud.
- **You want a unified developer experience.**

### Doppler / Infisical
- **You're heavily regulated** with on-prem requirements (self-host Infisical then).

### SOPS / Sealed Secrets
- **You need dynamic secrets** (these are static encrypted blobs).

## Why It Matters in 2026

Three forces:

1. **Secret leaks are the #1 breach vector.** Per Verizon DBIR, stolen credentials drive most breaches. Hard-coded secrets in repos / Slack / config files = breach waiting to happen.
2. **Cloud IAM matured.** Every cloud now has first-class secret managers; OIDC for short-lived credentials means you don't need long-lived API keys.
3. **Dev-first secret tools (Doppler, Infisical) closed the DX gap with Vault.** Small teams no longer have an excuse for `.env` files in git.

Practitioner defaults in 2026:
- **AWS / GCP / Azure** → cloud-native secret manager.
- **Small team / multi-cloud** → Doppler or Infisical.
- **Enterprise / regulated** → Vault or cloud-native + Vault.
- **K8s GitOps** → Sealed Secrets or External Secrets Operator + cloud manager.
- **Local dev** → Doppler / Infisical CLI + `.env.local` (gitignored).

## Scoring Matrix (0–100)

### Vault
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 9+ years old; the enterprise standard. |
| Community | 90 | Large; many integrations. |
| Learning curve | 45 | Steep; policies, tokens, leases, auth methods. |
| Performance | 85 | Excellent; HA clusters scale. |
| Cost | 70 | OSS free; enterprise + managed options. |
| DX | 65 | Powerful but complex; UI is dated. |
| Production readiness | 95 | Battle-tested at every scale. |

### Doppler
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 75 | 5+ years; growing fast. |
| Community | 80 | Loved by devs; growing. |
| Learning curve | 90 | Easy to start; intuitive UX. |
| Performance | 90 | Fast; sync is instant. |
| Cost | 80 | Generous free tier; paid is reasonable. |
| DX | 95 | Best-in-class dev DX. |
| Production readiness | 85 | Used at many startups; younger than Vault. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **`.env` in git** | Never (still common in tutorials). | Always use a real secret manager. |
| **HashiCorp Vault** | Enterprise; dynamic secrets; PKI. | Small teams — too complex. |
| **Cloud-native secret managers** | Single-cloud deployments. | Multi-cloud. |
| **Doppler / Infisical** | Dev-first; small-to-medium teams; multi-cloud. | Massive enterprise scale. |
| **SOPS / Sealed Secrets** | Git-based secret workflows; K8s GitOps. | Dynamic secrets; audit-heavy. |
| **1Password CLI** | Teams already using 1Password for personal / team passwords. | Service-to-service at scale. |
| **CyberArk / BeyondTrust** | PAM-heavy enterprise. | Most teams — overkill. |

## Sources

- [HashiCorp Vault](https://www.vaultproject.io/) — 2026
- [Vault Developer Docs](https://developer.hashicorp.com/vault) — 2026
- [Vault GitHub (hashicorp/vault)](https://github.com/hashicorp/vault) — 2026
- [AWS Secrets Manager Docs](https://docs.aws.amazon.com/secretsmanager/) — 2026
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) — 2026
- [Google Secret Manager](https://cloud.google.com/secret-manager) — 2026
- [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/) — 2026
- [Doppler Docs](https://docs.doppler.com/) — 2026
- [Doppler](https://www.doppler.com/) — 2026
- [Infisical](https://infisical.com/) — 2026
- [Infisical GitHub (Infisical/infisical)](https://github.com/Infisical/infisical) — 2026
- [Sealed Secrets (Bitnami Labs)](https://github.com/bitnami-labs/sealed-secrets) — 2026
- [SOPS](https://www.sops.sh/) — 2026
- [1Password](https://1password.com/) — 2026
- [age (FiloSottile/age)](https://github.com/FiloSottile/age) — 2026
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — 2026