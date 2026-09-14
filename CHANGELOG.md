# Changelog

All notable changes to PL-OS (formerly LIQ OS) are recorded in this file.

The format follows Keep a Changelog conventions and the project uses semantic versioning for published operating system releases.

## [v2.4.0] - 2026-09-14

### Added

- Dark Mode & Accessibility standard with a WCAG 2.2 AA engineering target, native-software interpretation, surface rules, component states, chart treatments, and app release evidence requirements.
- 140 component contrast checks covering both themes, selected surfaces, placeholders, state labels, control indicators, charts, and filled actions; six calculation and regression tests in CI.
- Dated Plectara Flutter source audit with measured failures, exact source references, reproducible fixtures, and prioritized remediation.
- Expanded interactive component samples for inputs, selected controls, status badges, focus, and charts.

### Changed

- Link Brand, Design, Engineering, and Flutter integration guidance to the dark mode contract; distinguish WCAG thresholds from PL-OS platform sizing and focus conventions.
- Preserve the approved palette, logo assets, and released download packages. App remediation and device accessibility verification remain separate from this standards update.

## [v2.3.0] - 2026-09-11

### Added

- Native Android VectorDrawable foreground and matching monochrome silhouette for themed launcher icons.
- Standard and round adaptive icon definitions for Android 8+ and themed definitions for Android 13+.
- 21 shape/appearance examples as SVG and PNGs at 1024, 192, and 48 px, with individual gallery downloads.
- Dedicated Android ZIP, source provenance, per-file checksums, and consumer integration guidance.
- Geometry, placement, safe-circle, resource-reference, preview, legacy-density, and package validation.

### Changed

- Apply the owner-approved Android size and placement: about 13% larger, with unchanged ribbon geometry and colors.
- Replace the five density-specific foreground PNGs with native vectors and refresh standard/round legacy icons.
- Include the Android kit in the complete brand download and refresh current release and platform usage guidance.

## [v2.2.0] - 2026-09-11

### Added

- Native Liquid Glass iOS app icon built from seven unchanged Plectara vector layers.
- Six Apple-rendered appearance previews at 1024 px, 60 pt at 3×, and 20 pt at 3×.
- Editable Icon Composer document, SVG layers, native render manifest, and standalone iOS ZIP download.
- A six-appearance gallery with individual PNG downloads and Xcode integration guidance.
- Validation of original geometry, layer references, native render checksums, transparent corners, and package/site parity.

### Changed

- Extend the brand rules with an approved native iOS material treatment and system-managed clear/tinted appearances.
- Refresh brand-kit packaging, inventory, and release documentation; preserve the flat logo masters and legacy platform catalog.

## [v2.1.0] - 2026-09-07

### Changed

- Standardize the head as jade `#76B7A5` in every full-color Plectara logo, on light and dark backgrounds.
- Define ink lettering on light backgrounds, white lettering on dark backgrounds, and one consistent fill throughout each monochrome logo.
- Refresh current source artwork, PNGs, social graphics, brand board, asset inventory, site copies, and brand-kit ZIP.

### Added

- A gallery of nine logo, standalone-symbol, and lettering treatments with direct SVG and transparent PNG downloads.
- A white outlined wordmark and reusable PNG lettering exports.
- Automated checks for full-color head consistency, monochrome fills, lettering colors and geometry, PNG transparency, and downloadable-file parity.
- v2.1.0 release notes and migration guidance for existing asset consumers.

## [v2.0.0] - 2026-09-04

### Changed

- Adopt Plectara and PL-OS for current product and operating-system naming; preserve the LIQ-OS repository slug and historical records.
- Apply owner-approved woven-person artwork with consistent gaps and restored outlined lettering.
- Replace the legacy lime gradient with the Plectara palette and theme-specific component colors.
- Preserve the existing component language, typography, spacing, radii, and interaction standards.

### Added

- SVG/PNG logo set, platform icons, social assets, and downloadable brand kit.
- CSS and Flutter color adapters with legacy compatibility names.
- Light/dark component preview and 64 passing palette contrast checks.
- ADR-0011, ADR-0012, migration guidance, and a local v2.0.0 manifest.

Publication uses the existing repository and Amplify deployment workflow. No repository rename or legal registration is included.

## [v1.7.0] - 2026-08-20

### Added

- Capture-first standards for home screen widgets, lock screen widgets, shortcuts, wearable surfaces, and compact launch surfaces.
- One-tap, guided, and freeform Capture behavior with success, correction, unavailable, and permission-limited states.
- Adaptive Capture rules based on frequency, recency, time, context, sequence, and user control.
- Capture, Habits, and Insights as the connected LifestyleIQ Product Experience pillars.
- The One Sentence Test as a required feature-proposal gate.
- Release notes, manifest, and checklist for v1.7.0.

### Changed

- Design Language now requires compact surfaces to prioritize Capture over dashboards, scores, charts, and summaries.
- Product Experience now defines the evolution from new captures to Favorite Captures, learned habits, and dormant habits.
- Product Philosophy now requires features to increase user understanding while fitting naturally into the user's routine.
- Insights guidance now explicitly connects evidence and interpretation to captured observations and learned habits.

### Deprecated

- None.

### Removed

- None.

## [v1.0.1] - 2026-08-03

### Fixed

- Removed duplicated canonical Markdown folders from the repository root.
- Made `docs/` the single canonical Markdown source for MkDocs publishing.
- Removed the root-level `docs/README.md` conflict that triggered MkDocs warnings.
- Updated Amplify build instructions to avoid virtual-environment path failures.

### Added

- ADR-0009 documenting the `docs/`-canonical documentation publishing model.
- Release notes and manifest for v1.0.1.
- CI validation that checks repository layout and runs `mkdocs build --strict`.

### Changed

- Root `README.md` now focuses on repository operations and deployment.
- `mkdocs.yml` now documents the single-source `docs/` architecture.

## [v1.0.0] - 2026-08-02

### Added

- Initial LIQ OS repository structure.
- LIQ OS Core specification and constitutional governance.
- Brand Identity, Design Language, Product Experience, Engineering, AI, Architecture, Marketing, and Governance specification volumes.
- Initial ADR set for name, philosophy, AI color reservation, signature gradient, versioned OS model, Markdown-first source, Inter typography, and GitHub-ready documentation.
- Initial RFC set for typography, component library, Flutter design system, AI insight model, and documentation publishing.
- MkDocs configuration for static documentation publishing.
- GitHub issue templates, pull request template, CODEOWNERS placeholder, and CI workflow.
- Brand assets and design-token placeholders.

### Baseline Decisions

- Product name: LifestyleIQ.
- Internal system name: LifestyleIQ Operating System (LIQ OS).
- Philosophy: "Translating daily habits into a plan towards optimal health."
- Signature palette: Fresh Lime to Evergreen gradient.
- AI accent: Purple reserved for AI-generated insights and machine-learning behavior.
