---
name: Linux
category: infra-tools
status: researched
last-updated: 2026-07-30
sources:
  - https://www.kernel.org/
  - https://www.linux.org/
  - https://ubuntu.com/
  - https://www.debian.org/
  - https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
  - https://www.shellcheck.net/
  - https://linuxcommand.org/
  - https://tldp.org/
  - https://www.linuxfoundation.org/
  - https://systemd.io/
  - https://docs.kernel.org/
tags: [linux, kernel, ubuntu, debian, rhel, systemd, bash, shell, operating-system]
---

# Linux

## One-liner

The open-source operating system kernel powering everything from Android phones to the world's top supercomputers — the default OS for production servers, cloud VMs, and most developer environments.

## What It Is

[Linux](https://www.kernel.org/) is the open-source kernel created by Linus Torvalds in 1991. Combined with GNU userland + desktop / server packages, it forms the **GNU/Linux** operating system — packaged as **distributions** (distros): Ubuntu, Debian, RHEL, Fedora, Arch, Alpine, etc.

The 2026 stack:

| Component | Description |
|-----------|-------------|
| **Kernel** | [kernel.org](https://www.kernel.org/); >40M lines of code; ~3K+ contributors. |
| **Distros** | [Ubuntu](https://ubuntu.com/) (default server + desktop), [Debian](https://www.debian.org/) (rock-solid), RHEL/Fedora (enterprise), Alpine (containers), Arch (DIY). |
| **systemd** | Init system + service manager + login manager (default on most). |
| **Package managers** | apt (Debian / Ubuntu), dnf (RHEL/Fedora), pacman (Arch), apk (Alpine). |
| **Filesystem** | ext4, XFS, Btrfs, ZFS. |
| **Networking** | iptables / nftables; systemd-networkd; NetworkManager. |
| **Shell** | Bash (default), Zsh (popular), Fish (developer-friendly). |
| **Container base** | Most container images are Linux-based. |

Adoption: Linux powers **100% of the top 500 supercomputers**, **>90% of cloud VMs** (AWS Lambda, GCP, Azure all Linux), **>70% of smartphones** (Android), and **all major container platforms** (Docker, K8s).

## When To Use It

- **Any server / cloud workload** — Linux.
- **Containers** — Linux.
- **Mobile (Android)** — Linux.
- **Embedded / IoT** — Linux (or RTOS).
- **Dev environment** — Linux (WSL2 / macOS / Linux native).

## When NOT To Use It

- **Windows-only enterprise** (legacy).
- **macOS-specific apps** — Apple's platform.
- **Real-time critical embedded** — RTOS.

## Why It Matters in 2026

Three forces: (1) AI runs on Linux — every training cluster, every inference server; (2) Cloud is Linux — every hyperscaler; (3) Containers = Linux processes — Docker / K8s are Linux.

Practitioner playbook: (1) Linux basics: filesystem, processes, permissions, networking; (2) Shell scripting (see [shell-bash.md](shell-bash.md)); (3) Package management; (4) systemd services; (5) SSH + key auth; (6) Performance tuning basics.

## Scoring Matrix (0–100)

### Linux Kernel
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 35+ years; battle-tested. |
| Community | 100 | Massive; thousands of contributors. |
| Learning curve | 70 | Basics easy; advanced takes years. |
| Performance | 95 | Highly optimized; tunable. |
| Cost | 100 | Free OSS. |
| DX | 85 | Depends on distro; Ubuntu is excellent. |
| Production readiness | 100 | Universal. |

### Ubuntu
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | Since 2004; LTS every 2 years. |
| Community | 100 | Largest Linux community. |
| Learning curve | 95 | Easiest major distro. |
| Performance | 90 | Good for most use cases. |
| Cost | 100 | Free. |
| DX | 95 | Best for beginners + intermediates. |
| Production readiness | 100 | AWS / Azure / GCP default. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Windows Server** | Windows-only enterprise. | Most workloads. |
| **macOS** | Apple-specific. | Servers. |
| **BSD (FreeBSD)** | You want BSD license. | Linux ecosystem. |
| **ChromeOS** | Lightweight laptops. | Servers. |
| **Alpine Linux** | Containers; minimal. | Desktop use. |

## Sources

- [Linux Kernel (kernel.org)](https://www.kernel.org/) — 2026
- [The Linux Foundation](https://www.linux.org/) — 2026
- [Ubuntu](https://ubuntu.com/) — 2026
- [Debian](https://www.debian.org/) — 2026
- [Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) — 2026
- [ShellCheck](https://www.shellcheck.net/) — 2026
- [LinuxCommand.org](https://linuxcommand.org/) — 2026
- [The Linux Documentation Project](https://tldp.org/) — 2026
- [Linux Foundation](https://www.linuxfoundation.org/) — 2026
- [systemd](https://systemd.io/) — 2026
- [Kernel Docs](https://docs.kernel.org/) — 2026