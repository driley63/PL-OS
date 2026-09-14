# PL-OS v2.4.0 — Dark mode standards and app audit

Date: 2026-09-14
Status: Product owner approved publication through main and automatic deployment
Change class: Minor — additive design and engineering standards

## Added

- [Dark Mode & Accessibility](../../specs/02-design/dark-mode.md): WCAG 2.2 AA engineering target, native-software interpretation, approved surfaces, component states, transparency rules, focus, and charts.
- [140 component contrast checks](../../specs/02-design/plectara-component-contrast-report.md), alongside the existing 64 palette checks, plus six calculation and regression tests in CI.
- [Plectara Flutter source audit](../../specs/04-engineering/dark-mode-audit-2026-09-14.md) with six confirmed problem areas, source references, reproducible measurements, and prioritized remediation.
- [Expanded component samples](../../specs/02-design/plectara-component-preview.md) for inputs, validation, selection, focus, status badges, and charts.

## Changed

- Brand, Design, Engineering, and Flutter integration guidance now link to a shared dark mode contract.
- Theme integration guidance maps foreground/background pairs, surface levels, placeholders, error states, and chart roles explicitly.
- App testing guidance separates palette calculations, source findings, rendered components, and assistive-technology workflow evidence.

## Deprecated and removed

No APIs or brand assets are deprecated or removed by this release. Approved palette values, logo geometry, fonts, and packaged brand downloads retain their existing versions and contents.

## Consumer migration

Adopt the dark mode component/state matrix and resolve colors for the current theme. Replace light-only hints, health-state colors, and chart primitives in dark components. Validate custom surfaces and alpha layers against the actual content placed on them. Add real component tests in both themes and use the release evidence record for manual review.

The [audit remediation order](../../specs/04-engineering/dark-mode-audit-2026-09-14.md#remediation-order) identifies the app changes. The measured source revision is recorded in the audit; verify the current app revision before implementing fixes.

## Known limitations

This release publishes PL-OS standards and audit evidence. It does not modify or release the Plectara app. Device rendering, text scaling, VoiceOver/TalkBack, and other manual app workflow checks remain outstanding. Passing PL-OS color checks does not establish ADA compliance.

See the [release manifest](manifest.json) and [verification record](verification.md).
