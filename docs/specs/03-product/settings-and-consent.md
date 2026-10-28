# Settings and Consent

Status: Released
Owner: Product Working Group
Version: 1.3.0
Last updated: 2026-08-04

## Purpose

Defines settings, consent, permission, privacy, export, deletion, and user-control behavior for Product Experience.

## Scope

- Account settings, notification settings, data permissions, integrations, AI controls, export, and deletion
- Mobile and web settings surfaces
- Product, privacy, legal, engineering, and support review

## Requirements

- Settings must expose controls in language users can understand without legal or technical expertise.
- Consent must be specific to purpose, data type, and product behavior where relevant.
- Users must be able to review and change notification preferences.
- Users must be able to understand how connected data sources affect product experiences.
- Revocation, disconnect, export, and deletion flows must explain consequences before completion.
- AI-related controls must identify what is AI-assisted and what changes when disabled.

## Settings Areas

| Area | Required behavior |
| --- | --- |
| Profile | Show editable user-facing account information |
| Privacy | Explain data use, consent state, and sensitive controls |
| Notifications | Allow channel, timing, and topic control |
| Integrations | Show connected services, sync state, and disconnect behavior |
| AI assistance | Explain AI features, visibility, and control state |
| Export | Preview scope and format before export |
| Deletion | Explain impact, reversibility, and timing |

## Preferences navigation amendment

For the selected mobile organization, use [Preferences Organization](preferences-organization.md) and [ADR-0018](../../adr/0018-adopt-preferences-section-hub.md). Preferences uses nine Section Hub destinations under **Your Health**, **Settings**, and **Connections & Account**. The detailed specification maps every existing destination, preserves conditional tracking choices, and keeps shared reminder schedules and independent AI consents intact. It is an approved, unreleased navigation amendment; the released consent, export, deletion, and permission requirements in this document remain authoritative.

## Consent Records

Consent-sensitive actions should capture:

- What the user accepted or changed
- When the action occurred
- Which product purpose was described
- Which data categories were affected
- How the user can revoke or modify the setting
- Which version of the relevant policy or product explanation was shown

## Revocation and Deletion

- Revocation must not be hidden behind support-only workflows unless required by external constraints.
- Disabling a data source must explain which features may degrade.
- Deletion must distinguish local app state, account data, exported files, and third-party data.
- Users must receive clear confirmation when a privacy-impacting action completes.
- Product copy must avoid dark patterns, guilt, or confusing reversals.

## Implementation Guidance

- Group settings by user intent rather than internal system architecture.
- Use plain-language summaries before detailed policy links.
- Keep destructive privacy actions explicit but not obstructive.
- Log consent changes in an auditable way without exposing unnecessary sensitive detail.
- Review new settings with support teams before release.

## Acceptance Criteria

- Users can find, understand, and change core controls.
- Consent state is visible and specific.
- Revocation, export, and deletion consequences are clear.
- AI and integration controls identify behavior impact.
- Settings flows are accessible and recoverable.

## References

- core/SPEC.md
- specs/03-product/onboarding.md
- specs/04-engineering/security-and-privacy.md
- specs/05-ai/privacy.md

## Version History

- Unreleased: Links the owner-selected Section Hub organization and complete destination mapping; does not replace the released consent policy.
- v1.3.0: Adds settings areas, consent records, revocation, deletion, and acceptance criteria.
- v1.0.0: Initial repository baseline.
