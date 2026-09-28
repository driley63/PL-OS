# Health Timeline

Status: Approved for PL-OS v2.6.0
Owner: Product Working Group
Version: 2.6.0
Last updated: 2026-09-28

## Purpose

Defines timeline behavior for showing health logs, events, summaries, interventions, reports, and insight evidence over time.

## Scope

- Daily, weekly, monthly, and custom-range health timelines
- Logs, symptoms, habits, context, reports, annotations, and AI insights
- Mobile and web filtering, grouping, navigation, and accessibility behavior

## Requirements

- Timeline entries must identify type, timestamp or date range, source, and edit state where relevant.
- Product summaries must distinguish user-entered data from imported, inferred, or AI-generated data.
- Filtering must preserve context so users understand what is hidden.
- Missing data must be shown as unavailable or not logged, not as zero unless zero is the actual value.
- Health timelines must avoid implying causation without reviewed evidence.
- Timelines must remain usable without color-only categories.

## Timeline Entry Types

| Entry type | Required context |
| --- | --- |
| Daily log | Date, category, entered values, edit affordance |
| Imported data | Source, sync time, permission state |
| Symptom or event | Date/time, severity or notes when provided |
| Habit or intervention | Start/end or recurrence, user intent |
| Insight | Evidence, confidence, timeframe, AI or rule source |
| Report | Covered period, generated time, sharing/export status |

## Navigation and Filtering

- Default views should prioritize recent and actionable context.
- Date controls must support quick jumps to today, previous period, and custom ranges.
- Filters must show active state and allow easy reset.
- Search or filtering should not hide critical warnings without a visible filter indicator.
- Mobile timelines should use progressive loading or grouping when density is high.

## Evidence Context

Every interpretive timeline moment should show:

- What data is included
- What timeframe is used
- What is missing or excluded
- Whether the entry is user-entered, imported, rule-derived, or AI-generated
- What action the user can take next

## Implementation Guidance

- Use stable grouping by date or period before visual embellishment.
- Preserve scroll position when a user edits or dismisses an entry.
- Provide accessible text alternatives for visual trend markers.
- Treat timezone, daylight-saving, and backfilled-entry behavior as product requirements.
- Use reports for dense interpretation that would overload the timeline.

## Acceptance Criteria

- Users can understand what happened, when, and from what source.
- Missing or filtered data is not mistaken for a health conclusion.
- Interpretive entries expose evidence and limitations.
- Timeline controls work across mobile and web.
- Users can recover from sync, edit, and unavailable states.

## References

- core/SPEC.md
- specs/02-design/layout-grid.md
- specs/02-design/cards.md
- specs/03-product/daily-logging.md

## Current visual reference

Apply the [App Visual Specification](../02-design/app-visuals.md) to the current Timeline: category chips above one readable opaque panel, entry labels and multiline metadata, explicit delete controls, copper row rules, and stable bottom navigation. Owner-approved screenshot entries are review fixtures; they do not expand the supported capture catalog. Existing source, missing-data, grouping, edit, deletion and recovery behavior remains governed by this product standard.

## Version History

- v2.6.0: Integrates the approved screenshot-matched woven app visual contract.
- v1.3.0: Adds timeline entry types, filtering rules, evidence context, and acceptance criteria.
- v1.0.0: Initial repository baseline.
