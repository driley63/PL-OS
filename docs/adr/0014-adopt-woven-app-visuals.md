# ADR-0014: Adopt the woven Plectara app visuals

Status: Accepted for repository implementation
Date: 2026-09-28
Owner: Design System Working Group

## Context

The owner approved the capture widget identity and requested a matching app direction. The first app proposal's content did not reflect the actual app. The owner supplied an empty Today screenshot, followed by populated Today, Timeline, Charts, and Insights screenshots. The revised four-screen light/dark review was approved for PL-OS integration.

## Decision

Adopt the [App Visual Specification](../specs/02-design/app-visuals.md): exact saved gentle-focus yarn across the shell, horizontal ink header shade, unchanged canonical logo on Today, actual page titles elsewhere, soft copper rules, opaque mint light cards, opaque ink dark cards, tested control outlines, and the current four navigation destinations.

Publish screenshots, exact artwork, design values, color adapters, provenance, an editable/offline reference, and verification evidence. Preserve screen content, source badges, units, warnings, and actual feature behavior. Chart geometry and screenshot values remain review fixtures.

## Approved exceptions

- The daily app shell may carry the yarn identity, extending the previous reservation of large brand expression for onboarding and milestones.
- App reading cards use 14-unit padding/radius and thin decorative copper outlines. These are component aliases, not replacement foundation scales.
- Your Progress contains three display-only metric tiles. This bounded group is an exception to the no-nested-card rule.
- Today retains global filled Log and a contextual filled Log Period inside a supported reminder. Quick Log remains outlined; ordinary forms retain the usual action hierarchy.
- The screenshot's chart uses tested link tones with circle markers. The app-local attention and control-outline tones have their own contrast fixtures.

## Alternatives

Header-only yarn and lifted dark cards remain review alternatives. A fictional dashboard with favorites and sample health summaries was replaced with the actual screenshot content. Copying the widget's transparent dark grouping into long app reading cards was not adopted.

## Consequences

Brand, Design, Product, and Engineering guidance link to the app contract. Existing widget rendering continues under ADR-0013. Foundation tokens, AI authorship policy, clinical rule thresholds, route behavior, and the tracking catalog are governed by their existing contracts. This acceptance covers PL-OS standards and assets; native implementation and accessibility evidence are separate.

See [RFC-0008](../rfc/0008-woven-app-visuals.md) and [v2.6.0 release notes](../releases/v2.6.0/README.md).
