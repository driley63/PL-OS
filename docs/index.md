# PL-OS

Plectara Operating System (PL-OS) is the canonical source of truth for Plectara's brand, design language, product experience, engineering standards, AI behavior, and release governance.

## Current Version

- Version: v2.6.0
- Status: Approved v2.6.0 release
- Prepared: 2026-09-28
- Product name: Plectara
- Operating system name: PL-OS
- Design philosophy: "Translating daily habits into a plan towards optimal health."

[Download logo samples](specs/01-brand/plectara-brand-kit.md){ .md-button .md-button--primary }
[Preview component colors](specs/02-design/plectara-component-preview.md){ .md-button }

PL-OS now includes a [Dark Mode & Accessibility standard](specs/02-design/dark-mode.md), 140 component contrast checks, and a [Plectara app source audit](specs/04-engineering/dark-mode-audit-2026-09-14.md). Read the [v2.4.0 changes](releases/v2.4.0/README.md). Android icons, Liquid Glass iOS icons, and the established logo library remain available in the [brand kit](specs/01-brand/plectara-brand-kit.md).

## Capture widget design update

The [Capture Widget Visual Specification](specs/02-design/capture-widget-visuals.md) includes light/dark screenshots for Small, Medium, and Large, the exact background texture, component design values, source records, and a downloadable implementation kit. See the [v2.5.0 release notes](releases/v2.5.0/README.md). Native app implementation remains separate.

## App visual standards update

The [App Visual Specification](specs/02-design/app-visuals.md) extends the approved woven styling to Today, Timeline, Charts, and Insights. It includes light/dark screenshots matched to the actual app, exact yarn and logo files, theme and geometry values, an offline reference, a downloadable kit, and updates to affected component and product guidance. See the [v2.6.0 release notes](releases/v2.6.0/README.md).

## Documentation Source

The canonical Markdown source for the published documentation site lives under `docs/`.

- `docs/core/`: PL-OS Core
- `docs/specs/`: specification volumes
- `docs/adr/`: decision records
- `docs/rfc/`: proposals
- `docs/playbook/`: operating guidance
- `docs/releases/`: release manifests and notes

Repository-root files such as `README.md`, `mkdocs.yml`, `amplify.yml`, and `.github/workflows` are operational files, not duplicated canonical specification content.
