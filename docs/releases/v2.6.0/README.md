# PL-OS v2.6.0 — Woven app visual standards

Date: 2026-09-28
Status: Approved standards; release candidate, publication pending
Change class: Minor — additive app visual variant and implementation assets

## Added

- [App Visual Specification](../../specs/02-design/app-visuals.md) for screenshot-matched Today, Timeline, Charts, and Insights in light and dark mode.
- Eight populated-screen screenshots, two empty Today screenshots, four comparison sheets, and an offline-capable editable reference.
- Exact saved yarn textures, canonical logo, fonts/licenses, source records, app-local design values, CSS/Flutter color adapters, checksums, contrast fixtures, and a [downloadable kit](../../assets/app/plectara/plectara-app-visuals-v1.zip).
- [RFC-0008](../../rfc/0008-woven-app-visuals.md), [ADR-0014](../../adr/0014-adopt-woven-app-visuals.md), packaging validation, and migration guidance.

## Changed

- Design Language now permits the approved woven shell on daily app screens and defines app-local geometry rather than silently changing foundation scales.
- Shell/navigation, cards, buttons, charts, lists, filters, page templates, spacing, radius, overlays, and theme guidance point to the approved app composition.
- Brand token/color and Flutter integration guidance explain the local app aliases and tested opaque reading surfaces.
- Product Timeline/Insights and AI visual guidance preserve real content, source badges, evidence, units, and health-rule state while applying the new visual treatment.

## Migration

1. Integrate the exact texture, shaded header, copper rules, and themed reading cards into shared native shell components.
2. Use the local values and adapters alongside foundation tokens. Keep real app content, navigation, clinical rules, and capture workflows.
3. Reproduce the bounded progress group, category list rows, chart controls/units, source badges, and warning context.
4. Respect safe areas, theme preferences, text scaling, localization, focus, and native target sizes. Reserve clearance for floating actions.
5. Complete native/device and assistive-technology review before releasing the app.

## Deprecated / removed

None. The approved widget kit and historical release artifacts remain available.

## Scope and limitations

The owner approved the visual direction and PL-OS integration. This candidate updates standards and reference assets; it does not ship Flutter app changes. Screenshot values are review fixtures, the symptom chart is visually traced, and unseen content/workflows are not inferred. Color and browser checks do not establish ADA compliance. Main-branch publication and live hosting verification remain separate from this preparation.

See the [manifest](manifest.json) and [verification record](verification.md).
