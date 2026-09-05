# Daily Capture and Logging

Status: Released
Owner: Product Working Group
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Defines daily capture and logging behavior for recurring health, habit, symptom, lifestyle, and context entries.

## Scope

- Daily mobile and web capture flows
- One-tap capture, guided capture, freeform capture, edits, skipped days, review, and history
- User-defined quick captures, learned habits, and adaptive capture suggestions
- Health-sensitive copy, privacy, accessibility, and analytics review

## Requirements

- Capture must be fast enough for repeated daily use.
- If a recurring action contains enough information to create a meaningful observation, one tap should save it.
- If additional information is genuinely required, one tap should open the exact guided capture screen needed to finish.
- Users must be able to edit entries and understand when data was last updated.
- Required fields must be minimal and justified by product value.
- Free-text fields must be optional unless the workflow specifically depends on user narrative.
- The product must support partial completion, skipped days, and late entries without shame language.
- Logging must not imply clinical evaluation unless a reviewed product policy supports it.
- Sensitive fields must explain why the data is collected and how it affects product behavior.

## Entry Patterns

| Pattern | Use | Requirement |
| --- | --- | --- |
| One-tap capture | Frequent observation with sufficient default meaning | Save immediately, confirm briefly, and make undo or edit reachable |
| Guided capture | Frequent observation that needs one essential detail | Open a focused capture screen with the selected item already applied |
| Freeform capture | Unusual or undefined observation | Let the user record flexible context without setup |
| Structured log | Multiple related health or habit fields | Group fields by meaning and preserve progress |
| Reflection | Optional qualitative context | Make it skippable and private by default |
| Correction | Editing past entries | Show changed timestamp and affected summaries |
| Backfill | Logging a missed day | Allow context without penalizing the user |

## Adaptive Capture

Adaptive Capture is the product behavior that makes repeated capture faster over time. It should learn from user behavior, not require users to manually design every surface before the product becomes useful.

Adaptive Capture may consider:

- Frequency: what the user captures often.
- Recency: what the user has captured recently.
- Time: what tends to happen at this time of day or day of week.
- Context: what is relevant to location, schedule, device surface, or current workflow when permission allows.
- Sequence: what usually happens before or after another captured observation.
- User control: what the user has pinned, hidden, edited, dismissed, or marked as important.

Adaptive suggestions should feel helpful, not deterministic. The product should not show prediction percentages unless research shows that users understand them and they do not add pressure or false precision.

## Favorites and Habits

Plectara should treat repeated capture as an evolution path:

| Stage | Meaning | Product behavior |
| --- | --- | --- |
| New capture | The user records something normally | Do not ask for setup too early |
| Favorite capture | The user saves or accepts a shortcut for repeated use | Make it easy to access and edit |
| Learned habit | Plectara recognizes a recurring pattern | Surface it contextually while preserving user control |
| Dormant habit | The pattern stops being useful | Reduce prominence without judgment |

Favorites are user-declared. Habits are learned patterns. A learned habit may appear in Adaptive Capture, but the user must be able to pin, hide, rename, edit defaults, or remove it from high-frequency surfaces.

## Widget and Shortcut Capture

Widgets, watch surfaces, shortcuts, and similar entry points should follow one rule:

> The widget is for Capture. The app is for understanding.

These surfaces should not become miniature dashboards. They should prioritize recording observations from real life with the least interruption possible. Summaries, correlations, evidence review, reports, and deeper interpretation belong inside the app.

Widget capture behavior should follow the same patterns as the product:

- One-tap captures save immediately when the observation is already meaningful.
- Guided captures open the focused in-app flow when severity, quantity, duration, or notes are required.
- Freeform capture remains available for anything not predicted or favorited.
- Sleep and general Capture may remain stable anchors while the surrounding suggestions adapt.

## Required States

| State | Product behavior |
| --- | --- |
| Empty | Explain what can be logged and why it matters |
| Partial | Preserve progress and show what remains optional or required |
| Saved | Confirm briefly and return to the user’s next useful context |
| Edited | Make updated data visible without over-alerting |
| Skipped | Respect the user’s choice and avoid guilt language |
| Error | Preserve entered values and explain recovery |

## Streaks and Progress

- Streaks must not punish illness, travel, disability, caregiving, or intentional rest.
- Progress language should emphasize consistency, awareness, or learning rather than perfection.
- Missed entries may be shown as missing data, not failure.
- Weekly and monthly summaries should distinguish logged data from inferred gaps.

## Implementation Guidance

- Prefer structured controls for repeated values and optional notes for context.
- Use platform-native inputs for dates, times, and numeric entry where possible.
- Keep common actions reachable on mobile with one hand where practical.
- Keep high-frequency widget and shortcut labels short, user-authored where possible, and consistent with the app's Capture language.
- Use analytics to detect abandonment, repeated edits, and confusing field labels.
- Review new logging categories for privacy sensitivity before release.

## Acceptance Criteria

- A user can complete core logging without private instruction.
- Entries can be corrected without losing trust in summaries.
- Missed or partial logs do not create shame, alarm, or unsupported interpretation.
- Logging states are accessible and recoverable.
- Product and data reviewers can identify what each field is used for.
- Widget, shortcut, and repeated capture flows reduce effort without hiding correction paths.
- Adaptive Capture behavior can be explained without exposing private or sensitive context unnecessarily.

## References

- core/SPEC.md
- specs/02-design/inputs.md
- specs/02-design/capture-widgets.md
- specs/03-product/health-language.md
- specs/03-product/settings-and-consent.md

## Version History

- v1.7.0: Adds one-tap, guided, freeform, Adaptive Capture, and Habit evolution standards.
- v1.3.0: Adds daily logging entry patterns, states, streak rules, and review criteria.
- v1.0.0: Initial repository baseline.
