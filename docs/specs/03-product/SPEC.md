# Volume 03 - Product Experience Specification v1.7.0

Status: Released
Owner: Product Working Group
Version: 1.7.0
Last updated: 2026-08-20

## Purpose

Defines the user experience model for daily capture, habit learning, analysis, recommendations, reports, consent, and health-sensitive product communication.

## Scope

- Plectara product ecosystem
- Daily capture, habit learning, health timelines, insights, reports, onboarding, settings, consent, notifications, and research
- Mobile app, web app, documentation examples, and future product design artifacts
- Product surfaces that interpret health behavior, summarize patterns, or ask for sensitive user input

## System Boundaries

Volume 03 covers:

- User goals, workflow intent, and product behavior
- Health-sensitive language and evidence requirements
- Logging, timeline, report, onboarding, notification, and settings patterns
- Consent-aware product controls and user research governance
- Review criteria for product claims, recommendations, and AI-assisted experiences

Volume 03 does not define brand identity, component styling, AI model policy, data architecture, engineering implementation, or marketing claims. Those decisions live in Brand Identity, Design Language, AI Principles, Product Architecture, Engineering Standards, and Marketing volumes.

## Experience Principles

- Reduce effort before adding instruction.
- Capture first on high-frequency surfaces; understanding belongs in deeper product views.
- Every feature proposal must pass the One Sentence Test: "How does this help users understand how their lifestyle affects how they feel?"
- Show evidence before interpretation.
- Keep health guidance cautious, plain, and user-controlled.
- Design for repeated daily use, not only first-run success.
- Make data use, permissions, and AI involvement visible at the point of relevance.

## Product Pillars

| Pillar | User promise | Product responsibility |
| --- | --- | --- |
| Capture | I can record what happened without breaking my routine | Minimize friction, support correction, and preserve trust |
| Habits | Plectara learns what is normal for me | Surface repeated captures, respect user control, and avoid judgment |
| Insights | I can see what may influence how I feel | Explain evidence, confidence, limitations, and optional next steps |

These pillars are sequential but not separate. Capture creates the raw observations. Habits identify what repeats and make capture easier. Insights use those observations and habits to explain patterns without reducing the user to a generic score.

## Requirements

- Standards must map to implementation or reviewable behavior.
- Changes must remain consistent with PL-OS Core.
- Product UI must use released Brand Identity and Design Language standards.
- Feature proposals must identify which product pillar they strengthen, whether they reduce friction, whether they increase user understanding, and whether they align with the North Star that Plectara should disappear into the user's routine.
- Widgets, shortcuts, and other high-frequency entry points must prioritize frictionless Capture over dashboard-style consumption.
- Product claims must identify evidence, source, timeframe, confidence, and limitations when relevant.
- Health-sensitive experiences must avoid blame, shame, diagnosis, or unsupported certainty.
- Consent, privacy, and data-deletion behavior must be understandable before the user commits.
- AI-assisted product behavior must follow AI Principles and identify AI involvement clearly.
- New product patterns must document mobile and web behavior, empty/error/loading states, and accessibility impact.
- Changes that alter released product behavior must update release notes.

## Core Dependencies

| Area | Depends on |
| --- | --- |
| Brand identity | `docs/specs/01-brand/SPEC.md` |
| Design system | `docs/specs/02-design/SPEC.md` |
| Health-sensitive AI behavior | `docs/specs/05-ai/SPEC.md` |
| Product architecture | `docs/specs/06-architecture/SPEC.md` |
| Security and privacy implementation | `docs/specs/04-engineering/security-and-privacy.md` |
| Product alignment review | `docs/specs/03-product/alignment-review.md` |

## Product Pattern Definition of Done

A Product Experience pattern is complete when it defines:

- User goal and success outcome
- Entry points and exit points
- Required data, permissions, and consent context
- Default, loading, empty, error, warning, success, and unavailable states where applicable
- Evidence, confidence, and limitation language where interpretation is present
- Accessibility, privacy, and safety review criteria
- Mobile and web behavior
- Analytics or research signals needed to evaluate quality

## Implementation Guidance

- Use RFCs for uncertain additions.
- Create ADRs for accepted decisions with durable consequences.
- Update release notes when standards change.
- Prefer product patterns over one-off screen decisions.
- Keep examples close to the workflow they describe.
- Treat unsupported health interpretation as a release blocker.

## Acceptance Criteria

- A contributor can locate the relevant product standard.
- A designer or engineer can apply the guidance consistently.
- Reviewers can identify when a product change needs an exception, RFC, ADR, release note, or safety review.
- Product surfaces can be checked against workflow, evidence, consent, language, notification, and research standards.
- The product experience can evolve without breaking released Brand Identity or Design Language constraints.

## References

- core/SPEC.md
- specs/01-brand/SPEC.md
- specs/02-design/SPEC.md
- specs/05-ai/SPEC.md
- specs/03-product/alignment-review.md

## Version History

- v1.7.0: Adds the One Sentence Test to Product Experience feature review.
- v1.7.0: Adds Capture, Habits, and Insights as Product Experience pillars.
- v1.3.0: Adds implementable Product Experience standards and release checklist.
- v1.0.0: Initial repository baseline.
