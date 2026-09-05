# Onboarding

Status: Released
Owner: Product Working Group
Version: 1.3.0
Last updated: 2026-08-04

## Purpose

Defines first-run onboarding behavior for expectation setting, account setup, permissions, personalization, consent, and activation.

## Scope

- New-user onboarding, returning-user reactivation, permission education, and initial goal setup
- Mobile and web first-run flows
- Product, design, privacy, accessibility, and research review

## Requirements

- Onboarding must explain product value before requesting sensitive data or permissions.
- Required steps must be limited to what is necessary for the first useful experience.
- Optional personalization must be skippable and editable later.
- Permission requests must be contextual, plain-language, and reversible where the platform allows it.
- Onboarding must not overpromise health outcomes, diagnosis, or AI certainty.
- Users must be able to leave onboarding and return without losing progress.

## Onboarding Stages

| Stage | Goal | Requirement |
| --- | --- | --- |
| Welcome | Set expectation | Explain Plectara in plain language without dense policy copy |
| Account setup | Establish identity and access | Collect only required account information |
| Goal context | Understand user intent | Keep goals editable and avoid clinical promises |
| Data setup | Configure logs or integrations | Explain why each data source matters |
| Consent | Confirm data use | Make permission, privacy, and revocation clear |
| First useful action | Create momentum | Help the user complete one meaningful task |

## Permission Sequencing

- Ask for permissions only when the user understands the immediate value.
- Do not stack multiple platform permission prompts without explanation.
- Provide a fallback path when a permission is denied.
- Make denied, unavailable, and later-enabled states visible in settings.
- Treat consent acceptance as a product event that must be auditable.

## Implementation Guidance

- Use progressive disclosure for privacy and data-use detail.
- Keep onboarding copy calm and short.
- Avoid gamified pressure before trust is established.
- Test onboarding with users who are skeptical, privacy-sensitive, or managing complex health routines.
- Measure completion, skipped steps, permission denial, and first-week retention together.

## Acceptance Criteria

- Users understand what Plectara does before sharing sensitive data.
- Permissions and consent are requested with context and alternatives.
- Required setup remains minimal.
- Onboarding can recover from interruption.
- Product value is demonstrated through a first useful action.

## References

- core/SPEC.md
- specs/03-product/settings-and-consent.md
- specs/03-product/health-language.md
- specs/02-design/empty-error-loading-states.md

## Version History

- v1.3.0: Adds onboarding stages, permission sequencing, and acceptance criteria.
- v1.0.0: Initial repository baseline.
