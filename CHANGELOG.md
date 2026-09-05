# Changelog

All notable changes to PL-OS (formerly LIQ OS) are recorded in this file.

The format follows Keep a Changelog conventions and the project uses semantic versioning for published operating system releases.

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
