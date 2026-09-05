# Volume 02 - Design Language Specification v2.0.0

Status: Approved for v2.0.0
Owner: Design System Working Group
Version: 2.0.0
Last updated: 2026-09-04

## Plectara color migration

Apply the v2.0.0 [semantic color roles](plectara-color-migration.md) to existing components. Shapes, spacing, type scale, motion, interaction, and Capture-first behavior remain unchanged. The [preview](plectara-component-preview.md) and [contrast results](plectara-contrast-report.md) document the local implementation.

## Purpose

Defines the visual and interaction system that Plectara product screens inherit. This volume translates the released Brand Identity standards into practical UI rules for layout, components, data visualization, motion, accessibility, and state handling.

## Scope

- Plectara product ecosystem
- PL-OS implementation guidance
- Future Flutter, web, and documentation artifacts
- Mobile app, web app, design files, and reusable component libraries
- Product surfaces that show health logs, summaries, trends, recommendations, and AI insights
- Compact capture surfaces such as widgets, shortcuts, and wearable entry points

## System Boundaries

Volume 02 covers:

- Spacing, layout, and responsive grid behavior
- Radius, elevation, containers, and visual layering
- Component taxonomy, buttons, inputs, cards, charts, icons, lists, tables, overlays, feedback, search, filters, progress, and disclosure
- App shell, navigation, page templates, and prototype-facing screen patterns
- Capture-first widget, shortcut, and compact surface behavior
- Motion rules and reduced-motion alternatives
- Product accessibility requirements

Volume 02 does not define brand identity, medical claims, AI recommendation policy, data architecture, or feature prioritization. Those decisions live in Brand Identity, Product Experience, AI, Engineering, and Governance volumes.

## Design Principles

- Use restrained UI structure for repeated daily workflows.
- Design compact surfaces for frictionless Capture before dashboard consumption.
- Reserve large brand expression for onboarding, empty states, app store assets, and milestone moments.
- Prefer scannable content, explicit labels, and predictable interaction patterns over decorative layouts.
- Keep AI-generated content visually distinct without using AI Purple as generic decoration.
- Make health data understandable without requiring color, animation, or chart expertise.

## Requirements

- Standards must map to implementation or reviewable behavior.
- Changes must remain consistent with PL-OS Core.
- Domain-specific behavior must consider accessibility, privacy, and user trust.
- Product UI must use Volume 01 color, typography, and token rules.
- Widgets and shortcuts must use released tokens and components while prioritizing Capture actions over charts, scores, and summaries.
- Components must identify default, hover, active, focus, disabled, loading, empty, error, and success states when applicable.
- Prototype-facing UI patterns must identify app shell, navigation, page template, collection, overlay, search, filter, sort, progress, and disclosure behavior where applicable.
- Patterns that affect health interpretation must include accessibility and evidence-review considerations.
- New interaction patterns must document mobile and web behavior.
- Design changes that alter released component behavior must update release notes.

## Core Token Dependencies

| Area | Depends on |
| --- | --- |
| Color | `docs/specs/01-brand/color-system.md` |
| Typography | `docs/specs/01-brand/typography.md` |
| Brand tokens | `docs/specs/01-brand/design-tokens.md` |
| Token alignment | `docs/specs/02-design/token-alignment.md` |
| Logo and icon use | `docs/specs/01-brand/logo-usage.md` and `docs/specs/01-brand/iconography.md` |

## Component Definition of Done

A Design Language component or pattern is complete when it defines:

- Purpose and intended use
- Anatomy and required content
- Variants and responsive behavior
- Interaction states
- Accessibility requirements
- Token dependencies
- Review criteria and known exceptions

## Implementation Guidance

- Use RFCs for uncertain additions.
- Create ADRs for accepted decisions with durable consequences.
- Update release notes when standards change.
- Prefer tokens and shared components over one-off local styling.
- Keep examples close to the pattern they describe.
- Avoid introducing production-only behavior that cannot be represented in design files.

## Acceptance Criteria

- A contributor can locate the relevant standard.
- A designer or engineer can apply the guidance consistently.
- Reviewers can identify when an exception needs documentation.
- Prototype screens can be assembled from documented app shell, navigation, page template, collection, overlay, search, filter, sort, progress, and disclosure patterns.
- Product surfaces can be checked against spacing, layout, component, state, motion, and accessibility standards.
- The design system can evolve without breaking Brand Identity constraints.

## References

- core/SPEC.md
- specs/01-brand/SPEC.md
- specs/01-brand/design-tokens.md
- specs/02-design/token-alignment.md
- specs/02-design/ui-pattern-alignment-review.md
- specs/02-design/capture-widgets.md
- specs/03-product/SPEC.md
- specs/04-engineering/SPEC.md

## Version History

- v1.7.0: Adds Capture-first compact surface and widget design requirements.
- v1.5.0: Adds cross-volume alignment review for UI Pattern Expansion dependencies.
- v1.5.0: Adds prototype-facing UI pattern standards for app shell, navigation, page templates, lists, tables, overlays, feedback, search, filters, sorting, progress, and disclosure.
- v1.2.0: Adds implementable Design Language standards and release checklist.
- v1.0.0: Initial repository baseline.
