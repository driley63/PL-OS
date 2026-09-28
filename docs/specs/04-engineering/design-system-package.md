# Design System Package

Status: Approved for PL-OS v2.6.0
Owner: Engineering Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines engineering standards for implementing and versioning shared design-system tokens, components, themes, and platform exports.

## Scope

- Flutter, web, and future platform design-system packages
- Brand tokens, design tokens, component APIs, documentation examples, and generated exports
- Consumer contracts for product teams

## Requirements

- Design-system packages must map to released Brand Identity and Design Language standards.
- Token exports must preserve semantic meaning across CSS, Flutter, Figma, iOS, and Android targets.
- Component APIs must prefer explicit variants over arbitrary styling escape hatches.
- Accessibility defaults must ship with components, not as downstream optional behavior.
- Breaking API or token changes must include migration guidance and release notes.
- Product-specific behavior must not be embedded inside foundation components.

## Package Contracts

| Contract | Requirement |
| --- | --- |
| Tokens | Source, generated output, owner, version, and platform mapping are documented |
| Components | Purpose, variants, states, accessibility behavior, and token dependencies are explicit |
| Themes | Brand and design values resolve through semantic tokens |
| Icons | Approved source, size, stroke, color alias, and accessible behavior are documented |
| Examples | Usage examples cover common states and misuse boundaries |

## Versioning Rules

- Adding a token, component, or optional variant is a minor change.
- Fixing implementation without changing public behavior is a patch change.
- Renaming, deleting, or changing visual meaning is potentially breaking.
- Generated outputs must identify the source revision or generation command.
- Consumers must not depend on internal implementation paths.

## Implementation Guidance

- Keep package public APIs small and reviewable.
- Use visual regression tests for component changes that affect layout or styling.
- Include accessibility and focus behavior in component stories or examples.
- Use lint rules or review gates to block raw token values where feasible.
- Document any temporary escape hatch with owner and expiry.

## Acceptance Criteria

- Product engineers can use components without private design context.
- Tokens and components trace back to released standards.
- Public API changes are versioned and documented.
- Accessibility defaults are testable.
- Consumers have migration notes when behavior changes.

## References

- core/SPEC.md
- specs/01-brand/design-tokens.md
- specs/02-design/SPEC.md
- specs/04-engineering/release-engineering.md

## Woven app component contract

The [App Visual Specification](../02-design/app-visuals.md) and [downloadable kit](../../assets/app/plectara/plectara-app-visuals-v1.zip) define a named app variant with exact artwork, color adapters, geometry aliases, screenshots, checksums, and bounded browser/color evidence. Prefer shared shell, reading-card, copper-rule, progress-group, row, chart and navigation components over per-screen styling.

Preserve actual routing, logging, clinical rules, evidence/source labels, theme preference and data state. Validate app-local colors/state layers and native focus/text scaling/target sizes in the consuming package. Screenshot heights, OS decoration, fixture data, and local preview dialogs are not runtime contracts. Record the consuming app's revision and device/accessibility evidence before release.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.4.0: Adds package contracts, token export rules, versioning, and acceptance criteria.
- v1.0.0: Initial repository baseline.
