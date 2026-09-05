# Volume 05 - AI Principles

Volume 05 defines how Plectara uses AI to explain health patterns, support user decisions, communicate uncertainty, protect sensitive data, and remain inside safe product boundaries.

## Status

- Current milestone: v1.6.0 released
- Owner: AI Working Group
- Dependencies: PL-OS Core, Brand Identity v1.1.0, Design Language v1.5.0, Product Experience v1.3.0, and Engineering Standards v1.4.0
- Release type: minor release because this work adds implementation-ready AI behavior standards without changing released brand, design, product, or engineering decisions

## Purpose

AI Principles translate the PL-OS philosophy into rules for model-assisted product behavior. They define how insights are generated, explained, evaluated, constrained, reviewed, labeled, and recovered when AI output is uncertain, unsafe, unavailable, or incomplete.

## Principles

- Evidence before inference: AI output must point back to source data, timeframe, confidence, and limitations.
- Assistance over authority: AI may support understanding and planning, but it must not diagnose, prescribe, or replace professional care.
- User agency by default: users must be able to inspect, dismiss, correct, and control AI-assisted behavior.
- Privacy by design: prompts, context, logs, and evaluations must minimize sensitive health data exposure.
- Recoverable uncertainty: low confidence, missing data, model failure, and safety blocks must be visible and non-blaming.

## Document Map

- `SPEC.md`: volume scope, boundaries, requirements, dependencies, and definition of done
- `alignment-review.md`: cross-volume dependency review against Brand, Design, Product, and Engineering standards
- `ai-product-principles.md`: product-facing rules for AI purpose, agency, transparency, and boundaries
- `insight-types.md`: AI-assisted insight taxonomy, eligibility, and required user context
- `confidence-and-evidence.md`: confidence labels, evidence requirements, limitation language, and uncertainty handling
- `recommendation-policy.md`: allowed, restricted, and prohibited recommendation behavior
- `prompt-and-context.md`: prompt ownership, context minimization, retrieval boundaries, and output contracts
- `evaluation.md`: evaluation dimensions, test sets, quality gates, and release review criteria
- `safety-boundaries.md`: health-safety limits, blocked output, escalation handling, and review triggers
- `failure-states.md`: unavailable, stale, low-confidence, blocked, and degraded AI states
- `human-review.md`: review triggers, reviewer responsibilities, audit records, and override rules
- `privacy.md`: consent, data minimization, retention, logging, deletion, and user controls
- `ai-visual-language.md`: AI labels, visual affordances, confidence display, and AI Purple usage rules

## Acceptance Criteria

- Product teams can define AI-assisted behavior without private policy context.
- Designers can represent AI involvement, confidence, evidence, and failure states consistently.
- Engineers can identify prompt, context, logging, evaluation, privacy, and safety requirements.
- Reviewers can reject unsupported health claims, unsafe recommendations, hidden AI behavior, or missing evidence.
- AI behavior remains traceable to released Product, Design, Engineering, Brand, and PL-OS Core standards.
