# RFC-0009: Neutral light-mode app surfaces

Status: Accepted for repository implementation
Owner: Design System Working Group
Date: 2026-10-15

## Problem and accepted proposal

Large mint surfaces compound the green woven background, while white selected controls lack a clear visual hierarchy. Replace light reading/navigation surfaces with warm ivory; use warm gray for inset tiles and secondary controls, quieter neutral decorative borders, and ink selections with white foregrounds. Preserve teal primary actions, semantic status feedback, the canonical artwork, and the existing layout.

Pure white cards were considered. The approved warm ivory direction is softer alongside the yarn and existing copper accent. The owner approved the mockup and requested the PL-OS update. Dark mode must remain unchanged.

## Acceptance

The [App Visual Specification](../specs/02-design/app-visuals.md) defines exact values and migration requirements. [ADR-0015](../adr/0015-neutral-light-app-surfaces.md) records the accepted decision. Validate light selected foregrounds and required outlines, preserve dark tokens/styling, and compare all rendered dark reference states. Honor PL-213's 12-unit section gap in both themes and correct the reference's stale 20-unit spacing; retain historical previews in the v1 archive. Native implementation remains separate.
