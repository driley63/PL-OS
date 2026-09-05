# Product Experience Alignment Review

Status: Released
Owner: Product Working Group
Version: 1.3.0
Last updated: 2026-08-04

## Purpose

Documents the Volume 03 review against released Brand Identity v1.1.0, released Design Language v1.2.0, and the AI Principles baseline. This review makes v1.3.0 release dependencies explicit and reviewer-verifiable.

## Scope

- Product Experience principles, workflows, insights, reports, onboarding, consent, notifications, health language, and user research
- Released Brand Identity color, typography, voice, token, AI color, and governance rules
- Released Design Language component, accessibility, state, motion, chart, and iconography rules
- AI Principles baseline guidance for evidence, safety, privacy, AI labeling, and failure states

## Review Outcome

Volume 03 is aligned with Brand Identity v1.1.0, Design Language v1.2.0, and the current AI Principles baseline. No released Brand Identity or Design Language values need to change for v1.3.0.

The review adds one clarification: Product Experience owns workflow intent, evidence expectations, consent behavior, and health-sensitive product language, while implementation must still use released brand tokens, design-system patterns, and AI safety boundaries.

## Required Alignment Rules

- Product UI must use released Brand Identity and Design Language standards before creating new visual behavior.
- Product claims must not exceed the evidence, confidence, and limitation language visible to users.
- AI-assisted product behavior must identify AI involvement and must not use AI Purple for non-AI product states.
- Health-sensitive workflows must avoid diagnosis, prescription, blame, shame, or unsupported urgency.
- Consent, privacy, deletion, export, and notification controls must remain understandable at the point of user decision.
- Product research findings must distinguish observed evidence from interpretation and recommendation.

## Brand Alignment

| Brand rule | Product Experience usage | Review decision |
| --- | --- | --- |
| Plectara is calm, positive, scientific, human, and trustworthy | Health language, onboarding, reports, and notifications | Aligned; product copy uses calm, non-blaming, evidence-first language |
| Product surfaces use semantic tokens before primitive values | Product workflows reference released Design Language and Brand Identity standards | Aligned; Volume 03 defines behavior, not new visual tokens |
| AI Purple is reserved for AI-generated and model-assisted behavior | AI insights, AI explanations, confidence, and AI-specific product states | Aligned; Volume 03 requires AI labeling and prohibits unsupported AI decoration |
| Inter and platform fallbacks remain the UI type strategy | Product copy and report standards defer typography to Brand and Design volumes | Aligned; no competing typeface or type scale is introduced |
| Brand system does not define medical claims | Product health language defines claim classes and review gates | Aligned; product claim behavior stays in Volume 03 |

## Design Language Alignment

| Design rule | Product Experience usage | Review decision |
| --- | --- | --- |
| Product UI must use Volume 01 color, typography, and token rules | Volume 03 requires released Brand and Design standards | Aligned |
| Components must define states where applicable | Daily logging, reports, timelines, settings, notifications, and onboarding define required states | Aligned |
| Charts and insights must remain understandable without color alone | Timeline, reports, insights, and correlations require source, timeframe, labels, and alternatives | Aligned |
| Motion must not obscure health information or imply certainty | Product Experience avoids urgency, false certainty, and unsupported escalation | Aligned |
| Accessibility applies to controls, charts, states, and health UX | Volume 03 pattern definition of done includes accessibility and recovery criteria | Aligned |

## AI Principles Alignment

| AI baseline area | Product Experience usage | Review decision |
| --- | --- | --- |
| Confidence and evidence | Insights and correlations require evidence, timeframe, confidence, and limitations | Aligned with current baseline; future AI refinement may add stricter thresholds |
| Safety boundaries | Health language prohibits diagnosis, prescription, unsupported causation, and unsupported urgency | Aligned |
| Privacy | Settings, consent, onboarding, exports, and notifications require user-visible data-use context | Aligned |
| AI visual language | AI involvement must be labeled and AI Purple remains reserved for AI-specific meaning | Aligned |
| Failure states | Product states must explain missing, unavailable, stale, or failed AI/data behavior without blame | Aligned |

## Review Findings

- No Volume 03 document introduces conflicting brand color, typography, or token values.
- Volume 03 correctly depends on Design Language for components, states, layout, charts, and accessibility.
- Volume 03 health language prevents unsupported medical claims, diagnosis, prescription, and causation.
- Volume 03 consent and settings standards make privacy-impacting controls user-visible and reversible where possible.
- Volume 03 AI behavior is framed through evidence, confidence, limitations, user controls, and AI labeling.
- Future production flows, prototypes, analytics specs, and research artifacts remain pending implementation artifacts.

## Acceptance Criteria

- Reviewers can trace product workflow rules back to user goals and released PL-OS dependencies.
- Health-sensitive copy distinguishes facts, interpretations, suggestions, limitations, and claims.
- AI-assisted experiences identify evidence, confidence, limitations, and model involvement where relevant.
- Consent, notification, export, and deletion behavior preserve user agency.
- New product patterns document any exception to Brand, Design, AI, privacy, or accessibility standards.

## References

- specs/01-brand/SPEC.md
- specs/02-design/SPEC.md
- specs/03-product/SPEC.md
- specs/05-ai/SPEC.md

## Version History

- v1.3.0: Adds Product Experience alignment review against Brand Identity, Design Language, and AI Principles.
