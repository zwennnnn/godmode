---
name: NGINX
category: infra-tools
status: researched
last-updated: 2026-07-30
sources:
  - https://nginx.org/
  - https://nginx.org/en/docs/
  - https://github.com/nginx/nginx
  - https://docs.nginx.com/
  - https://github.com/nginx-proxy/NGINX-Proxy-Manager
  - https://docs.nginx.com/nginx/admin-guide/
  - https://github.com/caddyserver/caddy
  - https://doc.traefik.io/traefik/
  - https://www.haproxy.org/
  - https://www.envoyproxy.io/
  - https://github.com/kubernetes/ingress-nginx
tags: [nginx, reverse-proxy, load-balancer, web-server, caddy, traefik, envoy, haproxy]
---

# NGINX

## One-liner

The high-performance HTTP server, reverse proxy, and load balancer that became the default for serving web traffic — the most deployed web server on the internet, the foundation of CDNs, and the Swiss army knife of HTTP.

## What It Is

[NGINX](https://nginx.org/) (pronounced "engine-x") is an open-source HTTP server, reverse proxy, load balancer, and mail proxy. Originally written by Igor Sysoev in 2004 to solve the C10K problem (handling 10K concurrent connections), it became the default for serving web traffic at scale.

The 2026 stack:

| Tool | Description |
|------|-------------|
| **[NGINX](https://nginx.org/) (open source)** | The original. |
| **NGINX Plus** | Commercial; advanced features + support. |
| **[NGINX Proxy Manager](https://github.com/nginx-proxy/NGINX-Proxy-Manager)** | Web UI for NGINX; easy self-host. |
| **[Caddy](https://github.com/caddyserver/caddy)** | Modern alternative; auto-HTTPS by default. |
| **[Traefik](https://doc.traefik.io/traefik/)** | Cloud-native reverse proxy; auto-discovery. |
| **[HAProxy](https://www.haproxy.org/)** | The original load balancer. |
| **[Envoy](https://www.envoyproxy.io/)** | Service proxy (CNCF); the data plane of Istio. |
| **[ingress-nginx](https://github.com/kubernetes/ingress-nginx)** | NGINX-based K8s ingress controller. |

Adoption: NGINX is **the most popular web server** (~33% of all websites with known server, per W3Techs). Used by Netflix, Cloudflare, WordPress.com, every major CDN.

## When To Use It

- **Serve static + dynamic HTTP** — NGINX.
- **Reverse proxy + load balancer** — NGINX.
- **TLS termination** — NGINX + Let's Encrypt.
- **Web server in front of Node / Python / Go** — NGINX.
- **K8s ingress controller** — ingress-nginx.

## When NOT To Use It

- **You want auto-HTTPS with zero config** — Caddy.
- **You need a cloud-native service mesh** — Envoy (via Istio) or Traefik.
- **Pure TCP load balancing** — HAProxy.

## Why It Matters in 2026

Three forces: (1) NGINX remains the default; (2) Cloud-native alternatives (Envoy, Traefik) compete for new workloads; (3) Caddy is the modern easy option.

Practitioner playbook: (1) Install NGINX (or Caddy); (2) Configure as reverse proxy in front of app; (3) Add TLS with Let's Encrypt (or Caddy's auto-HTTPS); (4) Configure rate limiting + security headers; (5) Use NGINX Proxy Manager for easy GUI.

## Scoring Matrix (0–100)

### NGINX (open source)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 22+ years; battle-tested at hyperscale. |
| Community | 100 | Massive. |
| Learning curve | 70 | Config is powerful but old-school. |
| Performance | 100 | Best-in-class HTTP server. |
| Cost | 100 | Free OSS. |
| DX | 80 | Config files are clear; not for beginners. |
| Production readiness | 100 | Battle-tested everywhere. |

### Caddy
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | Since 2015; v2 stable. |
| Community | 85 | Growing; loved by devs. |
| Learning curve | 95 | Auto-HTTPS = zero config. |
| Performance | 95 | Excellent. |
| Cost | 100 | Free. |
| DX | 100 | Best-in-class. |
| Production readiness | 90 | Used at scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Caddy** | You want auto-HTTPS; zero config. | You need complex NGINX features. |
| **Traefik** | Cloud-native; K8s; auto-discovery. | You want simple config. |
| **Envoy** | Service mesh; K8s; complex routing. | You want simple. |
| **HAProxy** | Pure TCP/L4 load balancing. | You need HTTP features. |
| **Apache httpd** | Legacy / .htaccess. | New project. |

## Sources

- [NGINX](https://nginx.org/) — 2026
- [NGINX Docs](https://nginx.org/en/docs/) — 2026
- [NGINX GitHub (nginx/nginx)](https://github.com/nginx/nginx) — 2026
- [NGINX Admin Guide (docs.nginx.com)](https://docs.nginx.com/) — 2026
- [NGINX Proxy Manager](https://github.com/nginx-proxy/NGINX-Proxy-Manager) — 2026
- [Caddy](https://github.com/caddyserver/caddy) — 2026
- [Traefik](https://doc.traefik.io/traefik/) — 2026
- [HAProxy](https://www.haproxy.org/) — 2026
- [Envoy Proxy](https://www.envoyproxy.io/) — 2026
- [Kubernetes ingress-nginx](https://github.com/kubernetes/ingress-nginx) — 2026