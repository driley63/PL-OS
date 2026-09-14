# Accessibility

Status: Released baseline with v2.4.0 dark mode addendum
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-09-14

## Purpose

Defines accessibility requirements for Design Language patterns and component review.

## Scope

- Product UI, charts, forms, navigation, states, motion, and AI insight surfaces
- Mobile and web accessibility behavior
- Design review and implementation validation

## Requirements

- Product UI must target WCAG 2.2 AA; interpret relevant native-software criteria using WCAG2ICT. Follow [Dark Mode & Accessibility](dark-mode.md) for concrete color, component, and state requirements.
- Color cannot be the only signal for state, priority, category, or AI source.
- Interactive controls must have visible focus states.
- Mobile touch targets must be at least 44 by 44 pt on iOS and 48 by 48 dp on Android (logical layout units). PL-OS web controls target 44 by 44 CSS px. These product/platform targets are distinct from WCAG AA's minimum; see [target guidance](dark-mode.md#focus-links-and-interaction).
- Motion must respect reduced-motion settings.
- Charts and insight surfaces must provide accessible text alternatives.

## Required Checks

| Area | Requirement |
| --- | --- |
| Text contrast | Body and UI text meet AA contrast |
| Focus | Keyboard-visible focus is present and not clipped |
| Hit targets | Mobile controls meet minimum target size |
| Labels | Inputs and icon-only controls have accessible names |
| State | Error, warning, success, AI, and loading states have text or icon cues |
| Motion | Reduced-motion alternative exists |
| Charts | Data meaning is available outside color or hover-only interaction |

## Health UX Requirements

- Error copy must be specific and non-blaming.
- Consent and privacy controls must use plain language.
- Critical warnings must not be hidden behind color-only badges.
- AI-generated health insights must identify evidence, confidence, and limitations where applicable.

## Implementation Guidance

- Include accessibility acceptance criteria in component specs.
- Test designs at mobile width, zoomed text, and reduced motion.
- Test light and dark themes independently, including selected, focused, pressed, error, and loading states. Measure actual composited colors; palette-only results do not cover local overrides.
- Test text at 200% and larger supported platform settings, with VoiceOver/TalkBack and applicable keyboard or switch access.
- Use semantic HTML or platform-native accessibility primitives before custom behavior.
- Treat inaccessible chart-only interpretation as a review blocker.

## Acceptance Criteria

- Users can complete core workflows with keyboard or assistive technology.
- Health data and AI insight meaning is not lost without color, animation, or hover.
- Components document labels, roles, focus, and state behavior.
- Accessibility exceptions are documented with owner and remediation plan.

## References

- core/SPEC.md
- specs/01-brand/accessibility.md
- specs/02-design/charts.md
- specs/05-ai/confidence-and-evidence.md

## Version History

- v2.4.0: Applies the dark mode component contract and current accessibility target; see RFC-0006.

- v1.2.0: Adds accessibility checks, health UX requirements, and component review criteria.
- v1.0.0: Initial repository baseline.
