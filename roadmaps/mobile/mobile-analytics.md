---
name: Mobile Analytics and Crash Reporting
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://sentry.io/
  - https://docs.sentry.io/
  - https://firebase.google.com/docs/crashlytics
  - https://firebase.google.com/docs/analytics
  - https://amplitude.com/
  - https://amplitude.com/docs
  - https://mixpanel.com/
  - https://docs.mixpanel.com/
  - https://posthog.com/
  - https://posthog.com/docs
  - https://www.bugsnag.com/
  - https://docs.bugsnag.com/
  - https://docs.expo.dev/guides/analytics/
  - https://segment.com/
  - https://segment.com/docs/
tags: [analytics, crash-reporting, sentry, firebase, amplitude, mixpanel, posthog, bugsnag, mobile, observability]
---

# Mobile Analytics and Crash Reporting (Sentry / Firebase / Amplitude / PostHog)

## One-liner

How to know what your users are doing (analytics), what's breaking (crash reporting), and how to debug in production — the eyes and ears of your mobile app.

## What It Is

Two distinct (but related) domains:

1. **Crash reporting** — automatically capture unhandled exceptions, ANRs, native crashes; show stack traces + breadcrumbs; alert on spikes.
2. **Product analytics** — track user events, funnels, retention, feature usage; build cohorts and segments.

The 2026 landscape:

### Crash reporting / Error tracking

| Tool | Notes |
|------|-------|
| **[Sentry](https://sentry.io/)** | The de-facto error tracking for mobile + web + backend; rich context, releases, source maps. |
| **[Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)** | Free; Android-first; great for native crashes; lighter for JS errors. |
| **[Bugsnag](https://www.bugsnag.com/)** | Stability scoring; loved by enterprises. |
| **App Center Crash** | Deprecated (Microsoft winding down). |

### Product analytics

| Tool | Notes |
|------|-------|
| **[Firebase Analytics](https://firebase.google.com/docs/analytics)** | Free; default for Android; integrates with all Firebase products. |
| **[Amplitude](https://amplitude.com/)** | Product analytics leader; funnels + cohorts + experiments. |
| **[Mixpanel](https://mixpanel.com/)** | Event-based analytics; loved by growth teams. |
| **[PostHog](https://posthog.com/)** | OSS-first; product analytics + feature flags + session replay; self-hostable. |
| **[Segment](https://segment.com/)** | Customer data platform; routes events to any tool. |

### Combined

| Tool | Notes |
|------|-------|
| **Sentry + Amplitude / Mixpanel** | Best-of-breed for errors + analytics. |
| **Firebase (Analytics + Crashlytics + Remote Config + A/B)** | Free; all-in-one; Android-first. |
| **PostHog alone** | OSS; analytics + feature flags + error tracking (new). |

## When To Use It

### Crash reporting

#### Sentry
- **Default for React Native + Expo apps.**
- **You want rich context** (breadcrumbs, user info, source maps).
- **You want alerts + releases + performance monitoring.**

#### Firebase Crashlytics
- **Free.** Default for native Android.
- **You're already on Firebase.**

#### Bugsnag
- **You want stability scoring** + enterprise features.

### Product analytics

#### Amplitude
- **You want best-in-class funnels + cohorts + experimentation.**
- **You have a growth team** that lives in dashboards.

#### Mixpanel
- **You want event-based analytics** with strong segmentation.

#### PostHog
- **You want OSS** + self-hostable + product analytics + feature flags + session replay in one.

#### Firebase Analytics
- **Free; you're already on Firebase.**

## When NOT To Use It

### Sentry
- **You only need basic crash reporting** — Crashlytics is simpler + free.

### Firebase Crashlytics
- **You want rich context for JS errors** — Sentry is better for RN.

### Amplitude / Mixpanel
- **Cost-sensitive** — both are expensive at scale. PostHog may be cheaper.

### PostHog
- **You need only basic analytics** — Firebase Analytics is simpler.

### Multiple tools
- **Vendor sprawl.** Pick 1–2 and stick.

## Why It Matters in 2026

Three forces:

1. **Mobile users churn on bugs.** App store reviews are unforgiving. Crash reporting is non-optional for any serious app.
2. **Privacy regulations changed analytics.** GDPR, CCPA, App Tracking Transparency (iOS) all require consent for tracking. Tools that bake in privacy (PostHog, Amplitude) have an edge.
3. **AI-assisted debugging matured.** Sentry's Seer, PostHog's AI summaries — debugging is increasingly AI-augmented.

Practitioner defaults in 2026:
- **React Native / Expo**: Sentry (errors) + Amplitude or PostHog (analytics).
- **Native iOS / Android**: Firebase Crashlytics + Firebase Analytics (free; all-in-one).
- **Flutter**: Sentry + Amplitude / PostHog / Firebase.
- **Cost-sensitive / OSS**: PostHog self-hosted.

## Scoring Matrix (0–100)

### Sentry
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 10+ years; the standard for mobile error tracking. |
| Community | 95 | Massive; loved by devs. |
| Learning curve | 80 | Easy to install; advanced features (releases, performance) take study. |
| Performance | 90 | Excellent; lightweight SDK. |
| Cost | 70 | Free tier; paid scales with volume. |
| DX | 95 | Best-in-class. |
| Production readiness | 100 | Battle-tested. |

### PostHog
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | 5+ years; rapidly maturing. |
| Community | 85 | OSS community; growing. |
| Learning curve | 75 | More features = more concepts. |
| Performance | 85 | Excellent for self-hosted; cloud is fine. |
| Cost | 90 | OSS free; cloud is reasonable. |
| DX | 85 | All-in-one is appealing; some rough edges. |
| Production readiness | 85 | Used at scale; some enterprise features still maturing. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Sentry** | JS/TS apps; you want rich context. | Pure native + only basic crashes. |
| **Firebase Crashlytics** | Native Android; free. | JS errors; you want rich context. |
| **Bugsnag** | Stability scoring + enterprise. | Most teams — niche. |
| **Amplitude** | Best product analytics. | Cost-sensitive; OSS-only. |
| **Mixpanel** | Event-based analytics. | Cost-sensitive. |
| **PostHog** | OSS + self-host + all-in-one. | Best-of-breed in each category. |
| **Firebase Analytics** | Free; all-in-one Firebase. | Advanced cohorts / funnels. |
| **Segment** | You route events to many tools. | You only need one tool. |

## Sources

- [Sentry](https://sentry.io/) — 2026
- [Sentry Docs](https://docs.sentry.io/) — 2026
- [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics) — 2026
- [Firebase Analytics](https://firebase.google.com/docs/analytics) — 2026
- [Amplitude](https://amplitude.com/) — 2026
- [Amplitude Docs](https://amplitude.com/docs) — 2026
- [Mixpanel](https://mixpanel.com/) — 2026
- [Mixpanel Docs](https://docs.mixpanel.com/) — 2026
- [PostHog](https://posthog.com/) — 2026
- [PostHog Docs](https://posthog.com/docs) — 2026
- [Bugsnag](https://www.bugsnag.com/) — 2026
- [Bugsnag Docs](https://docs.bugsnag.com/) — 2026
- [Expo Analytics Guide](https://docs.expo.dev/guides/analytics/) — 2026
- [Segment](https://segment.com/) — 2026
- [Segment Docs](https://segment.com/docs/) — 2026