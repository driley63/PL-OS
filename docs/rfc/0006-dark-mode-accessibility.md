# RFC-0006: Dark Mode & Accessibility

Status: Accepted; included in PL-OS v2.4.0
Owner: Design System Working Group / Engineering Working Group
Date: 2026-09-14

## Problem

PL-OS has a validated palette but incomplete rules for component states, overlays, and added surfaces. The consuming Flutter app demonstrates that light-only hints, state colors, and chart primitives can persist inside a dark theme.

## Decision

The product owner authorized expansion of the dark mode standard and an app audit on 2026-09-14. Use WCAG 2.2 AA as the engineering target with WCAG2ICT interpretation for native software. Add a component/state contract, surface and transparency rules, chart treatments, regression checks, and a dated audit. Preserve approved brand primitives and component geometry.

## Implementation

- [Dark Mode & Accessibility](../specs/02-design/dark-mode.md)
- [Component contrast checks](../specs/02-design/plectara-component-contrast-report.md)
- [Flutter source audit](../specs/04-engineering/dark-mode-audit-2026-09-14.md)
- [App testing requirements](../specs/04-engineering/accessibility-testing.md)

The original 64 palette checks and released brand downloads remain the existing baseline. New component checks add coverage without changing the palette. The app audit records defects and migration actions; it does not certify a distributed build or implement the app fixes.

## Validation and release

Run the palette generator, component contrast checks, contrast regression tests, brand validator, and strict documentation build. Review the expanded preview in both themes. The product owner authorized pushing these changes to main for deployment on 2026-09-14. Publish with the v2.4.0 release; app remediation and device accessibility review require their own evidence.
