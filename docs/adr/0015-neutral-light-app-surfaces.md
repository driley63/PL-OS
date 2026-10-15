# ADR-0015: Neutral light-mode app surfaces

Status: Accepted for repository implementation
Date: 2026-10-15
Owner: Design System Working Group
Amends: [ADR-0014](0014-adopt-woven-app-visuals.md), light appearance only

## Context

The owner found that mint cards, mint navigation, and the woven background made light mode too green. The white selected controls were also unsatisfactory. The owner approved a mockup with ivory cards, warm-gray progress tiles, quieter outlines, and an ink selected navigation pill, then requested PL-OS updates. The owner explicitly required preservation of dark mode.

## Decision

Adopt the light-only palette and state contract in the [App Visual Specification](../specs/02-design/app-visuals.md). Use opaque ivory reading/navigation surfaces, warm-gray controls, neutral decorative outlines, and ink selections with white foregrounds. Keep teal primary actions, meaningful green status feedback, and the copper header rule. Quick Log remains secondary, with neutral backing, ink text and a tested slate outline.

Preserve the exact yarn, canonical logo, approved geometry, screen content, navigation behavior, foundation palette, capture-widget contract, and all dark color/state styling. Scope the restyle selectors and native overrides to light mode.

Honor PL-213's already approved 12-unit section gap in both themes. The tokens and written specification had been updated, but the HTML reference and screenshots still showed 20 units. Correct that stale reference spacing and regenerate both theme previews. Compare dark renders against the original reference with only the PL-213 spacing correction; the light restyle must introduce no additional dark changes. Keep the original previews in the unchanged v1 archive.

## Consequences

Publish visual kit v2 with updated light previews, references, app-local adapters, approval provenance, contrast evidence, and migration notes. Preserve the v1 archive and original approval history. This is an approved standards amendment pending the next PL-OS release; it does not itself update the consuming Flutter app or establish native accessibility compliance.

See [RFC-0009](../rfc/0009-neutral-light-app-surfaces.md) and [migration notes](../releases/unreleased.md).
