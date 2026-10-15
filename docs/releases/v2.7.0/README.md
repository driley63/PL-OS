# PL-OS v2.7.0 — Neutral light-mode app surfaces

Date: 2026-10-15
Status: Approved release
Change class: Minor — revised app visual contract and implementation assets

## Changed

- Ivory reading cards and navigation, warm-gray progress tiles and controls, neutral decorative edges, and subtle light-card shadows.
- Ink selected navigation/filter/timeframe fills with white foregrounds, plus an ink selected navigation label.
- Neutral Quick Log backing and ink content; teal Log and semantic status colors remain.
- Preserve PL-213's 12-unit section gap. Correct the stale 20-unit gap in the reference and regenerate both theme previews; dark colors and component states remain unchanged.
- [Visual kit v2](../../assets/app/plectara/plectara-app-visuals-v2.zip), updated light previews/reference/adapters, [ADR-0015](../../adr/0015-neutral-light-app-surfaces.md), and preserved dark appearance.

## Added

- [RFC-0009](../../rfc/0009-neutral-light-app-surfaces.md), [ADR-0015](../../adr/0015-neutral-light-app-surfaces.md), migration guidance, 60 app-local contrast checks, and dark appearance/spacing regression evidence.

## Consumer migration

1. Import the v2 app-local values alongside the existing foundation palette. Do not replace global brand tokens or capture-widget colors.
2. Apply changed fills and decoration only to the light branch. Keep the existing dark palette, component foregrounds, elevations, and state layers intact.
3. Update selected fill and foreground together. Ink selected controls require `onSelected` white; the navigation label below the pill uses `selectedLabel` ink. Retain checks, shape, and programmatic selection.
4. Separate attention backing from the selected-control `soft` role. In light mode `soft` now means ink selection; attention uses `attentionBacking` ivory. Do not put dark attention text on ink. Keep dark attention on its existing `soft` backing.
5. Use neutral decorative borders only on reading groups and display-only metric tiles. Keep the tested slate outline for inputs and interactive secondary controls. Preserve focus feedback independently of selection.
6. Keep real app content and canonical logo/texture. The approved concept is visual evidence, not a production raster asset. Preserve native safe-area and floating-action clearance.
7. Verify light default/selected/pressed/disabled/focus states and large text. Compare all four dark screens, dialogs, and System/Light/Dark transitions against the previous build before shipping the consuming app.

The PL-OS reference checks do not certify the separate native application. This update does not merge, deploy, or release that application.

## Deprecated / removed

None. The historical v1 visual kit, canonical artwork, foundation palette, and capture-widget contract remain available.

## Scope and limitations

The owner authorized push and publication on October 15, 2026. This release covers PL-OS specifications and assets. Native integration, native state-layer checks, device behavior, and assistive-technology validation remain separate. Preview values are review fixtures rather than production defaults.

See the [manifest](manifest.json) and [verification record](verification.md).
