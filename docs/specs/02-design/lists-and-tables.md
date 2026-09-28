# Lists and Tables

Status: Approved for PL-OS v2.6.0; publication pending
Owner: Design System Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines standards for lists, rows, tables, grouped collections, and timeline-like data displays in Plectara product interfaces.

## Scope

- List rows, grouped lists, timeline rows, table rows, compact data rows, and collection controls
- Health logs, history, settings, integrations, reports, exports, and prototype data views
- Selection, sorting, filtering, pagination, empty rows, loading rows, and responsive table alternatives

## Requirements

- Use lists for scannable collections and tables for structured comparisons.
- Health data collections must make date, source, status, and unavailable values explicit where relevant.
- Tables must not be the only way to understand critical health information on mobile.
- Row actions must be explicit and accessible.
- Selection, loading, empty, warning, stale, and error states must be visible without color alone.
- Dense collections must preserve readable labels and minimum interaction targets.

## Pattern Selection

| Need | Preferred pattern | Avoid |
| --- | --- | --- |
| Repeated records with short metadata | List row or grouped list | Overly complex card grids |
| Time-ordered health history | Timeline row or grouped date list | Dense calendar-only views without text |
| Side-by-side numeric comparison | Table or metric row group | Horizontal scrolling without labels |
| Settings or integrations | Settings list or grouped panel | Hidden controls inside generic rows |
| Export preview | Table with fallback summary | Chart-only or color-only representation |
| Mobile dense data | Stacked rows or summary/detail pattern | Shrinking desktop tables below legibility |

## Row Anatomy

A row may include:

- Leading icon, status marker, or avatar when useful
- Primary label
- Secondary metadata
- Value or summary
- Timeframe, source, or freshness indicator
- Status text
- Selection affordance
- Primary row action
- Overflow menu for secondary actions

Do not rely on swipe gestures or hidden overflow for destructive or privacy-sensitive actions.

## Table Anatomy

Tables should define:

- Caption or accessible label
- Column headings
- Row headings where useful
- Units and date/time formats
- Sort state
- Empty, loading, filtered-empty, and error rows
- Mobile fallback behavior
- Export behavior when table content leaves the product

## States

| State | Requirement |
| --- | --- |
| Loading | Preserve row or table layout with skeletons when dimensions are known |
| Empty | Explain whether data has not been logged, imported, synced, or permitted |
| Filtered empty | Show that data exists but is hidden by current filters |
| Stale | Show last successful update and recovery path |
| Error | Preserve user context and provide remediation |
| Selected | Use checkbox, text, or layout cue in addition to color |

## Implementation Guidance

- Use spacing tokens to keep row density consistent.
- Keep rows at least 44 px tall when interactive on touch devices.
- Use `radius.0` for dense tables and `radius.2` for bounded list panels.
- Keep sortable column labels visible and keyboard accessible.
- Provide summary text before dense tables in reports.
- Use synthetic data in prototypes and screenshots.

## Acceptance Criteria

- Users can scan records without losing source, date, or status context.
- Collection states distinguish no data, filtered data, stale data, unavailable data, and failed loading.
- Mobile alternatives preserve meaning without cramped tables.
- Row and table actions are accessible and recoverable.
- Health data values are not implied by blank cells unless the meaning is explicitly defined.

## References

- specs/02-design/spacing-system.md
- specs/02-design/radius-and-elevation.md
- specs/02-design/cards.md
- specs/02-design/accessibility.md
- specs/03-product/daily-logging.md
- specs/03-product/health-timeline.md
- specs/03-product/reports.md

## Woven app Timeline

Follow the [App Visual Specification](app-visuals.md): one opaque themed collection panel, leading category icons, entry name, multiline date/type/value metadata, explicit labeled delete controls, and decorative soft copper row rules. Category labels and selected filters remain visible. Do not infer the full logging catalog from the screenshot's visible filter row.

Preserve the app's actual deletion confirmation, edit behavior, and recovery path. The review's local dialog is illustrative. Owner-supplied screenshot content may be retained in an explicitly approved visual reference; record that approval and identify it as a review fixture. Do not assert synthetic/anonymized provenance without evidence or use fixture records in production accounts.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.5.0: Adds list, table, row, and collection-state standards.
