---
name: React Native
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://reactnative.dev/
  - https://reactnative.dev/docs/getting-started
  - https://reactnative.dev/architecture/landing-page
  - https://reactnative.dev/blog
  - https://github.com/facebook/react-native
  - https://github.com/react-native-community
  - https://www.bolderapps.com/blog-posts/react-natives-2026-new-architecture-how-jsi-and-fabric-finally-killed-the-performance-bridge
  - https://www.agilesoftlabs.com/blog/2026/03/react-native-new-architecture-migration
  - https://www.pkgpulse.com/guides/react-native-new-architecture-fabric-turbomodules-expo-2026
  - https://blog.codemagic.io/react-native-new-architecture-ota-updates/
  - https://github.com/expo/expo
  - https://docs.expo.dev/
  - https://expo.dev/
  - https://reactnavigation.org/
  - https://docs.swmansion.com/react-native-reanimated/
  - https://github.com/software-mansion/react-native-reanimated
  - https://github.com/mrousavy/react-native-mmkv
tags: [react-native, mobile, ios, android, fabric, turbomodules, jsi, hermes, expo, cross-platform]
---

# React Native

## One-liner

Meta's open-source framework for building native iOS and Android apps with React — the default choice for JS / TS teams shipping mobile in 2026.

## What It Is

React Native (RN) lets you write mobile apps using React + JavaScript/TypeScript, with components that compile to **native UI views** (not a webview). You get the productivity of the React ecosystem + the performance of native UI. The same codebase can target iOS, Android, and increasingly other platforms (visionOS, Windows, macOS).

The 2026 baseline is the **New Architecture** (now production-ready):

- **JSI (JavaScript Interface)** — direct C++ bindings replacing the old async bridge; eliminates serialization overhead.
- **Fabric** — new renderer with synchronous layout, concurrent React features (transitions, Suspense), better performance.
- **TurboModules** — lazy-loaded native modules with type-safe specs; **44% faster app startup** (3.2s → 1.8s per Bolder Apps 2026 benchmarks).
- **Codegen** — generates native code from TypeScript specs for type-safe native bridges.
- **Hermes** — the default JS engine; faster startup, lower memory than JSC.
- **Bridgeless mode** — fully synchronous native calls (2026 default).

The 2026 ecosystem around RN:

| Tool | Notes |
|------|-------|
| **[Expo](https://expo.dev/)** | The recommended RN framework; managed workflow; OTA updates; EAS Build. |
| **[React Navigation](https://reactnavigation.org/)** | Default navigation library. |
| **[Reanimated](https://docs.swmansion.com/react-native-reanimated/)** | High-performance animations on the UI thread. |
| **[MMKV](https://github.com/mrousavy/react-native-mmkv)** | Fast key-value storage (10× faster than AsyncStorage). |
| **[React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/)** | Native-driven gestures. |
| **[Expo Router](https://docs.expo.dev/router/introduction/)** | File-based routing for RN. |
| **[EAS Build / Submit / Update](https://docs.expo.dev/eas/)** | Expo's cloud CI/CD for RN. |
| **NativeWind** | Tailwind for RN. |

Adoption (per [State of JS](https://stateofjs.com/), GitHub stars, npm downloads):
- RN is the **most-used cross-platform mobile framework** by a wide margin.
- Used by Meta, Microsoft, Shopify, Discord, Tesla, Salesforce, Wix, Instagram (parts), Facebook (parts), every major startup.
- ~30%+ of new mobile apps in 2026 are React Native or Flutter.

## When To Use It

- **You're a JS / TS / React team** and want to ship mobile without learning Swift + Kotlin.
- **You want code sharing between web and mobile** (RN + React share state management patterns, tooling).
- **Your app is mostly forms, lists, navigation, business logic** — RN shines here.
- **You want OTA updates** (Expo Updates, CodePush) to bypass app store review for JS-only changes.
- **You want to ship fast** — single codebase, single dev team.
- **You want a huge ecosystem** of libraries (navigation, maps, charts, payments).

## When NOT To Use It

- **You need pixel-perfect platform-native UI** that follows every iOS HIG / Material guideline — native wins.
- **Heavy animations / custom UI rendering** (Sketch-like apps, procreate-like apps) — native or Flutter.
- **Tight integration with platform-specific hardware** (advanced camera, ARKit, low-level Bluetooth) — native is easier.
- **You're shipping to a platform RN doesn't support well** (older watchOS, embedded).
- **You have no JS experience and no time to learn.** Native for one platform might be faster.
- **Your app needs <50ms gesture response for gaming-style interactions** — RN is improving but native still wins here.

## Why It Matters in 2026

Three forces:

1. **The New Architecture finished its transition.** In 2024–2026, Fabric + TurboModules + Hermes went from "experimental opt-in" to "default and required." Performance complaints that plagued RN for years are mostly resolved. Startup is 44% faster; UI is smoother; native module APIs are type-safe.
2. **Expo became the default framework.** The Expo team's managed workflow (EAS Build, EAS Update, EAS Submit, Expo Router) made RN deploy + OTA + App Store submission genuinely pleasant. Bare RN is now the minority.
3. **AI-assisted RN is excellent.** Claude / Cursor / Copilot all generate RN + TSX reliably. The training data is massive.

Practitioner defaults in 2026:
- **New project**: Expo + Expo Router + TypeScript + React Navigation (via Expo Router) + Reanimated + MMKV.
- **Existing RN app**: Migrate to New Architecture; switch to Expo if practical.
- **State**: Zustand or Jotai for small; Redux Toolkit + RTK Query for large teams.
- **Navigation**: Expo Router (file-based) over React Navigation for new apps.
- **Animations**: Reanimated 3.x.
- **Storage**: MMKV.
- **Backend sync**: TanStack Query + a sync engine (see `offline-sync.md`).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 11+ years old (Meta, 2015); battle-tested at massive scale. |
| Community | 95 | Largest cross-platform mobile community; ~120K GitHub stars; thousands of libraries. |
| Learning curve | 65 | React knowledge transfers; native modules require Swift/Kotlin/Obj-C/Java. |
| Performance | 85 | New Architecture closed most of the gap with native; still slightly behind for extreme cases. |
| Cost | 95 | Free; App Store + Play Store fees are standard. |
| DX | 90 | Expo is best-in-class; Fast Refresh; Metro bundler; Flipper for debugging. |
| Production readiness | 95 | Used at Shopify, Microsoft, Discord, Tesla, every startup; Expo's EAS handles the app store submission mess. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Flutter** | You want pixel-perfect custom UI; you're not in JS. | You have JS/React skills; you want web reuse. |
| **Native (Swift / Kotlin)** | You need maximum performance, deep platform integration, or platform-specific UI. | You want cross-platform code sharing or you're JS-first. |
| **Capacitor / Cordova** | You're building a web app that needs a thin native shell. | You need native UI / performance. |
| **Kotlin Multiplatform (KMP)** | You want to share business logic between Android + iOS, with native UI. | You want a single codebase that includes UI. |
| **Ionic** | You're a web team that needs mobile fast. | You need native performance. |
| **Xamarin / .NET MAUI** | You're a .NET shop. | Most teams — smaller ecosystem. |
| **Tauri Mobile** | You're a Rust shop; tiny apps. | Ecosystem is young. |

## Sources

- [React Native Official Site](https://reactnative.dev/) — 2026
- [React Native — Getting Started](https://reactnative.dev/docs/getting-started) — 2026
- [About the New Architecture](https://reactnative.dev/architecture/landing-page) — 2026
- [React Native Blog](https://reactnative.dev/blog) — 2026
- [React Native GitHub (facebook/react-native)](https://github.com/facebook/react-native) — 2026
- [React Native Community (GitHub)](https://github.com/react-native-community) — 2026
- [Bolder Apps — React Native's 2026 New Architecture](https://www.bolderapps.com/blog-posts/react-natives-2026-new-architecture-how-jsi-and-fabric-finally-killed-the-performance-bridge) — 2026-02
- [AgileSoftLabs — React Native New Architecture Migration 2026 Guide](https://www.agilesoftlabs.com/blog/2026/03/react-native-new-architecture-migration) — 2026-03
- [PkgPulse — React Native New Architecture: Fabric & Expo 2026](https://www.pkgpulse.com/guides/react-native-new-architecture-fabric-turbomodules-expo-2026) — 2026-03
- [CodeMagic — New Architecture + OTA Updates](https://blog.codemagic.io/react-native-new-architecture-ota-updates/) — 2026-06
- [Expo GitHub (expo/expo)](https://github.com/expo/expo) — 2026
- [Expo Docs](https://docs.expo.dev/) — 2026
- [Expo](https://expo.dev/) — 2026
- [React Navigation](https://reactnavigation.org/) — 2026
- [Reanimated Docs](https://docs.swmansion.com/react-native-reanimated/) — 2026
- [Reanimated GitHub (software-mansion/react-native-reanimated)](https://github.com/software-mansion/react-native-reanimated) — 2026
- [React Native MMKV (mrousavy/react-native-mmkv)](https://github.com/mrousavy/react-native-mmkv) — 2026