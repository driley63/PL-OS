# Page Templates

Status: Approved for PL-OS v2.6.0
Owner: Design System Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines reusable page templates for Plectara product screens so rapid prototypes, design files, and future implementation work share the same structure before backend details are finalized.

## Scope

- Dashboard, detail, form, report, settings, onboarding, and empty-state page templates
- Page header structure, content regions, primary actions, secondary actions, and responsive behavior
- Prototype-facing layout decisions that should remain stable as implementation matures

## Requirements

- Page templates must use released Brand Identity tokens and Design Language spacing, radius, elevation, and component rules.
- Each page should expose one primary user intent.
- Health data pages must show source, timeframe, freshness, or unavailable state where relevant.
- Privacy, consent, export, deletion, and AI-related actions must remain explicit and reviewable.
- Templates must define mobile and desktop behavior before production implementation.
- Page sections should use hierarchy, spacing, and headings before decorative separators.

## Template Types

| Template | Purpose | Required regions |
| --- | --- | --- |
| Dashboard | Daily overview and high-priority health context | App context/title where present, primary summary, key cards, timeline preview, recovery states |
| Detail page | Focused view of one record, insight, report, or setting | Header, metadata, content body, related actions, audit or source context |
| Form flow | Create, edit, consent, onboarding, or preference workflows | Step context, fields, validation, primary action, safe cancellation |
| Report page | Long-form interpretation, export, and sharing review | Summary, evidence sections, charts/tables, limitations, export controls |
| Settings page | Account, consent, integrations, notifications, privacy | Grouped settings, current state, impact copy, confirmation paths |
| Empty-state page | First-run, missing data, unavailable data, or blocked route | Explanation, next action, optional education, recovery support |

## Page Anatomy

A page may include:

- App shell or navigation context
- Page title and optional eyebrow
- Short summary or current state
- One primary action
- Secondary actions or overflow menu
- Content sections with headings
- Cards, lists, charts, tables, or forms
- Empty, loading, error, stale, or permission-denied state
- Footer metadata, source, or version context where relevant

## Responsive Behavior

| Breakpoint | Structure |
| --- | --- |
| Mobile | Single column, top context, primary action near task completion, bottom navigation when applicable |
| Tablet | Optional secondary column for contextual content or navigation |
| Desktop | Multi-column dashboard or detail layouts with stable content order |

Content order must preserve meaning across breakpoints. Do not move consent, warning, or limitation context away from the action it qualifies.

## Implementation Guidance

- Start prototypes from the closest template before inventing page structure.
- Use full-width sections or unframed regions for page-level grouping; do not nest cards as layout scaffolding.
- Keep repeated daily workflows compact and predictable.
- Use cards for bounded items, not for every section.
- Place destructive, privacy-sensitive, or export actions near impact explanation.
- Document any page template exception with reason, affected breakpoint, and review owner.

## Acceptance Criteria

- Designers and engineers can select a page template without private context.
- Page hierarchy is clear without relying on decorative gradients or heavy shadows.
- Primary, secondary, destructive, privacy-sensitive, and AI-specific actions are distinguishable.
- Mobile and desktop layouts preserve content meaning and action context.
- Empty, loading, error, stale, and permission-denied states are accounted for.

## References

- specs/02-design/layout-grid.md
- specs/02-design/spacing-system.md
- specs/02-design/radius-and-elevation.md
- specs/02-design/cards.md
- specs/02-design/empty-error-loading-states.md
- specs/03-product/reports.md
- specs/03-product/settings-and-consent.md

## Reviewed app templates

The [App Visual Specification](app-visuals.md) is the current reference for Today, Timeline, Charts, and Insights. Today uses the branded header without an extra page title/date, the actual optional reminder/progress/findings state, and Log/Quick Log actions. Empty Today preserves its four screenshot sections. Timeline uses filters and one row panel; Charts retains selectors, summaries and units; Insights keeps device/source explanation, warning context and goal evidence.

Use the woven shell and opaque reading surfaces for other existing routes while preserving their product contracts. The four screenshots do not define unseen forms, settings options, graph data, or workflows. Scaled/localized content reflows; native floating actions reserve safe-area/content clearance.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.5.0: Adds page template standards for prototype and implementation alignment.
