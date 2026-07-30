---
name: Flutter
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://flutter.dev/
  - https://docs.flutter.dev/
  - https://docs.flutter.dev/get-started
  - https://flutter.dev/showcase
  - https://github.com/flutter/flutter
  - https://dart.dev/
  - https://dart.dev/overview
  - https://pub.dev/
  - https://docs.flutter.dev/perf
  - https://material.io/
  - https://docs.flutter.dev/ui/widgets/cupertino
  - https://firebase.google.com/docs/flutter
  - https://riverpod.dev/
  - https://bloclibrary.dev/
  - https://docs.flutter.dev/data-and-backend/state-mgmt/intro
tags: [flutter, dart, mobile, ios, android, cross-platform, material, cupertino, web, desktop]
---

# Flutter

## One-liner

Google's UI toolkit for building natively compiled applications for mobile, web, and desktop from a single Dart codebase — the leading non-JS cross-platform framework in 2026.

## What It Is

Flutter is Google's open-source UI SDK that compiles **Dart** code to native ARM / x86 binaries for iOS, Android, web (JavaScript / WebAssembly), Windows, macOS, and Linux. It ships its own rendering engine (Skia → Impeller) so apps look identical across platforms and don't rely on OEM UI components.

The 2026 baseline is **Flutter 3.x** (stable since 2022) with:

- **Impeller** — Flutter's new rendering engine (default on iOS; default on Android in 2024+); smoother animations, lower jank.
- **Dart 3** — sound null safety, records, patterns, class modifiers; modern language.
- **Material 3** (Material You) support; **Cupertino** widgets for native iOS look.
- **WebAssembly** compilation for web (stable, performance-improving).
- **Casual game dev** with Flame engine.
- **Hot reload** — sub-second state preservation on save.
- **Platform channels** for native API access.
- **Flutter 3.27+** in 2026 added tighter web performance + Impeller on Android by default.

State management ecosystem (per [Flutter state management docs](https://docs.flutter.dev/data-and-backend/state-mgmt/intro)):
| Tool | Notes |
|------|-------|
| **`setState` + `InheritedWidget`** | Built-in; fine for tiny apps. |
| **[Riverpod](https://riverpod.dev/)** | Modern; compile-safe; the de-facto default in 2026. |
| **[Bloc / Cubit](https://bloclibrary.dev/)** | Event-driven; great for complex flows; loved by enterprise. |
| **Provider** | Older; still works but Riverpod is the evolution. |
| **GetX** | All-in-one (state + nav + DI); popular but controversial. |

Adoption: Flutter is the **#2 cross-platform mobile framework** (after React Native). Used by Google Ads, Google Pay, BMW, eBay, Toyota, Realtor.com, Nubank, Hamilton app, many startups. ~20%+ of new mobile apps in 2026.

## When To Use It

- **You want pixel-perfect custom UI** that looks identical on every platform.
- **You have a design-heavy brand** (animations, custom layouts, sketch-quality screens).
- **You're not in JS/TS** — Flutter + Dart is a fresh start, often with TS-quality tooling.
- **You want one codebase for mobile + web + desktop** (Flutter's web and desktop are real, not toys).
- **You need 60/120fps animations** — Skia/Impeller is great.
- **You want hot reload** (sub-second iteration).

## When NOT To Use It

- **You have a JS/React team** — React Native is the natural fit; learning Dart is overhead.
- **You need 100% native UI** — Flutter draws everything itself; users can usually tell.
- **You depend on OEM-specific behavior** (e.g. exact iOS HIG animations) — native or RN.
- **You have a tiny simple app** — the Flutter overhead isn't worth it.
- **Your app is mostly text + forms** — RN is fine and faster to build.
- **You can't accept Dart in your hiring pool** — Dart is easier to learn than Rust but still a niche.

## Why It Matters in 2026

Three forces:

1. **Impeller shipped and killed the Skia jank complaints.** Flutter's old Skia renderer had minor animation issues; Impeller (default since 2023 iOS, 2024 Android) is smooth on both. The "Flutter is janky" era is over.
2. **Material 3 + Cupertino matured.** Flutter can ship a Material 3 Android look AND a Cupertino iOS look; many apps blend them for brand consistency.
3. **Web and desktop targets stabilized.** Flutter web (CanvasKit / Wasm) and desktop (macOS, Windows, Linux) are production-usable, not just demos. Single codebase → mobile + web + desktop is real.

Practitioner defaults in 2026:
- **State**: **Riverpod 2.x** (default) or Bloc for enterprise.
- **Routing**: **go_router** (official; declarative).
- **DI**: Riverpod covers it; or `get_it` for service locator.
- **Networking**: **Dio** (mature) or **package:http**.
- **Local DB**: **Drift** (formerly Moor) or **Isar**.
- **CI/CD**: **Codemagic** (Flutter-native), **Fastlane**, GitHub Actions.
- **Web**: enable Wasm compilation for perf.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 8+ years old (Google, 2017/2018 1.0); stable. |
| Community | 90 | 2nd-largest mobile cross-platform community; massive pub.dev ecosystem. |
| Learning curve | 70 | Dart is easy to learn; Flutter widget tree takes study; hot reload helps a lot. |
| Performance | 95 | Compiles to native ARM; Impeller renderer; 60/120fps animation. |
| Cost | 95 | Free; App Store + Play Store fees are standard. |
| DX | 95 | Hot reload is best-in-class; widget inspector; DevTools. |
| Production readiness | 95 | Used at Google, BMW, eBay, Toyota, many enterprises. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **React Native** | You're in JS/React; you want web reuse via React. | You're not in JS; you want pixel-perfect custom UI. |
| **Native (Swift / Kotlin)** | You need maximum performance, deep platform integration. | You want cross-platform code sharing. |
| **Kotlin Multiplatform (KMP)** | You want to share business logic only; UI is native. | You want a single codebase including UI. |
| **Capacitor / Cordova** | You're a web team; you want a thin native shell. | You need native UI / performance. |
| **Ionic** | You're a web team that wants webviews. | You need native performance. |
| **Tauri Mobile** | You're a Rust shop. | Young ecosystem. |
| **Xamarin / .NET MAUI** | You're a .NET shop. | Most teams — smaller ecosystem than Flutter. |

## Sources

- [Flutter Official Site](https://flutter.dev/) — 2026
- [Flutter Docs](https://docs.flutter.dev/) — 2026
- [Flutter — Get Started](https://docs.flutter.dev/get-started) — 2026
- [Flutter Showcase](https://flutter.dev/showcase) — 2026
- [Flutter GitHub (flutter/flutter)](https://github.com/flutter/flutter) — 2026
- [Dart](https://dart.dev/) — 2026
- [Dart Overview](https://dart.dev/overview) — 2026
- [pub.dev](https://pub.dev/) — 2026
- [Flutter Performance](https://docs.flutter.dev/perf) — 2026
- [Material Design](https://material.io/) — 2026
- [Cupertino Widgets](https://docs.flutter.dev/ui/widgets/cupertino) — 2026
- [Firebase Flutter](https://firebase.google.com/docs/flutter) — 2026
- [Riverpod](https://riverpod.dev/) — 2026
- [Bloc Library](https://bloclibrary.dev/) — 2026
- [Flutter State Management Intro](https://docs.flutter.dev/data-and-backend/state-mgmt/intro) — 2026