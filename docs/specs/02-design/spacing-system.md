# Spacing System

Status: Released
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-08-04

## Purpose

Defines the spacing scale, gutters, section rhythm, density rules, and review criteria for Plectara product interfaces.

## Scope

- Mobile and web product screens
- Documentation examples and product mockups
- Component library spacing aliases
- Dense health logs, cards, forms, charts, and AI insight surfaces

## Requirements

- Use a 4 px base grid for component spacing.
- Use semantic spacing tokens in implementation when they exist.
- Keep repeated health logging screens compact, but preserve enough space for scanning and touch accuracy.
- Use section spacing to show hierarchy instead of decorative dividers wherever possible.
- Do not use arbitrary one-off spacing values in production components without documenting the exception.

## Spacing Scale

| Token | Value | Primary use |
| --- | --- | --- |
| `space.0` | 0 px | Flush edges and intentional collapse |
| `space.1` | 2 px | Fine alignment, icon nudges, chart tick spacing |
| `space.2` | 4 px | Tight inline gaps |
| `space.3` | 8 px | Dense component internals |
| `space.4` | 12 px | Compact rows, tags, secondary controls |
| `space.5` | 16 px | Default component padding and mobile gutters |
| `space.6` | 20 px | Dense section spacing |
| `space.7` | 24 px | Standard section spacing and card groups |
| `space.8` | 32 px | Major content groups |
| `space.9` | 40 px | Page-level separation |
| `space.10` | 48 px | Large responsive sections |
| `space.11` | 64 px | Marketing or onboarding sections |

## Gutters and Containers

| Context | Default |
| --- | --- |
| Mobile screen gutter | 16 px |
| Compact mobile controls | 12 px only when touch targets remain valid |
| Tablet gutter | 24 px |
| Desktop content gutter | 32 px |
| Dense dashboard max width | 1280 px |
| Reading content max width | 760 px |

## Density Rules

- Daily logging, history, settings, and review screens may use compact spacing.
- Onboarding, explanation, empty states, and reports should use standard or spacious spacing.
- Health warnings and consent moments must not be visually crowded.
- Tables, lists, and timelines must preserve enough row height for labels, values, and state indicators.

## Implementation Guidance

- Map design tokens to CSS, Flutter, and Figma variables using the same scale.
- Prefer `space.5` for default mobile padding.
- Prefer `space.7` or `space.8` between major card groups.
- Avoid nested card padding that doubles visual whitespace.

## Acceptance Criteria

- Spacing values map to the approved scale or document an exception.
- Mobile screens remain usable without cramped touch targets.
- Dense screens remain scannable and do not depend on decoration for hierarchy.
- Designers and engineers can apply the same spacing names.

## References

- core/SPEC.md
- specs/01-brand/design-tokens.md
- specs/02-design/SPEC.md

## Version History

- v1.2.0: Adds spacing scale, gutters, density rules, and acceptance criteria.
- v1.0.0: Initial repository baseline.
