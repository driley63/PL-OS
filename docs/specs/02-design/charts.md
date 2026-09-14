# Charts

Status: Released baseline with v2.4.0 dark mode addendum
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-09-14

## Purpose

Defines chart selection, visual encoding, accessibility, evidence labeling, and review rules for health data visualization.

## Scope

- Trends, timelines, correlations, reports, dashboards, and insight evidence
- Mobile and web data displays
- AI explanation surfaces and exported reports

## Requirements

- Charts must state what data is shown, the timeframe, and the unit of measure.
- Color must not be the only encoding for state or category.
- AI-derived correlations must identify evidence, confidence, and limitations.
- Axis labels, legends, and annotations must remain readable at mobile widths.
- Charts must not imply clinical certainty unless the underlying product policy supports it.

## Chart Selection

| Need | Preferred chart |
| --- | --- |
| Change over time | Line chart, sparkline, or timeline |
| Daily completion | Calendar heat map or stacked log list |
| Category breakdown | Bar chart or sorted list |
| Compare values | Bar chart or grouped metric rows |
| Show correlation | Scatter plot with evidence notes |
| Explain insight | Annotated trend with supporting facts |

## Visual Encoding

- Use Brand Identity colors through semantic chart tokens.
- Follow the [dark mode chart contract](dark-mode.md#charts-and-health-data): default series use `primary` and `textSecondary`, with distinct patterns/markers. Check every used background and any necessary adjacent-series boundaries; logo primitives do not establish a tested chart palette.
- Reserve AI Purple for AI-generated insight overlays, confidence, or AI explanation layers.
- Use stroke style, icons, labels, or patterns in addition to hue.
- Avoid decorative gradients inside dense analytical charts.
- Keep chart chrome quiet so data remains primary.

## Required Context

Every chart should expose:

- Title or nearby label
- Timeframe
- Unit or scale
- Data source or log type when relevant
- Empty, loading, and unavailable states
- Evidence note when attached to an insight

## Implementation Guidance

- Use list or table fallbacks when chart density is too high for mobile.
- Keep tooltips accessible through keyboard or alternative details.
- Avoid hiding important values only inside hover states.
- Validate chart copy with Product and AI specs when it interprets health behavior.

## Acceptance Criteria

- Users can understand the chart without decoding color alone.
- Reviewers can identify data source, timeframe, and confidence context.
- Mobile charts remain legible and have accessible alternatives.
- AI chart overlays are clearly identified as AI-derived.

## References

- core/SPEC.md
- specs/01-brand/color-system.md
- specs/05-ai/confidence-and-evidence.md

## Version History

- v2.4.0: Applies the dark mode component contract and current accessibility target; see RFC-0006.

- v1.2.0: Adds chart selection, visual encoding, required context, and accessibility rules.
- v1.0.0: Initial repository baseline.
