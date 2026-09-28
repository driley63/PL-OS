# RFC-0007: Capture widget visual specification

Status: Accepted for repository implementation
Owner: Design System Working Group
Date: 2026-09-28
Target bundle: v2.5.0, prepared

## Problem

The existing Capture Widgets standard defines purpose and behavior but lacks an implementable visual contract, screenshots, and a packaged background asset. Earlier mockups also show an Edit control that will not exist in production.

## Accepted proposal

Adopt the owner-reviewed revision 13: whole-widget woven yarn, gentle focus progression, horizontal logo shading, a soft copper divider, one mint light card or transparent dark card, paired teal/white light Capture and Sleep buttons, title case quick labels, and saved confirmation without Edit. Preserve canonical logos and readable controls.

Publish an individual light/dark screenshot for each home screen size, a separate accessory concept, full resolution and exact delivery textures, provenance, design values, and a browser reference. Record layout and contrast review separately from native/device accessibility evidence.

## Alternatives considered

- Header-only yarn: retained as an earlier fallback in the review archive.
- Whole-widget texture washed out in light mode: replaced with vibrant yarn and an opaque mint action card.
- Strong defocus on the left: replaced with the accepted gentler-focus derivative.
- Ivory card and mint Sleep: replaced with mint card and matching teal Capture/Sleep in light mode.
- A widget Edit action: removed at the owner's explicit direction.

## Approval and scope

The owner approved the final visual refinements and requested inclusion in PL-OS with screenshots, texture files, and written specifications on September 28. This approval authorizes documentation and asset integration. It does not assert native implementation or completed publication.

See [ADR-0013](../adr/0013-adopt-capture-widget-visuals.md), the [visual specification](../specs/02-design/capture-widget-visuals.md), and [prepared release notes](../releases/v2.5.0/README.md).
