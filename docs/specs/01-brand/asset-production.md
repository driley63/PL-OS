# Asset Production

Status: Approved for PL-OS v2.1.0
Owner: Brand Working Group
Version: 2.1.0
Last updated: 2026-09-07

## Purpose

Defines required asset export sets for app, web, social, and presentation use.

## Scope

- Plectara brand identity
- Digital product implementation
- Marketing and platform assets
- App store, favicon, launcher, social, press, and documentation assets

## Requirements

- Maintain SVG masters.
- Generate PNG exports at platform-required sizes.
- Keep app icon source separate from masked platform outputs.
- Document every generated asset in an inventory.
- Production assets must identify source file, export process, owner, date, and intended surfaces.
- Placeholder assets must be labeled as placeholders until final optical refinement is approved.
- Generated assets must not become the source of truth for future edits.

## Source Locations

| Path | Role |
| --- | --- |
| `assets/brand/plectara/source/` | Owner-approved SVG masters and outlined lettering |
| `assets/brand/plectara/png/` | Generated PNG, favicon, and platform outputs when checked in |
| `assets/brand/plectara/platform/ios/` | iOS `AppIcon.appiconset` outputs when checked in |
| `assets/brand/plectara/platform/android/` | Android adaptive and legacy icon outputs when checked in |
| `assets/brand/plectara/inventory.json` | Asset inventory when production exports exist |

The approved Plectara output set is present and reproducible. Archived placeholders remain separately in `assets/brand/logos/`; they must not be used as new production sources.

## Required Export Set

| Surface | Required output |
| --- | --- |
| Source review | SVG master with accessible title |
| Web header | Horizontal SVG, full color and reversed |
| Reusable logo samples | Transparent SVG/PNG downloads: color with ink/white lettering, ink/white monochrome, three standalone symbols, and ink/white outlined lettering |
| Favicon | 16, 32, and 48 px PNG or ICO-derived outputs |
| PWA manifest | 192 and 512 px PNG |
| iOS app icon | Complete `AppIcon.appiconset`, generated from unmasked 1024 px source |
| Android launcher | Adaptive foreground/background plus legacy PNG densities |
| Social avatar | 1024 px rounded avatar; square icons also provided at 512 and 1024 px |
| Press kit | SVG, 1024 px PNG, and monochrome variants |

## Inventory Requirements

Each production asset inventory entry must include:

- Asset name
- Source path
- Generated path
- Version or commit SHA
- Export size and format
- Intended surfaces
- Owner
- Review date
- Notes for safe-area, contrast, or platform masking

## Quality Gates

- SVG masters must be optimized only after visual review.
- PNG exports must be generated from source SVG or source design file.
- App icon safe areas must be checked against platform masks.
- Dark-mode and light-mode logo variants must be tested on approved backgrounds.
- Every full-color figure must have a jade `#76B7A5` head. Monochrome figures and lettering must share one ink or white fill.
- Site downloads must match the generated source/PNG files and complete brand-kit ZIP.
- Any placeholder asset shipped in docs must be explicitly labeled.

## Implementation Guidance

- Keep source artwork and generated exports in separate directories.
- Include scripts or documented steps for repeatable export generation before final production handoff.
- Do not overwrite source assets without preserving review context in Git history.
- Update release notes whenever export requirements or source assets change.

## Acceptance Criteria

- A reviewer can trace every generated asset back to a source.
- Platform-specific outputs can be regenerated.
- Placeholder and production assets are clearly distinguishable.
- App, web, social, and press surfaces have complete export requirements.

## References

- adr/0001-adopt-lifestyleiq-name.md
- adr/0002-establish-brand-philosophy.md
- adr/0003-reserve-purple-for-ai.md
- adr/0004-adopt-green-teal-gradient.md

## Version History

- v1.1.0: Adds source locations, export sets, inventory requirements, and quality gates.
- v1.0.0: Initial repository baseline.
