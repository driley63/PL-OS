# Volume 05 - AI Principles Specification v1.6.0

Status: Released
Owner: AI Working Group
Version: 1.6.0
Last updated: 2026-08-04

## Purpose

Defines AI behavior standards for model-assisted insights, explanations, recommendations, prompts, context, evaluation, safety boundaries, human review, privacy, visual labeling, and failure states across Plectara product surfaces.

## Scope

- Plectara product ecosystem
- PL-OS implementation guidance
- Mobile app, web app, documentation examples, evaluation assets, and future AI service implementations
- AI-assisted surfaces that interpret health logs, timelines, correlations, reports, summaries, recommendations, or user goals
- AI-adjacent behavior where rules, retrieval, summaries, or automation may be mistaken for model-generated guidance

## System Boundaries

Volume 05 covers:

- AI product principles, model involvement labels, and user agency requirements
- Insight types, recommendation boundaries, confidence, evidence, and limitation standards
- Prompt and context handling, retrieval boundaries, output contracts, and data minimization
- Evaluation gates, human-review triggers, safety escalation, and failure-state behavior
- AI privacy, logging, retention, correction, deletion, and visual-language rules

Volume 05 does not define brand identity, general UI component styling, product workflow prioritization, production service topology, model vendor selection, clinical care pathways, marketing claims, or regulatory classification. Those decisions live in Brand Identity, Design Language, Product Experience, Engineering Standards, Product Architecture, Marketing, Governance, and separate legal or clinical review artifacts.

## AI Principles

- AI should help users understand patterns, uncertainty, and practical options without claiming clinical authority.
- AI output should be explainable enough for a user, reviewer, or engineer to inspect the source, reasoning boundary, and confidence.
- AI should ask for less data before asking for more data.
- AI should be quiet when evidence is insufficient, unsafe, stale, or outside the product boundary.
- AI behavior should degrade into transparent states, not silent guesses.

## Requirements

- Standards must map to implementation or reviewable behavior.
- Changes must remain consistent with PL-OS Core.
- AI-assisted behavior must identify model involvement where a user could reasonably interpret output as personalized, generated, inferred, or recommended.
- Health-sensitive AI output must expose source data, timeframe, confidence, limitations, and safe next action where relevant.
- AI must not diagnose, prescribe, claim causation without reviewed evidence, create unsupported urgency, or replace professional medical advice.
- Prompts, retrieval context, logs, eval traces, and feedback records must minimize sensitive health data and follow consent constraints.
- Recommendations must be optional, evidence-appropriate, reversible where possible, and framed as user-controlled choices.
- Low-confidence, missing-data, stale-context, blocked, or failed AI behavior must use documented failure states.
- Human review is required for new high-impact AI behavior, safety-boundary changes, evaluation-gate changes, or output that can affect health interpretation.
- AI behavior must document mobile and web UX, accessibility impact, privacy impact, evaluation coverage, and release impact where relevant.
- Changes that alter released AI behavior must update release notes.

## Core Dependencies

| Area | Depends on |
| --- | --- |
| PL-OS governance | `docs/core/SPEC.md` |
| Brand tokens and AI color | `docs/specs/01-brand/SPEC.md` and `docs/specs/01-brand/design-tokens.md` |
| AI visual treatment and UI states | `docs/specs/02-design/SPEC.md` and `docs/specs/02-design/ui-pattern-alignment-review.md` |
| Product workflow intent and health language | `docs/specs/03-product/SPEC.md` and `docs/specs/03-product/health-language.md` |
| Engineering implementation, testing, security, and observability | `docs/specs/04-engineering/SPEC.md` |
| AI alignment review | `docs/specs/05-ai/alignment-review.md` |

## AI Behavior Definition of Done

An AI behavior, prompt, model-assisted workflow, or generated output pattern is complete when it defines:

- User goal, product surface, and whether AI involvement is visible or background-only
- Allowed inputs, excluded inputs, consent requirements, and context-retention rules
- Output type, evidence fields, confidence fields, limitation language, and safe action rules
- Prompt, retrieval, tool, or rule contract required to generate the behavior
- Failure, unavailable, stale, low-confidence, blocked, and correction states
- Evaluation dataset or scenario coverage, pass criteria, and regression risks
- Safety, privacy, accessibility, observability, and human-review requirements
- Release notes and migration impact when existing AI behavior changes

## Implementation Guidance

- Use RFCs for uncertain additions.
- Create ADRs for accepted decisions with durable consequences.
- Update release notes when standards change.
- Prefer documented output contracts over free-form prompt behavior.
- Keep examples close to the AI behavior they govern.
- Treat unsupported diagnosis, prescription, causation, hidden model involvement, or unreviewed sensitive-data use as release blockers.
- Design model behavior so the product can show why an output appeared and why it may be wrong.

## Acceptance Criteria

- A contributor can locate the relevant AI standard.
- Product, design, and engineering teams can apply AI rules consistently across mobile and web.
- Reviewers can identify when a change needs an exception, RFC, ADR, release note, safety review, privacy review, or human-review gate.
- AI-assisted surfaces can be checked against evidence, confidence, recommendation, prompt, context, evaluation, safety, privacy, visual-language, and failure-state standards.
- AI standards can evolve without breaking released Brand, Design, Product, Engineering, or PL-OS Core constraints.

## References

- core/SPEC.md
- specs/01-brand/SPEC.md
- specs/01-brand/design-tokens.md
- specs/02-design/SPEC.md
- specs/03-product/SPEC.md
- specs/04-engineering/SPEC.md
- specs/05-ai/alignment-review.md

## Version History

- v1.6.0: Adds implementable AI Principles standards, release checklist, and cross-volume alignment review.
- v1.0.0: Initial repository baseline.
