---
name: Game Development
slug: game-development
source: https://roadmap.sh/game-developer + https://roadmap.sh/server-side-game-developer
last-updated: 2026-07-30
tech-count: 6
status: in-progress
---

# Game Development

> **Category:** Technologies and disciplines for building video games — engines, design principles, multiplayer networking, asset pipelines, and the business of shipping games.
> **Sources:** [roadmap.sh/game-developer](https://roadmap.sh/game-developer), [roadmap.sh/server-side-game-developer](https://roadmap.sh/server-side-game-developer)

This roadmap covers the modern game development stack — Unity / Unreal / Godot engines, game design fundamentals, multiplayer networking, and the production practices that ship games in 2026.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Game Developer (overview) | [game-developer.md](game-developer.md) | placeholder |
| 2 | Unity | [unity.md](unity.md) | placeholder |
| 3 | Unreal Engine | [unreal-engine.md](unreal-engine.md) | placeholder |
| 4 | Godot | [godot.md](godot.md) | placeholder |
| 5 | Game Design (mechanics, loops, balance) | [game-design.md](game-design.md) | placeholder |
| 6 | Multiplayer Game Development | [multiplayer-game-development.md](multiplayer-game-development.md) | placeholder |

---

## Quick Decision Guide

### If you're making a mobile / casual / 2D game

**[Unity](unity.md)** is the default (asset store + mobile tooling). Or **[Godot](godot.md)** if OSS / lightweight.

### If you're making a AAA / 3D / cinematic game

**[Unreal Engine](unreal-engine.md)** (Nanite + Lumen = photorealistic in real time).

### If you're indie / open-source / cross-platform

**[Godot 4](godot.md)** — MIT, fast, growing community.

### If you're making a multiplayer game

See [multiplayer-game-development.md](multiplayer-game-development.md) — Photon / PlayFab / Nakama / Engine-specific SDKs.

### If you want to learn game design fundamentals

Every game developer needs [game-design.md](game-design.md) — MDA framework, player types, mechanics.

### If you're just starting out

Start with **[Godot](godot.md)** (free, MIT, easiest to learn) or **[Unity Personal](unity.md)** (free for indies, biggest community). Finish a small game — that's the most important step.

---

## Cross-references

- For 3D graphics and shaders, see [`../ai-ml-llm/multimodal-models.md`](../ai-ml-llm/multimodal-models.md) (for computer vision adjacent topics).
- For dev / deploy pipelines, see [`../devops-cloud/README.md`](../devops-cloud/README.md).
- For mobile app deployment, see [`../mobile/mobile-ci-cd.md`](../mobile/mobile-ci-cd.md).

---

## Build progress

**Phase 11 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.