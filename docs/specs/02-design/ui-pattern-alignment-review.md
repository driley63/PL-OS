# UI Pattern Expansion Alignment Review

Status: Released
Owner: Design System Working Group
Version: 1.5.0
Last updated: 2026-08-04

## Current brand authority

This review records the v1.5.0 baseline. For current identity and color implementation, use [Plectara color migration](plectara-color-migration.md) and the [approved brand kit](../01-brand/plectara-brand-kit.md). The former gradient and LIQ OS lockup are historical; PL-OS now uses Plectara's identity. Existing layout and interaction conclusions remain applicable.

## Purpose

Documents the v1.5.0 UI Pattern Expansion review against released Brand Identity v1.1.0, Product Experience v1.3.0, Engineering Standards v1.4.0, and the current documentation-site brand patch v1.4.1. This review makes prototype-facing UI dependencies explicit for release traceability.

## Scope

- App shell, navigation, page templates, lists, tables, overlays, feedback, search, filters, sorting, progress, and disclosure
- Released Brand Identity color, typography, logo, token, AI color, accessibility, and governance rules
- Released Product Experience workflow intent, health-language, consent, reports, insights, onboarding, settings, notifications, and user-research rules
- Released Engineering Standards routing, state, data model, testing, accessibility, security, privacy, observability, performance, and release rules
- Current documentation-site brand patch behavior for the PL-OS MkDocs site

## Review Outcome

The v1.5.0 UI Pattern Expansion is aligned with Brand Identity v1.1.0, Product Experience v1.3.0, Engineering Standards v1.4.0, and the current documentation-site brand patch v1.4.1. No released Brand, Product, Engineering, or documentation-site brand values need to change for v1.5.0.

The review adds one clarification: UI Pattern Expansion owns reusable presentation and interaction patterns for prototype and product UI assembly, while Product Experience remains authoritative for workflow intent and health-sensitive meaning, Engineering remains authoritative for implementation constraints, and Brand Identity remains authoritative for visual identity and token semantics.

## Required Alignment Rules

- Prototype UI must use released Brand Identity tokens before adding new colors, type, icon, or logo behavior.
- Product workflow screens must preserve Product Experience intent, health-sensitive copy rules, consent behavior, and user agency.
- UI patterns that imply routing, state, persistence, privacy, analytics, security, performance, or release behavior must remain compatible with Engineering Standards.
- AI Purple remains reserved for AI-generated, model-assisted, or confidence-related behavior, even in prototype-only UI.
- Health, privacy, consent, export, deletion, warning, error, loading, stale, and unavailable states must be understandable without color alone.
- Documentation-site styling may demonstrate brand application, but it must not redefine product UI standards.

## Brand Alignment

| Brand rule | UI Pattern Expansion usage | Review decision |
| --- | --- | --- |
| Product UI must use semantic tokens before raw primitive values | Navigation, page templates, collections, feedback, buttons, state cues, and progress patterns reference released token rules | Aligned; no new brand color or typography values are introduced |
| AI Purple is reserved for AI and machine-learning behavior | Navigation, cards, buttons, overlays, and result states restrict AI color to AI-specific destinations and actions | Aligned |
| Signature gradient is reserved for brand moments and large identity surfaces | Page templates and feedback patterns avoid gradients for routine buttons, dense tables, rows, and data cards | Aligned |
| Inter and platform fallbacks remain the UI type strategy | UI patterns define structure and hierarchy without creating a competing typeface or type scale | Aligned |
| Color cannot be the only signal for state | Navigation, collections, feedback, search, progress, and disclosure patterns require text, icon, layout, or semantic cues | Aligned |

## Product Experience Alignment

| Product rule | UI Pattern Expansion usage | Review decision |
| --- | --- | --- |
| Product Experience owns workflow intent and health-sensitive meaning | Page templates define reusable structure but defer workflow intent, copy, claims, and evidence meaning to Volume 03 | Aligned |
| Daily workflows should be compact, stable, and forgiving | App shell, page templates, lists, tables, progress, and disclosure preserve predictable repeated-use patterns | Aligned |
| Health language must avoid diagnosis, prescription, shame, blame, and unsupported urgency | Overlays, feedback, empty states, unavailable states, and confirmations require calm, specific, non-blaming copy | Aligned |
| Consent, privacy, export, deletion, and notification controls must be understandable at decision time | Page templates, overlays, search, and disclosure patterns require impact context near sensitive actions | Aligned |
| Reports, insights, and health data views must expose source, timeframe, evidence, freshness, confidence, or limitations where relevant | Page templates, lists, tables, search result states, and disclosure patterns preserve evidence-bearing context | Aligned |

## Engineering Standards Alignment

| Engineering area | UI Pattern Expansion usage | Review decision |
| --- | --- | --- |
| Routing and navigation | App shell and navigation require route labels, recovery navigation, active states, deep-link behavior, and privacy-safe labels | Aligned |
| State management | Lists, tables, feedback, progress, and search patterns distinguish loading, stale, empty, unavailable, partial, permission-denied, and error states | Aligned |
| Data models and privacy | Lists, tables, reports, exports, search, filters, and query summaries require source, timeframe, state, and privacy-safe handling | Aligned |
| Testing and accessibility | Every new pattern includes acceptance criteria for keyboard, screen-reader, focus, motion, mobile, and non-color state behavior | Aligned |
| Security, privacy, observability, and release gates | Patterns identify review triggers for sensitive query terms, exports, consent, destructive actions, analytics, URLs, and screenshots | Aligned |
| Performance | Progress, disclosure, skeleton, search, and list patterns avoid layout instability and require slow/offline/partial-state review | Aligned |

## Documentation Site Brand Patch Alignment

| Site brand patch behavior | UI Pattern Expansion relationship | Review decision |
| --- | --- | --- |
| MkDocs uses the PL-OS lockup, Plectara favicon, and released brand tokens | Documentation site branding remains an implementation of released Brand and Design standards | Aligned |
| Site CSS avoids Google font fetches and uses platform fallbacks | UI Pattern Expansion continues to defer typography values to Brand Identity | Aligned |
| MkDocs theming is constrained by the static documentation framework | UI pattern standards do not assume MkDocs-specific classes or limitations for product UI | Aligned |
| Placeholder-derived logo assets are documented as non-production | Product UI patterns do not require final logo artwork to proceed with prototype structure | Aligned |

## Review Findings

- No v1.5.0 UI pattern document introduces conflicting brand colors, typography, logo rules, gradients, or AI color usage.
- The new patterns fill prototype-facing gaps without changing released Product Experience workflow intent.
- Navigation, page templates, lists, tables, overlays, feedback, search, filters, progress, and disclosure now expose state, privacy, accessibility, and recovery expectations before backend implementation.
- Sensitive health, consent, export, deletion, query, route, analytics, and screenshot behavior has clear review triggers.
- Engineering implementation remains responsible for actual route guards, state persistence, data classification, test coverage, performance budgets, and release gates.
- Future Flutter components, Widgetbook stories, interactive prototypes, token exports, and visual examples remain implementation artifacts outside this documentation release.

## Acceptance Criteria

- Reviewers can trace v1.5.0 UI pattern decisions back to released Brand, Product, Engineering, and documentation-site brand dependencies.
- Prototype screens can be assembled without introducing new brand values or product-policy decisions.
- UI states preserve health, privacy, consent, evidence, and recovery meaning before backend integration.
- Accessibility and non-color state cues are visible in every relevant pattern.
- Release metadata can show that cross-volume dependency review is complete before v1.5.0 promotion.

## References

- specs/01-brand/SPEC.md
- specs/01-brand/color-system.md
- specs/01-brand/design-tokens.md
- specs/01-brand/logo-usage.md
- specs/02-design/SPEC.md
- specs/02-design/token-alignment.md
- specs/02-design/app-shell-and-navigation.md
- specs/02-design/page-templates.md
- specs/02-design/lists-and-tables.md
- specs/02-design/overlays-and-feedback.md
- specs/02-design/search-filter-sort.md
- specs/02-design/progress-and-disclosure.md
- specs/03-product/SPEC.md
- specs/03-product/alignment-review.md
- specs/03-product/health-language.md
- specs/03-product/settings-and-consent.md
- specs/04-engineering/SPEC.md
- specs/04-engineering/alignment-review.md
- releases/v1.4.1/README.md

## Version History

- v1.5.0: Adds UI Pattern Expansion alignment review against Brand Identity v1.1.0, Product Experience v1.3.0, Engineering Standards v1.4.0, and documentation-site brand patch v1.4.1.
