# AI Principles Alignment Review

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-08-04

## Purpose

Documents the Volume 05 review against released Brand Identity v1.1.0, released Design Language v1.5.0, released Product Experience v1.3.0, and released Engineering Standards v1.4.0. This review makes v1.6.0 AI dependencies explicit and reviewer-verifiable.

## Scope

- AI Principles specification, insight types, recommendations, prompts, context, evaluation, safety, privacy, human review, failure states, and visual language
- Released Brand Identity token, AI Purple, typography, accessibility, and governance requirements
- Released Design Language component, state, navigation, overlay, feedback, progress, disclosure, accessibility, and UI pattern requirements
- Released Product Experience workflow, health-language, insight, report, consent, notification, onboarding, and user-research requirements
- Released Engineering Standards architecture, testing, security, privacy, observability, performance, accessibility, and release-engineering requirements

## Review Outcome

Volume 05 is aligned with Brand Identity v1.1.0, Design Language v1.5.0, Product Experience v1.3.0, and Engineering Standards v1.4.0. No released Brand, Design, Product, Engineering, or PL-OS Core values need to change for v1.6.0.

The review adds one clarification: AI Principles own model-assisted behavior, safety boundaries, evidence, confidence, prompt/context rules, evaluation gates, and AI-specific user meaning, while Product Experience remains authoritative for workflow intent and Engineering remains authoritative for implementation mechanics.

## Required Alignment Rules

- AI visual treatment must use released Brand and Design tokens before introducing new AI-specific visuals.
- AI Purple remains reserved for generated, model-assisted, or AI-specific behavior and must not become generic decoration.
- Product AI behavior must preserve Product Experience intent, health-sensitive language, consent behavior, and user agency.
- Engineering implementation must preserve prompt/context boundaries, privacy requirements, evaluation gates, logging constraints, and recoverable failure states.
- AI-assisted output must not exceed its evidence, confidence, limitations, safety boundary, or user consent.
- Exceptions must document owner, scope, user impact, safety/privacy impact, expiry, and remediation path.

## Brand Alignment

| Brand rule | AI Principles usage | Review decision |
| --- | --- | --- |
| Plectara is calm, positive, scientific, human, and trustworthy | AI copy, failure states, recommendations, and explanations use evidence-first, non-alarming language | Aligned |
| AI Purple is reserved for AI-generated and model-assisted behavior | AI visual language restricts AI Purple to model involvement, confidence, and AI-specific affordances | Aligned |
| Product surfaces use semantic tokens before primitive values | AI visual standards defer to released Brand and Design tokens | Aligned; no new primitive colors or typography values are introduced |
| Brand system does not define medical claims | AI safety boundaries and recommendation policy define claim limits and review triggers | Aligned |
| Accessibility applies to color, language, and meaning | AI confidence, evidence, and visual treatment require non-color cues and clear labels | Aligned |

## Design Language Alignment

| Design rule | AI Principles usage | Review decision |
| --- | --- | --- |
| Product UI must use released color, typography, component, and state rules | AI visual language and failure states depend on released UI patterns | Aligned |
| Components must identify states where applicable | AI unavailable, stale, blocked, low-confidence, loading, and correction states are documented | Aligned |
| Charts and insight surfaces must remain understandable without color alone | Confidence and evidence standards require labels, source context, and accessible alternatives | Aligned |
| Overlays, feedback, and disclosures must protect focus and user control | AI explanations, evidence drawers, confirmations, and corrections follow released interaction rules | Aligned |
| Navigation and page templates must keep current state visible | AI-generated summaries and insights must preserve source, timeframe, route, and context | Aligned |

## Product Experience Alignment

| Product rule | AI Principles usage | Review decision |
| --- | --- | --- |
| Product Experience owns workflow intent and health-sensitive meaning | AI system boundaries defer workflow prioritization, health language, reports, settings, notifications, and onboarding to Volume 03 | Aligned |
| Insights must show source, timeframe, confidence, and limitations | AI insight types and confidence standards require the same visible context | Aligned |
| Health language must avoid diagnosis, prescription, blame, shame, and unsupported urgency | Safety boundaries and recommendation policy enforce those limits for AI output | Aligned |
| Consent, deletion, export, notification, and privacy controls must remain understandable | Privacy and prompt/context standards require consent-aware context, logging, and controls | Aligned |
| Users must be able to inspect, dismiss, save, or correct AI-assisted insights where meaningful | AI product principles, failure states, and human-review standards preserve user agency | Aligned |

## Engineering Standards Alignment

| Engineering rule | AI Principles usage | Review decision |
| --- | --- | --- |
| Product implementation must respect Brand, Design, and Product standards | AI requirements explicitly depend on released standards and keep implementation mechanics in Volume 04 | Aligned |
| Sensitive health data must be protected by default | Privacy and prompt/context standards require minimization, consent, retention controls, and privacy-safe logs | Aligned |
| CI/CD must run required validation before release | Evaluation standards define AI quality gates and regression checks for relevant changes | Aligned |
| Production-impacting failures must have observability and ownership | Failure states and evaluation standards require owner-visible quality, safety, and fallback records | Aligned |
| Exceptions require owner, scope, user impact, expiry, and remediation | AI alignment rules mirror Engineering exception requirements | Aligned |

## Review Findings

- No Volume 05 document introduces conflicting brand colors, typography, tokens, logos, or product component rules.
- Volume 05 correctly depends on Design Language for AI labels, confidence display, feedback states, overlays, disclosures, accessibility, and responsive behavior.
- Volume 05 correctly depends on Product Experience for workflow intent, evidence expectations, health language, consent, notifications, reports, and user agency.
- Volume 05 correctly depends on Engineering Standards for implementation controls, tests, evaluation gates, observability, security, privacy, and release mechanics.
- AI standards clarify that model-assisted behavior must be visible, explainable, bounded, privacy-aware, and recoverable.
- Future model selection, prompt libraries, evaluation datasets, AI service architecture, and production monitoring remain implementation artifacts outside this documentation release.

## Acceptance Criteria

- Reviewers can trace AI rules back to released Brand, Design, Product, Engineering, and PL-OS Core dependencies.
- AI-assisted experiences identify evidence, confidence, limitations, and model involvement where relevant.
- AI output does not override product workflow intent, health-language limits, consent behavior, or user agency.
- Sensitive prompt, context, evaluation, log, and feedback behavior has clear privacy and safety review triggers.
- Release metadata shows that cross-volume dependency review is complete for v1.6.0.

## References

- specs/01-brand/SPEC.md
- specs/01-brand/design-tokens.md
- specs/01-brand/color-system.md
- specs/02-design/SPEC.md
- specs/02-design/ui-pattern-alignment-review.md
- specs/02-design/empty-error-loading-states.md
- specs/03-product/SPEC.md
- specs/03-product/insights-and-correlations.md
- specs/03-product/health-language.md
- specs/03-product/settings-and-consent.md
- specs/04-engineering/SPEC.md
- specs/04-engineering/security-and-privacy.md
- specs/04-engineering/testing.md
- specs/05-ai/SPEC.md

## Version History

- v1.6.0: Adds AI Principles alignment review against Brand Identity v1.1.0, Design Language v1.5.0, Product Experience v1.3.0, and Engineering Standards v1.4.0.
