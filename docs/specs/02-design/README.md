# Volume 02 - Design Language

Volume 02 defines the visual and interaction system that Plectara product screens and compact capture surfaces inherit.

## Status

- Current milestone: v2.6.0 approved woven app visual variant
- Owner: Design System Working Group
- Dependency: Volume 01 Brand Identity v2.0.0
- Release type: minor, additive app visual standards over the existing component and capture baselines

## Plectara migration

The [color migration](plectara-color-migration.md) changes theme roles, not the component library. Review the [live samples](plectara-component-preview.md) in both themes.

## Purpose

The Design Language translates Brand Identity into product UI rules. It establishes how screens should be spaced, structured, layered, controlled, visualized, animated, and reviewed before implementation in Flutter, web, design files, and documentation examples.

## Principles

- Calm density: screens should be efficient without feeling cramped.
- Clear hierarchy: primary actions, insight states, and health context must be easy to scan.
- Capture-first compact surfaces: widgets and shortcuts should record user behavior before presenting summaries.
- Evidence-friendly UI: charts, cards, and states should make data interpretation clear.
- Accessible by default: color, motion, focus, and touch targets must work for diverse users.
- Controlled shell branding: the approved woven app and widget shells carry the identity; repeated reading surfaces keep content quiet and readable.

## Document Map

- `SPEC.md`: volume scope, system boundaries, requirements, and definition of done
- `token-alignment.md`: review matrix for Volume 02 dependencies on released Brand Identity tokens
- `ui-pattern-alignment-review.md`: cross-volume review for v1.5.0 prototype-facing UI pattern standards
- `spacing-system.md`: spacing scale, gutters, section rhythm, and density rules
- `layout-grid.md`: responsive structure, content widths, and page organization
- `radius-and-elevation.md`: surface shape, depth, and layering rules
- `component-taxonomy.md`: component classes, owners, required records, and governance
- `buttons.md`: action hierarchy, variants, sizing, labels, and states
- `inputs.md`: field types, anatomy, validation, and health-entry ergonomics
- `cards.md`: card roles, anatomy, visual rules, and interaction states
- `charts.md`: chart selection, visual encoding, evidence context, and accessibility
- `motion.md`: duration, easing, reduced-motion behavior, and state transitions
- `accessibility.md`: product accessibility checks and health UX requirements
- [Dark Mode & Accessibility](dark-mode.md): surfaces, component states, charts, theme migration, and measurable review criteria
- [Component contrast checks](plectara-component-contrast-report.md): 140 tested uses of current semantic colors
- `empty-error-loading-states.md`: async, unavailable, and recovery state rules
- `iconography.md`: product icon style, usage, labels, and AI icon behavior
- [Capture Widgets](capture-widgets.md): Capture-first widget, shortcut, wearable, and adaptive surface rules
- [Widget Visual Specification](capture-widget-visuals.md): approved woven backgrounds, family/theme screenshots, local design values, downloadable assets, and native implementation criteria
- [App Visual Specification](app-visuals.md): approved screenshot-matched app layouts, light/dark surfaces, yarn, header, rules, downloadable assets, and migration requirements
- `app-shell-and-navigation.md`: app shell, navigation, route labels, and wayfinding rules
- `page-templates.md`: reusable dashboard, detail, form, report, settings, and empty-state templates
- `lists-and-tables.md`: collection, row, table, and responsive data-display rules
- `overlays-and-feedback.md`: modal, sheet, dialog, banner, toast, and confirmation rules
- `search-filter-sort.md`: search, filter, sort, query summary, and result-state rules
- `progress-and-disclosure.md`: progress, skeleton, stepper, accordion, and progressive-detail rules

## Acceptance Criteria

- A designer can produce consistent Plectara screens without private context.
- An engineer can map UI decisions to tokens, components, and reviewable behavior.
- Reviewers can identify when a UI change needs an exception, RFC, ADR, or release note.
- Screens remain usable for daily, repeated health workflows across mobile and web.
