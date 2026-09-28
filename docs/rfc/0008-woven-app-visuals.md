# RFC-0008: Woven app visual specification

Status: Accepted for repository implementation
Owner: Design System Working Group
Date: 2026-09-28
Target bundle: v2.6.0

## Problem

The approved widget identity and the app's existing visual guidance diverge. A matching app proposal needs the app's actual information hierarchy and an implementable texture, header, card, divider, and theme contract.

## Accepted proposal

Use the approved saved yarn and canonical logo. Apply a horizontal ink header shade, soft copper rules, opaque mint light reading cards and opaque ink dark reading cards. Match the owner-supplied Today, Timeline, Charts, and Insights screenshots, including reminder/progress state, timeline metadata, chart controls/units, and rule-derived findings.

Record the shell-branding, card geometry, bounded progress-tile, contextual Today action, and chart-tone exceptions. Add eight populated screenshots, two empty-state screenshots, four comparison sheets, exact textures, fonts/licenses, app-local values and adapters, an offline reference, checksums, and migration guidance.

## Alternatives and limitations

- Header-only yarn and lifted dark cards are alternatives rather than the default.
- The earlier fictional dashboard content was replaced by screenshot-matched content.
- App reading cards are opaque in both themes; the separately approved dark widget action group remains transparent.
- Screenshot fixture values and the visually traced chart are not production data, clinical rules, or new logging requirements.
- Preview dialogs and controls do not define missing native workflows. Native implementation and app/device accessibility remain separate.

## Approval

The owner said “Looks great!” and requested PL-OS updates with screenshots and affected specifications on September 28. [ADR-0014](../adr/0014-adopt-woven-app-visuals.md) records the decision. See the [visual specification](../specs/02-design/app-visuals.md).
