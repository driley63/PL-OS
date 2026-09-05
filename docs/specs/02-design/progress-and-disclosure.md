# Progress and Disclosure

Status: Released
Owner: Design System Working Group
Version: 1.5.0
Last updated: 2026-08-04

## Purpose

Defines progress, loading, skeleton, stepper, accordion, disclosure, and progressive-detail standards for Plectara product interfaces.

## Scope

- Steppers, progress bars, completion indicators, skeletons, spinners, accordions, show-more controls, expandable sections, and contextual education
- Onboarding, daily logging, reports, exports, sync, AI preparation states, and long-form explanation surfaces
- Mobile, desktop, accessibility, motion, and prototype behavior

## Requirements

- Progress indicators must distinguish known progress from unknown waiting.
- Disclosures must not hide required consent, safety, limitation, or error information.
- Loading states must preserve layout where possible and avoid implying certainty.
- Multi-step workflows must show current step, completion state, and safe backtracking.
- Skeletons must approximate actual layout and not flicker for short waits.
- Users must be able to access disclosed content by keyboard and assistive technology.

## Pattern Selection

| Pattern | Use | Avoid |
| --- | --- | --- |
| Stepper | Known sequence with user progress | Nonlinear exploration or dense dashboards |
| Progress bar | Known measurable completion | Unknown API calls or AI processing time |
| Spinner | Short unknown wait | Long health-data sync without explanation |
| Skeleton | Predictable content layout while loading | Unknown layout or error-prone data |
| Accordion | Optional supporting detail | Required warnings, consent, or primary content |
| Show more | Long repeated content | Hiding decision-critical context |
| Inline education | Contextual help near a task | Large generic help blocks before action |

## Progress Rules

- Use percentages only when progress can be measured reliably.
- Use step counts for known workflows such as onboarding or report export preparation.
- Show `Saving`, `Saved`, `Syncing`, `Synced`, `Failed`, and `Offline` states when they affect user confidence.
- Keep optimistic updates reversible and visible when failure is possible.
- Do not use celebratory progress treatment for sensitive health outcomes.

## Disclosure Rules

Disclosed content may include:

- Definitions
- Data source explanation
- Evidence details
- Report methodology
- Optional personalization detail
- Less common settings
- Advanced filters

Disclosed content must not be the only place for:

- Consent impact
- Destructive-action consequences
- Safety limitations
- Critical errors
- Required form instructions
- Export or sharing risk

## Implementation Guidance

- Pair progress states with plain-language status copy.
- Keep loading and loaded content dimensions stable where feasible.
- Respect reduced-motion settings for expansion and loading animations.
- Default accordions to closed only when content is genuinely optional.
- Test slow network, offline, partial success, and repeated retry paths.
- Preserve user work during progress failure.

## Acceptance Criteria

- Users can distinguish waiting, known progress, saved state, failed state, and completion.
- Required health, privacy, consent, and safety context remains visible.
- Loading states do not shift layout unpredictably.
- Disclosures are keyboard-operable and screen-reader understandable.
- Progress and disclosure patterns reduce confusion rather than adding decorative complexity.

## References

- specs/02-design/motion.md
- specs/02-design/empty-error-loading-states.md
- specs/02-design/accessibility.md
- specs/03-product/onboarding.md
- specs/03-product/daily-logging.md
- specs/03-product/reports.md

## Version History

- v1.5.0: Adds progress, loading, stepper, skeleton, and disclosure standards.
