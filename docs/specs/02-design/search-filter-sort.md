# Search, Filter, and Sort

Status: Released
Owner: Design System Working Group
Version: 1.5.0
Last updated: 2026-08-04

## Purpose

Defines search, filter, sort, and query-state standards for Plectara product surfaces that help users browse health logs, timelines, insights, reports, settings, and support content.

## Scope

- Search inputs, filter chips, filter panels, sort controls, saved filters, query summaries, and result states
- Health records, reports, insights, timelines, exports, settings, and documentation examples
- Empty, filtered-empty, loading, stale, unavailable, permission-denied, and error states

## Requirements

- Search must preserve user-entered text and current context when results fail or loading is delayed.
- Filters and sorting must make the current result scope visible.
- Health-sensitive filters must avoid implying diagnosis, causation, or unsupported certainty.
- Filtered-empty states must distinguish no matching results from no available data.
- Privacy-sensitive query terms must not be written to logs, analytics, URLs, or screenshots without review.
- Sort and filter controls must be accessible by keyboard and screen reader.

## Pattern Selection

| Pattern | Use | Requirements |
| --- | --- | --- |
| Search input | Free-text lookup across known content | Visible label, clear action, loading and no-results state |
| Filter chip | One active, removable constraint | Readable label and clear selected state |
| Filter panel | Multiple constraints or advanced options | Apply/reset behavior and result summary |
| Sort menu | Stable ordering choices | Current sort visible after menu closes |
| Segmented control | Few mutually exclusive filters | Labels remain understandable without icons |
| Saved view | Reusable filter/sort combination | User-visible naming and edit/delete behavior |

## Query Summary

Result pages should show:

- Search term when safe to display
- Active filters
- Sort order
- Result count when available
- Date range or timeframe
- Data source or permission scope where relevant
- Clear-all action when filters are active

Do not expose sensitive health search terms in shareable URLs unless privacy review explicitly approves it.

## Result States

| State | User-facing meaning |
| --- | --- |
| Loading | Query is running and prior context is preserved |
| No data | Nothing has been logged, imported, or permitted |
| No matches | Data exists, but active query constraints hide it |
| Unavailable | Dependency is missing, offline, permission-blocked, or failed |
| Stale | Results exist but may not reflect latest data |
| Partial | Some data sources are included and others are missing |

## Implementation Guidance

- Prefer explicit filter labels over icon-only controls.
- Keep high-frequency filters close to the result set.
- Use progressive disclosure for advanced filters.
- Default sort order should match user expectation for the content type.
- Avoid hidden ranking behavior unless the ranking rule is explainable.
- Test long filter labels, empty results, slow queries, and partial data.

## Acceptance Criteria

- Users can tell what data they are looking at and why.
- Clearing or changing query constraints is obvious and reversible.
- Search and filter states do not leak sensitive health details.
- Result counts, empty states, and stale states are truthful.
- Keyboard and assistive-technology users can operate search, filters, and sort controls.

## References

- specs/02-design/inputs.md
- specs/02-design/buttons.md
- specs/02-design/lists-and-tables.md
- specs/03-product/health-timeline.md
- specs/03-product/insights-and-correlations.md
- specs/04-engineering/observability.md

## Version History

- v1.5.0: Adds search, filter, sort, and query-state standards.
