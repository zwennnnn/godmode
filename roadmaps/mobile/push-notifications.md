---
name: Push Notifications (FCM / APNs / OneSignal)
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://firebase.google.com/docs/cloud-messaging
  - https://developer.apple.com/documentation/usernotifications
  - https://onesignal.com/
  - https://documentation.onesignal.com/
  - https://docs.expo.dev/push-notifications/overview/
  - https://docs.expo.dev/push-notifications/sending-notifications/
  - https://docs.expo.dev/versions/latest/sdk/notifications/
  - https://docs.pusher.com/beams/
  - https://github.com/zo0r/react-native-push-notification
  - https://notifee.app/
  - https://github.com/invertase/notifee
  - https://www.pusher.com/
  - https://learn.microsoft.com/en-us/azure/notification-hubs/
  - https://aws.amazon.com/sns/
tags: [push-notifications, fcm, apns, onesignal, expo, notifee, pusher, mobile]
---

# Push Notifications (FCM / APNs / OneSignal)

## One-liner

How to deliver timely messages to mobile users — via Apple Push Notification service (iOS), Firebase Cloud Messaging (Android), or a cross-platform service that wraps both.

## What It Is

A push notification is a remote message from a server to a mobile app, displayed in the OS notification center. Three layers:

1. **Device registration** — the app gets a unique device token from Apple (APNs) or Google (FCM).
2. **Server** — your backend sends a notification payload to APNs / FCM with the device token.
3. **Delivery + display** — the OS routes the notification to the app; the app can handle it (deep link, action, etc.).

The 2026 platform landscape:

### Apple Push Notification service (APNs)
- **iOS only**; required for all iOS push notifications.
- **HTTP/2 API** with JWT-based auth.
- **Notification Service Extension** for custom delivery + modification.

### Firebase Cloud Messaging (FCM)
- **Android default**; also supports iOS (single API for both).
- **Free tier** is generous; scales to billions.
- **Topic subscriptions**, **device groups**, **data messages**.

### Cross-platform services

| Service | Notes |
|---------|-------|
| **[OneSignal](https://onesignal.com/)** | Default cross-platform wrapper for FCM + APNs; free tier generous; segments + A/B testing. |
| **[Expo Push](https://docs.expo.dev/push-notifications/overview/)** | Expo's managed wrapper for FCM + APNs; zero-config with EAS. |
| **[Pusher Beams](https://docs.pusher.com/beams/)** | Hosted push for iOS/Android; free tier; deprecated for new projects in favor of Beams. |
| **[Azure Notification Hubs](https://learn.microsoft.com/en-us/azure/notification-hubs/)** | Enterprise; multi-platform. |
| **[AWS SNS](https://aws.amazon.com/sns/)** | AWS-native pub/sub + push. |

### React Native libraries

| Library | Notes |
|---------|-------|
| **[Notifee](https://notifee.app/)** | Best local notifications (in-app + scheduled); required for foreground display on Android 13+. |
| **`@react-native-firebase/messaging`** | Firebase Cloud Messaging RN wrapper. |
| **`expo-notifications`** | Expo's wrapper; pairs with EAS. |
| **`react-native-push-notification`** | Older; less maintained. |

## When To Use It

### Expo Push
- **You're on Expo.** Default.
- **You want zero-config push** to both iOS and Android.

### OneSignal
- **You want advanced segmentation + A/B testing** + analytics.
- **You want a free managed service** without Firebase setup.

### Direct FCM / APNs
- **You want maximum control** and minimum vendor dependency.
- **You have a backend engineer** to handle FCM + APNs JWT + delivery.

### Pusher Beams
- **Legacy project**; not recommended for new 2026 apps (deprecated path).

### Notifee (local notifications)
- **You need local / scheduled notifications** (reminders, alarms, foreground).
- **You need rich notification UI** (Android 13+ foreground).

## When NOT To Use It

### Expo Push
- **You're on bare RN** — possible but less integrated.
- **You need features Expo doesn't expose** — go direct to FCM/APNs.

### OneSignal
- **You want to minimize third-party data sharing** — OneSignal's business model is push; you trade some data.

### Direct FCM / APNs
- **You're a small team with no backend engineer** — managed service is faster.

### Pusher Beams
- **New project in 2026** — use Expo Push or OneSignal.

## Why It Matters in 2026

Three forces:

1. **Push is mandatory for mobile engagement.** Apps without push see lower retention; the cost of sending them is real.
2. **Android 13+ notification permission is opt-in.** Apps must request notification permission at runtime. The permission UX is now a UX design problem.
3. **Cross-platform services simplified setup.** Expo Push and OneSignal removed most of the FCM + APNs boilerplate.

Practitioner defaults in 2026:
- **Expo project**: `expo-notifications` + Expo Push API + EAS.
- **Bare RN**: `@react-native-firebase/messaging` + direct FCM/APNs.
- **Marketing + segmentation**: OneSignal.
- **Local notifications**: Notifee.

## Scoring Matrix (0–100)

### Expo Push
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 5+ years; battle-tested with Expo apps. |
| Community | 90 | Default for Expo projects; huge community. |
| Learning curve | 90 | Zero-config for Expo apps; few concepts. |
| Performance | 90 | Fast delivery; FCM/APNs under the hood. |
| Cost | 85 | Free for reasonable usage; EAS paid tiers for scale. |
| DX | 95 | Best-in-class for Expo. |
| Production readiness | 90 | Used at scale. |

### FCM + APNs (direct)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | The original; used by every serious mobile app. |
| Community | 90 | Massive. |
| Learning curve | 55 | FCM + APNs APIs have quirks; JWT auth on APNs; FCM service account. |
| Performance | 100 | The platform itself. |
| Cost | 95 | Free. |
| DX | 60 | Powerful but verbose; needs backend code. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Expo Push** | You're on Expo. | Bare RN or non-Expo frameworks. |
| **OneSignal** | You want segmentation + A/B testing. | You want minimum third-party data sharing. |
| **FCM + APNs direct** | You want maximum control. | Small team with no backend engineer. |
| **Pusher Beams** | Legacy project. | New project in 2026. |
| **Azure Notification Hubs** | Enterprise / multi-platform. | Most teams. |
| **Email / SMS / in-app messages** | You don't need push. | You need OS-level notifications. |

## Sources

- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) — 2026
- [Apple User Notifications](https://developer.apple.com/documentation/usernotifications) — 2026
- [OneSignal](https://onesignal.com/) — 2026
- [OneSignal Docs](https://documentation.onesignal.com/) — 2026
- [Expo Push Notifications Overview](https://docs.expo.dev/push-notifications/overview/) — 2026
- [Expo Push — Sending Notifications](https://docs.expo.dev/push-notifications/sending-notifications/) — 2026
- [Expo Notifications SDK](https://docs.expo.dev/versions/latest/sdk/notifications/) — 2026
- [Pusher Beams Docs](https://docs.pusher.com/beams/) — 2026
- [react-native-push-notification (zo0r)](https://github.com/zo0r/react-native-push-notification) — 2026
- [Notifee](https://notifee.app/) — 2026
- [Notifee GitHub (invertase/notifee)](https://github.com/invertase/notifee) — 2026
- [Pusher](https://www.pusher.com/) — 2026
- [Azure Notification Hubs](https://learn.microsoft.com/en-us/azure/notification-hubs/) — 2026
- [AWS SNS](https://aws.amazon.com/sns/) — 2026