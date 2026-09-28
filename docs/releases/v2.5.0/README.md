# PL-OS v2.5.0 — Capture widget visual standards

Date: 2026-09-28
Status: Prepared; owner-approved design, publication pending
Change class: Minor — component-specific standards and assets

## Added

- [Widget Visual Specification](../../specs/02-design/capture-widget-visuals.md): family layouts, image crops, gradients, theme roles, typography, title case labels, actions, and native acceptance criteria.
- Six individual light/dark home screen screenshots, two review sheets, and a separate lock screen accessory concept.
- Exact saved full resolution PNG and embedded WebP texture, canonical logo copies, Inter, source records, and a [downloadable widget kit](../../assets/widgets/plectara/plectara-capture-widgets-v1.zip).
- Widget-local design values, source/delivery checksums, and browser verification evidence.
- [RFC-0007](../../rfc/0007-capture-widget-visuals.md) and [ADR-0013](../../adr/0013-adopt-capture-widget-visuals.md) recording the accepted direction and alternatives.

## Changed

- [Capture Widgets](../../specs/02-design/capture-widgets.md) now connects behavior to the approved visual contract and excludes an Edit action.
- Light widgets use a mint card with equally filled teal Capture/Sleep; dark widgets retain the transparent copper outlined grouping.
- The Buttons standard records the paired stable entry points as a component-specific exception.

## Consumer migration

1. Use the supplied gentle-focus texture and reproduce the reviewed crop for each native family.
2. Compose real logo artwork, live text, and native controls above it; do not flatten the widget into a screenshot.
3. Apply the widget-specific light/dark roles without changing global semantic tokens.
4. Use title case for English quick button labels and locale-appropriate display names.
5. Remove Edit from compact widget UI. Show saved confirmation only from acknowledged data.
6. Adapt to actual host bounds, text scaling, localization, system tint/clear, and accessory families.
7. Complete native/device accessibility and action-routing review before application release.

## Scope and limitations

This bundle updates PL-OS documentation and design assets. Native app code is not part of the change. The screenshot dimensions are illustrative, and the accessory concepts require separate implementation. Browser contrast checks do not establish ADA compliance or completed VoiceOver/TalkBack testing.

This release is prepared for review and has not been published by this record. See the [manifest](manifest.json) and [verification record](verification.md).
