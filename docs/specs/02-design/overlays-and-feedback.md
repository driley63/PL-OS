# Overlays and Feedback

Status: Released
Owner: Design System Working Group
Version: 1.5.0
Last updated: 2026-08-04

## Purpose

Defines standards for modals, dialogs, sheets, banners, toasts, confirmations, and inline feedback in Plectara product interfaces.

## Scope

- Modal dialogs, confirmation dialogs, bottom sheets, side panels, popovers, banners, toasts, alerts, and inline feedback
- Destructive actions, consent changes, permission requests, export flows, sync states, and prototype feedback
- Mobile, web, keyboard, screen-reader, and reduced-motion behavior

## Requirements

- Feedback must match user impact and not overstate urgency.
- Destructive, privacy-sensitive, consent, export, and account actions require clear confirmation when impact is not obvious.
- Overlays must be dismissible, focus-managed, and recoverable unless blocking behavior is legally or technically required.
- Health-sensitive warnings must use calm, specific, non-blaming copy.
- Toasts must not carry information that users need to complete a task later.
- Color must not be the only indicator for success, warning, error, AI, or destructive feedback.

## Pattern Selection

| Pattern | Use | Avoid |
| --- | --- | --- |
| Inline feedback | Field validation, local status, recoverable guidance | Page-level interruption for minor issues |
| Toast | Brief confirmation after a reversible action | Critical errors, health warnings, consent decisions |
| Banner | Persistent page or section status | Decorative announcements without user value |
| Dialog | Focused decision requiring user response | Long forms or dense content |
| Bottom sheet | Mobile task support or compact selection | Critical legal, privacy, or irreversible choices |
| Side panel | Desktop contextual detail or editing | Replacing page navigation for core workflows |
| Popover | Lightweight help, menu, or metadata | Important warnings or hidden required content |

## Confirmation Rules

Require explicit confirmation for:

- Deleting health data, account data, exports, or reports
- Revoking consent or disconnecting integrations
- Sharing, exporting, or downloading health-sensitive content
- Resetting settings that affect notifications, privacy, or AI assistance
- Actions that cannot be undone or whose recovery path is expensive

Confirmations must explain what changes, what remains, whether recovery is possible, and what happens next.

## Feedback States

| State | Requirements |
| --- | --- |
| Success | Confirm outcome and next available action without empty celebration |
| Warning | Explain attention needed and consequence without alarm |
| Error | Preserve work, state impact, and recovery path |
| Loading | Avoid implying known progress when progress is unknown |
| Permission denied | Explain missing permission and route to settings when relevant |
| Consent revoked | Explain feature impact without pressure |

## Accessibility and Motion

- Move focus into blocking overlays and return focus to the trigger on close.
- Trap focus only while an overlay is modal.
- Keep visible focus states inside rounded containers.
- Respect reduced-motion settings for sheets, dialogs, and toasts.
- Keep animation subtle and under the released motion durations unless platform-native behavior requires otherwise.
- Provide accessible names for icon-only close or overflow controls.

## Implementation Guidance

- Use inline feedback first when the user can continue the task.
- Use banners for persistent state that affects the page.
- Use dialogs sparingly and reserve them for decisions.
- Keep copy short, specific, and action-oriented.
- Do not hide destructive actions behind gesture-only behavior.
- Log feedback pattern exceptions with owner, scope, and remediation.

## Acceptance Criteria

- Users can understand what happened, what changed, and what to do next.
- Critical feedback remains available long enough to act on.
- Blocking overlays manage focus and dismissal correctly.
- Destructive and privacy-sensitive actions include impact context.
- Feedback severity maps to real product impact, not visual preference.

## References

- specs/02-design/buttons.md
- specs/02-design/motion.md
- specs/02-design/accessibility.md
- specs/03-product/health-language.md
- specs/03-product/settings-and-consent.md
- specs/04-engineering/state-management.md

## Version History

- v1.5.0: Adds overlay, feedback, confirmation, and severity standards.
