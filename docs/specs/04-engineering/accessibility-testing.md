# Accessibility Testing

Status: Released baseline with v2.4.0 dark mode addendum
Owner: Engineering Working Group
Version: 1.4.0
Last updated: 2026-09-14

## Purpose

Defines engineering validation for accessibility across product workflows, components, charts, forms, navigation, and health-sensitive states.

## Scope

- Mobile and web accessibility testing
- Product components, design-system components, charts, reports, notifications, onboarding, settings, and daily logging
- Automated checks, manual checks, assistive technology checks, and release gates

## Requirements

- Accessibility regressions in core workflows are release blockers.
- Validate both light and dark themes against [Dark Mode & Accessibility](../02-design/dark-mode.md), using WCAG 2.2 AA as the technical target and WCAG2ICT for native interpretation.
- Interactive controls must have accessible names, roles, focus behavior, and touch targets.
- Health data and AI insight meaning must not depend on color, hover, animation, or chart-only interpretation.
- Text must remain readable with platform scaling, zoom, and contrast requirements.
- Motion-sensitive experiences must honor reduced-motion settings.
- Accessibility exceptions must document owner, scope, expiry, and remediation plan.

## Required Checks

| Area | Engineering validation |
| --- | --- |
| Semantics | Labels, roles, headings, regions, and descriptions are present |
| Focus | Keyboard or platform focus order is logical and visible |
| Touch targets | Mobile controls meet minimum target size |
| Text scaling | Layout remains usable at supported large-text settings |
| Contrast | Text and meaningful non-text cues meet Design Language requirements |
| Motion | Reduced-motion behavior is implemented and tested |
| Charts | Equivalent data meaning is available outside visual encoding |

## Manual Review Scenarios

Run these scenarios with synthetic health data in light and dark modes. Include 200% text and larger supported platform settings, VoiceOver on iOS, TalkBack on Android, applicable keyboard/switch navigation, and reduced motion. Check System appearance changes and persisted Light/Dark choices. Include increased contrast and reduced transparency where the platform exposes them.

- First-run onboarding
- Daily logging completion and correction
- Error recovery after save failure
- Report review and export
- Notification destination
- Consent revocation and deletion
- AI insight inspection

## Implementation Guidance

- Add component-level accessibility tests for reusable components.
- Include accessibility checks in design-system package acceptance criteria.
- Use synthetic health data in accessibility fixtures.
- Validate platform-native controls before replacing them with custom behavior.
- Track accessibility defects with severity and affected workflow.

### Automated component checks

PL-OS CI runs the 64 original palette checks plus 140 component checks and calculation regression tests:

```bash
python tooling/build-plectara-tokens.py
python tooling/check-component-contrast.py
python -m unittest discover -s tooling -p 'test_component_contrast.py'
```

The component checker verifies the committed report. After an intentional palette or contract change, regenerate it with `python tooling/check-component-contrast.py --write` and review the differences.

Consuming apps must add widget tests using their real theme and real components in both brightness modes. Flutter's `textContrastGuideline`, `labeledTapTargetGuideline`, `iOSTapTargetGuideline`, and `androidTapTargetGuideline` can catch some problems; enable semantics and test the platform-relevant target guideline. Also assert resolved color pairs for hints, radios, validation borders, filled buttons, badges, and chart strokes. Inspect focus and state layers independently. See [Flutter's testing guidance](https://docs.flutter.dev/ui/accessibility/accessibility-testing).

Use `tooling/check-component-contrast.py --fixtures FILE.json` for source-resolved color measurements, including ordered translucent background layers. The [dated audit fixtures](../../assets/audits/plectara-dark-mode-2026-09-14.json) intentionally contain failures and return a nonzero exit status. They document the inspected app revision and are not a passing release gate.

### Release evidence record

| Field | Required evidence |
| --- | --- |
| Scope | App/build version, source revision, OS/device, theme, date, and reviewer |
| Component | Screen, control, state, text size, foreground, actual background and alpha layers |
| Measurement | Unrounded ratio, applicable threshold, pass/fail, tool or fixture reference |
| Interaction | Focus order and visibility, large-text layout, labels/roles/state, screen-reader outcome |
| Workflows | Onboarding, appearance, daily logging, validation/recovery, charts, insights, and consent tested in each theme |
| Defects | Severity, affected workflow, proposed fix, assigned owner, and retest evidence |

Do not infer a distributed app's accessibility from a source-only audit. A source pass, a rendered check, and a manual assistive-technology review are separate evidence levels. Record anything not tested explicitly. No automated report is an ADA certification.

## Acceptance Criteria

- Core workflows can be completed with assistive technology.
- Controls are discoverable and operable.
- Health interpretation remains understandable without color or animation.
- Accessibility checks are included in release readiness.
- Exceptions are documented and time-bound.

## References

- core/SPEC.md
- specs/02-design/accessibility.md
- specs/03-product/health-language.md
- specs/04-engineering/testing.md

## Version History

- v2.4.0: Applies the dark mode component contract and current accessibility target; see RFC-0006.

- v1.4.0: Adds accessibility validation requirements, scenarios, and release gates.
- v1.0.0: Initial repository baseline.
