# Brand Accessibility

Status: Released baseline with v2.4.0 dark mode addendum
Owner: Brand Working Group
Version: 1.0.0
Last updated: 2026-09-14

## Purpose

Defines accessibility expectations for brand use.

## Scope

- Plectara brand identity
- Digital product implementation
- Marketing and platform assets

## Requirements

- Product UI targets WCAG 2.2 AA, with WCAG2ICT interpretation for native software. Apply the [Dark Mode & Accessibility standard](../02-design/dark-mode.md) to both themes and every enabled component state.
- Color must not be the only signal for health state.
- AI, warning, danger, and success states require text or icon reinforcement.

## Implementation Guidance

- Use approved tokens and assets.
- Do not introduce one-off styling without an RFC.
- Update asset inventories and release notes when changing source assets.

## Acceptance Criteria

- The rule can be implemented in design and code.
- A reviewer can detect compliant and non-compliant usage.
- The standard maps to PL-OS Core.

## References

- adr/0001-adopt-lifestyleiq-name.md
- adr/0002-establish-brand-philosophy.md
- adr/0003-reserve-purple-for-ai.md
- [Current palette decision: ADR-0011](../../adr/0011-adopt-plectara.md)
- [Dark mode implementation decision: RFC-0006](../../rfc/0006-dark-mode-accessibility.md)

## Version History

- v2.4.0: Applies the dark mode component contract and current accessibility target; see RFC-0006.

- v1.0.0: Initial repository baseline.
