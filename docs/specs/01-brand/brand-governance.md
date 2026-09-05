# Brand Governance

Status: Released
Owner: Brand Working Group
Version: 1.1.0
Last updated: 2026-08-04

## Purpose

Defines how brand changes are reviewed and released.

## Scope

- Plectara brand identity
- Digital product implementation
- Marketing and platform assets
- Design tokens, production assets, and release records

## Requirements

- Logo, color, typography, token, and messaging changes require review.
- Breaking brand changes require major version consideration.
- Generated assets must include source traceability.
- Brand changes must identify whether they are patch, minor, major, or experimental.
- Exceptions must include owner, scope, expiry, and follow-up decision.
- Production brand asset changes must update release notes and asset inventory.

## Change Classes

| Class | Examples | Required process |
| --- | --- | --- |
| Patch | Clarify usage text, fix broken links, correct typos | PR review |
| Minor | Add token aliases, add export requirements, add usage standards | PR review and release note |
| Major | Rename product, replace logo direction, change reserved AI color | ADR, migration notes, maintainer approval |
| Experimental | Prototype visual style for limited test | RFC or documented experiment scope |

## Review Gates

A brand PR must answer:

- What surfaces are affected?
- Does this change alter a released logo, color, token, type, or messaging rule?
- Does the change affect AI color reservation?
- Are examples, assets, navigation, and release notes updated?
- Are migration notes required for product, design, or marketing consumers?

## Approval Rules

- Logo source changes require Brand Working Group review.
- Token changes require Brand Working Group and Engineering review.
- AI visual-language changes require Brand Working Group and AI review.
- Marketing claim or positioning changes require Product and Governance review.
- Breaking changes require ADR approval before release.

## Exception Handling

Exceptions are allowed only when the approved brand system cannot meet a concrete production need. Each exception must document:

- Request owner
- Affected surface
- Reason the standard cannot be followed
- Expiry or review date
- Replacement or remediation plan

Expired exceptions must be removed, renewed, or converted into a standard.

## Implementation Guidance

- Use PR descriptions to classify brand changes.
- Keep release notes current for any visible brand behavior.
- Create an ADR for changes that alter approved direction.
- Create an RFC for exploratory brand behavior that needs broader discussion.

## Acceptance Criteria

- Reviewers can identify the correct process for a brand change.
- Exceptions are visible and time-bound.
- Production assets remain traceable to source.
- Brand changes can be audited through PRs, release notes, RFCs, and ADRs.

## References

- adr/0001-adopt-lifestyleiq-name.md
- adr/0002-establish-brand-philosophy.md
- adr/0003-reserve-purple-for-ai.md
- adr/0004-adopt-green-teal-gradient.md

## Version History

- v1.1.0: Adds change classes, review gates, approval rules, and exception handling.
- v1.0.0: Initial repository baseline.
