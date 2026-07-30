---
name: Mobile CI/CD
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://docs.fastlane.tools/
  - https://fastlane.tools/
  - https://github.com/fastlane/fastlane
  - https://docs.expo.dev/build/introduction/
  - https://docs.expo.dev/eas/
  - https://docs.expo.dev/submit/introduction/
  - https://docs.codemagic.io/
  - https://codemagic.io/
  - https://github.com/codemagic-ci-cd/codemagic-docs
  - https://developer.apple.com/xcode-cloud/
  - https://developer.apple.com/testflight/
  - https://docs.github.com/en/actions
  - https://www.bitrise.io/
  - https://devcenter.bitrise.com/
  - https://github.com/bitrise-io/bitrise
  - https://learn.microsoft.com/en-us/azure/devops/pipelines/
  - https://circleci.com/docs/
tags: [mobile-ci-cd, fastlane, eas, codemagic, bitrise, xcode-cloud, testflight, devops, mobile]
---

# Mobile CI/CD (Fastlane / EAS Build / Codemagic / Bitrise)

## One-liner

The pipeline that builds, tests, signs, and ships iOS + Android apps — to the App Store, Play Store, internal testers, or your OTA channel.

## What It Is

Mobile CI/CD has unique challenges vs web:
- **iOS requires macOS** for builds (Xcode is macOS-only).
- **Code signing** with Apple Developer certificates, provisioning profiles, Google Play upload keys.
- **App Store submission** with metadata, screenshots, review.
- **Beta distribution** (TestFlight, internal tracks).
- **OTA updates** for JS / Dart apps (RN, Flutter).

The 2026 landscape:

| Tool | Sweet spot |
|------|-----------|
| **[Fastlane](https://docs.fastlane.tools/)** | The OG; mature; Ruby; widely used in scripts + CI. |
| **[EAS Build / Submit](https://docs.expo.dev/build/introduction/)** | Default for Expo; cloud builds (no Mac needed). |
| **[Codemagic](https://docs.codemagic.io/)** | Flutter-native; also supports RN; cloud builds. |
| **[Xcode Cloud](https://developer.apple.com/xcode-cloud/)** | Apple's CI for Apple platforms; integrates with TestFlight. |
| **[Bitrise](https://www.bitrise.io/)** | Mobile-first CI/CD; mature; lots of integrations. |
| **[App Center](https://appcenter.ms/)** (deprecated 2025) | Microsoft's mobile CI; winding down. |
| **GitHub Actions / CircleCI / GitLab CI** | General CI that can do mobile with the right config (often needs self-hosted macOS runners). |

### Fastlane
- **Ruby gem** with actions for: `match` (code signing), `gym` (build), `pilot` (TestFlight upload), `deliver` (App Store), `supply` (Play Store), `scan` (tests).
- **Lanes** = reusable workflow definitions.
- **Mature**; the most-used mobile build automation tool.
- **Cloud runs** on GitHub Actions / CircleCI / Bitrise.

### EAS Build
- **Expo's cloud build service**; no Mac required for iOS.
- **EAS Submit** for App Store / Play Store.
- **EAS Update** for OTA JS updates.
- **Integrates** with GitHub / GitLab / Bitbucket.
- **Pricing**: free tier + paid for larger builds.

### Codemagic
- **Flutter-first** (built by the Flutter community); also RN.
- **Cloud macOS / Linux / Windows** runners.
- **Auto-detects** Flutter / RN / native projects.

### Xcode Cloud
- **Apple's CI**; only for Apple platforms.
- **Builds, tests, distributes to TestFlight**.
- **Free tier**: 25 hours/month.

### Bitrise
- **Mobile-first CI**; mature; many integrations.
- **Cloud macOS M1 runners**; fastest for iOS.
- **Steep learning curve** vs EAS / Codemagic.

## When To Use It

### EAS Build
- **You're on Expo.** Default.
- **You want zero-config cloud builds** with no Mac.

### Fastlane
- **You have an existing Fastlane setup.**
- **You need fine-grained control** of every step.

### Codemagic
- **You're on Flutter** (or RN).
- **You want a polished Flutter-native UX**.

### Bitrise
- **You want mobile-first CI** with mature integrations.
- **You need iOS M1 cloud runners** (fastest).

### Xcode Cloud
- **Apple-platform-only apps.**
- **You want minimal config** with Apple's tooling.

### GitHub Actions (with macOS runners)
- **Your code is on GitHub** and you want one CI for everything.
- **You accept self-hosted macOS runner cost** (or use GitHub-hosted for public repos).

## When NOT To Use It

### EAS Build
- **You're on bare RN without Expo** — possible but less integrated.

### Xcode Cloud
- **Android** — Xcode Cloud is Apple-only.

### Bitrise / Codemagic
- **You need to minimize cost** — both are paid for serious use.

### Self-hosted macOS runners
- **You're a small team** — cloud is cheaper than maintaining Mac minis.

### Fastlane alone
- **You need cloud builds** — Fastlane is a scripting layer; you still need a CI.

## Why It Matters in 2026

Three forces:

1. **Cloud builds killed the Mac requirement.** EAS Build, Codemagic, Bitrise all run iOS builds in the cloud. Linux / Windows devs can ship iOS apps without a Mac mini.
2. **EAS Update + CodePush made OTA routine.** Ship bug fixes in minutes; bypass app store review for JS-only changes.
3. **Apple Silicon (M1+) made iOS builds fast.** Cloud runners with M-series chips cut build times 30–50%.

Practitioner defaults in 2026:
- **Expo app**: EAS Build + EAS Submit + EAS Update.
- **Bare RN**: Fastlane + GitHub Actions + CodePush or EAS Update.
- **Flutter**: Codemagic (default) or Fastlane + GitHub Actions.
- **Native iOS**: Xcode Cloud + Fastlane.
- **Native Android**: Fastlane + GitHub Actions.

## Scoring Matrix (0–100)

### EAS Build
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 5+ years; growing fast. |
| Community | 90 | Default for Expo; massive community. |
| Learning curve | 95 | Zero-config for Expo apps. |
| Performance | 90 | Cloud M1+ runners; fast builds. |
| Cost | 80 | Free tier; paid for serious use. |
| DX | 95 | Best-in-class for Expo. |
| Production readiness | 90 | Used at scale. |

### Fastlane
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 10+ years; the standard for mobile build automation. |
| Community | 90 | Massive. |
| Learning curve | 60 | Ruby; steep for beginners; powerful once learned. |
| Performance | 90 | Fast; depends on runner. |
| Cost | 90 | OSS free; you pay for CI runners. |
| DX | 75 | Powerful but verbose. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **EAS Build** | Expo app. | Bare RN with deep customization. |
| **Fastlane** | You want fine-grained control; existing setup. | Quick setup; Expo. |
| **Codemagic** | Flutter or RN. | Native iOS only. |
| **Bitrise** | Mobile-first CI; mature integrations. | Cost-sensitive. |
| **Xcode Cloud** | Apple-only; minimal config. | Multi-platform. |
| **GitHub Actions + Mac runner** | You want one CI for everything. | Heavy iOS build load (self-hosted cost). |
| **App Center** | Legacy. | New project — Microsoft deprecated it. |

## Sources

- [Fastlane Docs](https://docs.fastlane.tools/) — 2026
- [Fastlane](https://fastlane.tools/) — 2026
- [Fastlane GitHub (fastlane/fastlane)](https://github.com/fastlane/fastlane) — 2026
- [Expo Build](https://docs.expo.dev/build/introduction/) — 2026
- [EAS](https://docs.expo.dev/eas/) — 2026
- [Expo Submit](https://docs.expo.dev/submit/introduction/) — 2026
- [Codemagic Docs](https://docs.codemagic.io/) — 2026
- [Codemagic](https://codemagic.io/) — 2026
- [Codemagic GitHub (codemagic-ci-cd/codemagic-docs)](https://github.com/codemagic-ci-cd/codemagic-docs) — 2026
- [Xcode Cloud](https://developer.apple.com/xcode-cloud/) — 2026
- [TestFlight](https://developer.apple.com/testflight/) — 2026
- [GitHub Actions Docs](https://docs.github.com/en/actions) — 2026
- [Bitrise](https://www.bitrise.io/) — 2026
- [Bitrise Devcenter](https://devcenter.bitrise.com/) — 2026
- [Bitrise GitHub (bitrise-io/bitrise)](https://github.com/bitrise-io/bitrise) — 2026
- [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/) — 2026
- [CircleCI Docs](https://circleci.com/docs/) — 2026