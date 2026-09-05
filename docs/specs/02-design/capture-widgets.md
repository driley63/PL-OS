# Capture Widgets

Status: Released
Owner: Design System Working Group
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Defines design standards for Plectara widgets, shortcuts, wearable surfaces, and other compact entry points where the primary user goal is Capture.

## Scope

- Home screen widgets, lock screen widgets, watch complications, shortcut surfaces, and compact launch surfaces
- One-tap Capture, guided Capture entry, adaptive suggestions, pinned actions, and recent confirmation states
- Mobile, wearable, and platform-constrained surfaces that connect to the Plectara app

## Philosophy

The widget is for Capture. The app is for understanding.

Compact surfaces should help users record what just happened with the least interruption possible. They should not become miniature dashboards, analytics summaries, report previews, or health-score surfaces. If the user wants evidence, trends, correlations, reports, or interpretation, the surface should take them into the app.

## Requirements

- Every visible action must either capture immediately, open a focused Capture flow, or route to a clearly named Capture entry point.
- Widgets must prioritize high-frequency repeated actions over summaries, charts, scores, or broad navigation.
- Adaptive suggestions must use the released Plectara design system, not a separate visual language.
- User-pinned actions must remain stable and visually distinguishable from adaptive suggestions without relying on color alone.
- AI Purple must not be used for adaptive Capture unless the surface explicitly communicates AI-generated behavior.
- Success, undo, edit, loading, unavailable, and permission-limited states must be defined where platform capabilities allow.
- Widget content must avoid exposing sensitive health detail in places where the device surface may be public.

## Surface Model

| Region | Purpose | Guidance |
| --- | --- | --- |
| Brand or context label | Identifies Plectara or the active context | Keep compact and subordinate to actions |
| Stable anchors | Persistent actions such as Sleep or general Capture | Use for universal or user-pinned behaviors |
| Adaptive Capture area | Contextual suggestions based on repeated behavior | Keep tappable, concise, and easy to scan |
| Recent confirmation | Shows that the last capture succeeded when space allows | Keep brief and make correction reachable |
| Overflow or more entry | Opens broader Capture options | Use when the surface cannot show everything |

Not every widget size needs every region. Smaller widgets may include only stable anchors and one or two adaptive captures.

## Capture Behaviors

| Behavior | Use | Design rule |
| --- | --- | --- |
| One-tap Capture | The action contains enough default meaning to save | Show immediate feedback and keep undo or edit nearby when possible |
| Guided Capture | The action requires quantity, severity, duration, or notes | Deep-link to the focused in-app Capture screen with context preselected |
| Freeform Capture | The user needs to record something unusual | Route to the general Capture flow without forcing setup |

Do not design multi-question widget flows unless the target platform explicitly supports the required controls and the interaction still reduces total friction. When in doubt, use a focused in-app Capture flow.

## Adaptive Capture Behavior

Adaptive Capture should make the widget feel like it is learning the user's routine. It may reorder or swap suggestions based on repeated behavior, time of day, context, and recently captured sequences.

Adaptive areas should:

- Prefer actions the user repeats often.
- Promote actions that are likely in the current context.
- Avoid crowding; leave enough space for confident taps.
- Update after successful capture when the next likely action is useful.
- Respect pinned, hidden, dismissed, and edited user preferences.
- Fall back to general Capture when confidence or permission is insufficient.

Do not show prediction confidence as a percentage by default. Confidence display adds precision that may not help the user complete the task.

## Favorites and Habits

Design should distinguish three user-facing states:

| State | Meaning | Design treatment |
| --- | --- | --- |
| Recent capture | Recently used but not established | Can appear temporarily when relevant |
| Favorite Capture | User-saved or accepted as a shortcut | Stable enough to find and edit |
| Habit | Learned repeated behavior | Eligible for adaptive placement and contextual promotion |

The user should never need to understand an internal model to use these states. Product language may use Favorite Capture when the user controls the shortcut and Habit when Plectara is explaining that it has learned a recurring behavior.

## Layout Guidance

- Keep widget layouts action-first, with large enough targets for quick use.
- Prefer compact rows, grids, or ribbons of Capture actions over dashboard cards.
- Use released color, spacing, type, radius, elevation, and iconography tokens.
- Keep labels user-recognizable, short, and privacy-aware.
- Avoid charts, health scores, dense metrics, or evidence summaries on capture widgets.
- Use full app views for trend review, correlation explanation, reports, and AI-assisted interpretation.

## Accessibility and Privacy

- Provide accessible labels that describe the action and expected result.
- Do not rely on color, icon shape, or position alone to distinguish pinned and adaptive actions.
- Respect reduced motion and platform widget animation limits.
- Avoid sensitive details in widget labels unless the user explicitly configured them.
- Provide a recoverable path for accidental captures.

## Acceptance Criteria

- A widget design can be reviewed as a Capture surface, not a dashboard.
- One-tap, guided, and freeform Capture behaviors are clearly distinguished.
- Adaptive suggestions preserve user control and do not imply health interpretation.
- Widget visuals remain aligned with released Brand Identity and Design Language standards.
- Sensitive health context is minimized on public or glanceable surfaces.

## References

- specs/01-brand/color-system.md
- specs/02-design/buttons.md
- specs/02-design/iconography.md
- specs/02-design/inputs.md
- specs/02-design/overlays-and-feedback.md
- specs/03-product/daily-logging.md
- specs/03-product/experience-principles.md

## Version History

- v1.7.0: Adds Capture-first widget and adaptive surface design standards.
