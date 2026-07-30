---
name: Expo
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://expo.dev/
  - https://docs.expo.dev/
  - https://docs.expo.dev/eas/
  - https://docs.expo.dev/router/introduction/
  - https://docs.expo.dev/build/introduction/
  - https://docs.expo.dev/submit/introduction/
  - https://docs.expo.dev/workflow/overview/
  - https://docs.expo.dev/versions/latest/
  - https://github.com/expo/expo
  - https://github.com/expo/eas-cli
  - https://docs.expo.dev/guides/local-app-development/
  - https://expo.dev/changelog
  - https://reactnavigation.org/
  - https://docs.expo.dev/versions/latest/sdk/overview/
tags: [expo, react-native, eas, eas-build, eas-update, expo-router, mobile, devops, ota]
---

# Expo

## One-liner

The recommended framework on top of React Native — managed workflow, cloud build, OTA updates, file-based routing, and the easiest path from `npx create-expo-app` to the App Store.

## What It Is

Expo is a framework + platform on top of React Native. It provides:

- **Managed workflow** — most config is abstracted; you don't fight Xcode / Gradle.
- **Expo CLI + Expo Go** — instant dev on a physical device or simulator.
- **Expo SDK** — pre-built modules (Camera, Location, Notifications, SecureStore, etc.) that work cross-platform without writing native code.
- **Expo Router** — file-based routing for RN (parallels Next.js App Router).
- **EAS (Expo Application Services)** — cloud CI/CD:
  - **EAS Build** — builds your iOS / Android app in the cloud; no Mac needed for iOS.
  - **EAS Submit** — submits to App Store / Play Store.
  - **EAS Update** — OTA (over-the-air) JS updates; bypass app store review for JS-only changes.
- **Expo Modules API** — write your own native modules in Swift/Kotlin with a unified TS API.
- **Continuous Native Generation (CNG)** — `prebuild` regenerates native `ios/` and `android/` folders from config; CI builds without committing native code.

The 2026 baseline is **Expo SDK 52+** with:
- **New Architecture enabled by default** (Fabric + TurboModules).
- **Expo Router v4** mature.
- **EAS Build** cloud-only by default (no local Xcode required for iOS).
- **EAS Update** for OTA JS updates.
- **CNG** workflow standard.

Adoption: Expo is the **default way to start React Native projects** in 2026. Per [Expo's own metrics](https://expo.dev/changelog) and GitHub stars: massive growth since 2022; most RN tutorials and starter kits use Expo.

## When To Use It

- **You're starting a new React Native project.** Default.
- **You want OTA updates** to ship bug fixes and JS features without app store review.
- **You want cloud builds** — no Mac required for iOS.
- **You want file-based routing** (Expo Router parallels Next.js).
- **You're a small team** without dedicated iOS / Android engineers.
- **You want a batteries-included DX** with sensible defaults.

## When NOT To Use It

- **You need a heavily customized native layer** (custom UIKit views, low-level Android APIs) — bare RN or full native.
- **You have an existing RN app** with deep native customization — Expo's "bare workflow" exists but the migration cost may not be worth it.
- **You're allergic to managed abstractions** — Expo hides config; if you need to see every Gradle line, bare RN.
- **You need custom native modules** the SDK doesn't cover — possible with Expo Modules API, but add complexity.
- **You deploy to a platform Expo doesn't support** (Wear OS, embedded) — bare RN.

## Why It Matters in 2026

Three forces:

1. **Cloud builds removed the Mac requirement.** EAS Build compiles iOS apps in the cloud; Linux / Windows devs can ship iOS apps without ever touching Xcode. This single change unlocked RN for a massive population of developers.
2. **OTA updates became a strategic capability.** EAS Update + Expo Router means you ship a hotfix in minutes, not days. Major apps (consumer, fintech, social) rely on this for rapid iteration.
3. **The New Architecture is now default.** Expo SDK 52+ ships with Fabric + TurboModules + Hermes; performance complaints are mostly resolved.

Practitioner defaults in 2026:
- **New project**: `npx create-expo-app` + Expo Router + TypeScript + EAS Build + EAS Update.
- **Existing RN**: Migrate to Expo if practical; otherwise adopt Expo Modules API for new native code.
- **CI/CD**: EAS Build + EAS Submit + EAS Update.
- **Navigation**: Expo Router (file-based).
- **State**: Zustand + TanStack Query (same as web).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 9+ years old; SDK 52+ stable; battle-tested by thousands of apps. |
| Community | 95 | The default RN framework; massive community; EAS documentation is excellent. |
| Learning curve | 80 | Expo CLI is easy; advanced (custom native modules, prebuild) takes study. |
| Performance | 90 | New Architecture by default; performance is now RN-native (Fabric + Hermes). |
| Cost | 85 | Free tier generous; EAS paid plans are reasonable; saves infra cost (no Mac mini required). |
| DX | 95 | Best-in-class for RN; EAS Build = no Xcode; EAS Update = OTA in minutes. |
| Production readiness | 95 | Used at scale by major consumer apps. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Bare React Native** | You need deep native customization; you want full control of Xcode / Gradle. | You're starting a new project — Expo is simpler. |
| **Flutter** | You're not in JS; you want pixel-perfect custom UI. | You have JS / React skills. |
| **Capacitor** | You're a web team that needs a mobile shell. | You need native UI. |
| **Ionic** | You're a web team; you want webview-based apps. | You need native performance. |
| **Tauri Mobile** | You're a Rust shop. | Ecosystem is younger. |

## Sources

- [Expo](https://expo.dev/) — 2026
- [Expo Docs](https://docs.expo.dev/) — 2026
- [EAS Docs](https://docs.expo.dev/eas/) — 2026
- [Expo Router](https://docs.expo.dev/router/introduction/) — 2026
- [Expo Build](https://docs.expo.dev/build/introduction/) — 2026
- [Expo Submit](https://docs.expo.dev/submit/introduction/) — 2026
- [Expo Workflow Overview](https://docs.expo.dev/workflow/overview/) — 2026
- [Expo SDK Versions](https://docs.expo.dev/versions/latest/) — 2026
- [Expo GitHub (expo/expo)](https://github.com/expo/expo) — 2026
- [EAS CLI GitHub (expo/eas-cli)](https://github.com/expo/eas-cli) — 2026
- [Expo Local App Development](https://docs.expo.dev/guides/local-app-development/) — 2026
- [Expo Changelog](https://expo.dev/changelog) — 2026
- [React Navigation](https://reactnavigation.org/) — 2026
- [Expo SDK Overview](https://docs.expo.dev/versions/latest/sdk/overview/) — 2026