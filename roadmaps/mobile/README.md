---
name: Mobile
slug: mobile
source: https://roadmap.sh/react-native + https://roadmap.sh/android + https://roadmap.sh/ios
last-updated: 2026-07-30
tech-count: 10
status: in-progress
---

# Mobile Roadmap

> **Category:** Technologies for building, shipping, and operating mobile apps on iOS and Android — covering native (Swift / Kotlin), cross-platform (React Native, Flutter), build tooling, and mobile-specific concerns (push notifications, offline sync, CI/CD).
> **Sources:** [roadmap.sh/react-native](https://roadmap.sh/react-native), [roadmap.sh/android](https://roadmap.sh/android), [roadmap.sh/ios](https://roadmap.sh/ios)

This roadmap covers the mobile development stack for 2026: native iOS / Android, cross-platform frameworks, build + distribution, mobile-specific state + sync, and mobile CI/CD. The 10 picks below are the ones that decide your time-to-market, your developer hiring pool, and your day-2 operating cost.

---

## Technologies (all researched 2026-07-30)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | React Native (New Architecture: Fabric + TurboModules) | [react-native.md](react-native.md) | researched |
| 2 | Expo (managed framework + EAS Build/Submit/Update) | [expo.md](expo.md) | researched |
| 3 | Flutter (Dart + Impeller + Material 3) | [flutter.md](flutter.md) | researched |
| 4 | Swift / iOS Native (SwiftUI + Swift 6) | [swift-ios.md](swift-ios.md) | researched |
| 5 | Kotlin / Android Native (Jetpack Compose + KMP) | [kotlin-android.md](kotlin-android.md) | researched |
| 6 | Mobile State Management (Zustand / Redux Toolkit + MMKV) | [mobile-state-management.md](mobile-state-management.md) | researched |
| 7 | Offline-First Sync (PowerSync / WatermelonDB / RxDB / TanStack DB) | [offline-sync.md](offline-sync.md) | researched |
| 8 | Push Notifications (FCM / APNs / OneSignal / Expo Push) | [push-notifications.md](push-notifications.md) | researched |
| 9 | Mobile CI/CD (EAS Build / Fastlane / Codemagic / Bitrise) | [mobile-ci-cd.md](mobile-ci-cd.md) | researched |
| 10 | Mobile Analytics & Crash Reporting (Sentry / Firebase / Amplitude / PostHog) | [mobile-analytics.md](mobile-analytics.md) | researched |

---

## Quick Decision Guide

### If you're a JS / TS / React team shipping mobile

- **Framework**: **React Native + Expo** (managed workflow). New Architecture enabled by default.
- **Navigation**: Expo Router (file-based).
- **State**: Zustand + TanStack Query.
- **Persistence**: MMKV (replaces AsyncStorage).
- **Offline-first**: PowerSync + TanStack DB if you have a Postgres backend.
- **Push**: Expo Push (zero-config).
- **CI/CD**: EAS Build + EAS Submit + EAS Update.
- **Errors**: Sentry. **Analytics**: PostHog or Amplitude.

### If you're a brand-heavy / animation-heavy app

- **Framework**: **Flutter**.
- **State**: Riverpod 2.x.
- **DB**: Drift (SQLite).
- **Push**: Firebase Cloud Messaging.
- **CI/CD**: Codemagic (Flutter-native) or Fastlane + GitHub Actions.
- **Errors**: Sentry or Firebase Crashlytics. **Analytics**: Firebase Analytics or PostHog.

### If you're building platform-native iOS only

- **Language**: **Swift + SwiftUI** (default in 2026).
- **Persistence**: SwiftData + `@AppStorage` for settings.
- **Concurrency**: Swift Concurrency (async/await + actors).
- **CI/CD**: Xcode Cloud + Fastlane.
- **Errors**: Sentry or Firebase Crashlytics. **Analytics**: Firebase Analytics.

### If you're building platform-native Android only

- **Language**: **Kotlin + Jetpack Compose**.
- **DI**: Hilt. **DB**: Room. **Networking**: Retrofit + OkHttp (or Ktor Client).
- **CI/CD**: GitHub Actions + Fastlane.
- **Errors**: Firebase Crashlytics. **Analytics**: Firebase Analytics.

### If you want to share business logic between iOS + Android with native UIs

- **Framework**: **Kotlin Multiplatform (KMP)**.
- **UI**: Compose Multiplatform (if you want shared UI) or native UIs.
- **Mobile CI/CD**: Bitrise or Codemagic.

---

## Cross-references

- For the backend / API layer, see [`../frontend-backend/README.md`](../frontend-backend/README.md).
- For AI features in the app, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- For deployment / hosting, see [`../devops-cloud/README.md`](../devops-cloud/README.md).

---

## Build progress

**Phase 5 complete** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`. All 4 roadmaps now complete! 🎉

---

## Cross-references

- For the backend / API layer, see [`../frontend-backend/README.md`](../frontend-backend/README.md).
- For AI features in the app, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- For deployment / hosting, see [`../devops-cloud/README.md`](../devops-cloud/README.md).

---

## Build progress

**Phase 5 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.