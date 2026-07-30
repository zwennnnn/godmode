---
name: Ansible
category: infra-tools
status: researched
last-updated: 2026-07-30
sources:
  - https://www.ansible.com/
  - https://docs.ansible.com/
  - https://github.com/ansible/ansible
  - https://docs.ansible.com/ansible/latest/index.html
  - https://docs.ansible.com/ansible/latest/inventory_guide/index.html
  - https://docs.ansible.com/ansible/latest/playbook_guide/index.html
  - https://docs.ansible.com/ansible/latest/collections_guide.html
  - https://galaxy.ansible.com/
  - https://www.ansible.com/products/automation-platform
  - https://docs.ansible.com/ansible/latest/dev_guide/index.html
tags: [ansible, configuration-management, iac, yaml, ssh, ansible-automation-platform, devops]
---

# Ansible

## One-liner

Red Hat's agentless configuration management + orchestration tool — YAML playbooks over SSH that configure servers, deploy apps, and orchestrate workflows; the standard for VM + bare-metal provisioning.

## What It Is

[Ansible](https://www.ansible.com/) is an open-source automation tool for configuration management, application deployment, and task automation. It uses **agentless** architecture (SSH / WinRM) + declarative **YAML playbooks**.

The 2026 baseline is **Ansible Core 2.18+**:

- **Playbooks** — YAML; declarative + procedural.
- **Roles** — reusable structure (tasks, handlers, files, templates, vars).
- **Collections** — packaged Ansible content (e.g. `community.postgresql`).
- **Ansible Galaxy** — community hub for roles + collections.
- **Ansible Automation Platform (AAP)** — paid enterprise; controller + mesh + insights.
- **Execution environments** — containerized Ansible runtimes.
- **Ansible Lightspeed** — AI assistant (IBM watsonx); generates playbooks from natural language.

Adoption: Ansible is the **standard for agentless config management**. Used by Red Hat customers, every Fortune 500 with VMs / bare metal, plus cloud-managed nodes via SSH.

## When To Use It

- **VM / bare-metal configuration management** — agentless SSH wins.
- **Application deployment** — Ansible playbooks.
- **Network device automation** — Cisco / Juniper / Arista support.
- **Orchestration across heterogeneous environments** — mix of Linux + Windows + network devices.
- **You want YAML not a DSL** — Ansible's strength.

## When NOT To Use It

- **Cloud-native / K8s-only** — Helm / Argo / Terraform better.
- **You want agent-based** — Puppet / Chef / Salt.
- **Windows-first fleet** — Ansible works but PowerShell DSC is more native.

## Why It Matters in 2026

Three forces: (1) Ansible Automation Platform is the enterprise standard; (2) Ansible Lightspeed brings AI-generated playbooks; (3) Collections ecosystem matured — every major vendor publishes an Ansible Collection.

Practitioner playbook: (1) Start with `ansible --version`; (2) Write a playbook; (3) Refactor into roles; (4) Use collections from Galaxy; (5) Pin to specific versions; (6) Test with Molecule.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 13+ years old; battle-tested. |
| Community | 90 | Massive; Ansible Galaxy. |
| Learning curve | 70 | YAML easy; Jinja2 + vars + roles take study. |
| Performance | 75 | Sequential by default; forks scale; can be slow at scale. |
| Cost | 90 | Core free; AAP paid. |
| DX | 80 | Decent; linting + testing tools exist. |
| Production readiness | 95 | Used everywhere. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Puppet / Chef** | Agent-based; enterprise. | You want agentless. |
| **Salt** | You want agent + agentless. | Mature ecosystem matters. |
| **Terraform** | Cloud provisioning. | Server config / app deploy. |
| **Helm / Argo** | K8s-native. | VMs / bare-metal. |
| **Bash scripts** | Tiny tasks. | Multi-server orchestration. |

## Sources

- [Ansible](https://www.ansible.com/) — 2026
- [Ansible Docs](https://docs.ansible.com/) — 2026
- [Ansible GitHub (ansible/ansible)](https://github.com/ansible/ansible) — 2026
- [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html) — 2026
- [Ansible Inventory Guide](https://docs.ansible.com/ansible/latest/inventory_guide/index.html) — 2026
- [Ansible Playbook Guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html) — 2026
- [Ansible Collections Guide](https://docs.ansible.com/ansible/latest/collections_guide.html) — 2026
- [Ansible Galaxy](https://galaxy.ansible.com/) — 2026
- [Ansible Automation Platform](https://www.ansible.com/products/automation-platform) — 2026
- [Ansible Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html) — 2026