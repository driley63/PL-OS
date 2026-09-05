# PL-OS Core Specification v1.0.0

Status: Released
Release date: 2026-08-02
Owner: PL-OS Maintainers

## 1. Purpose

PL-OS exists to create a single source of truth for Plectara's product, brand, design, engineering, AI, and governance decisions. It prevents product drift by making important decisions explicit, versioned, and traceable.

Plectara is a personal health intelligence platform. It helps users understand how daily habits affect their health by using structured tracking, pattern discovery, AI-assisted analysis, and practical recommendations.

## 2. Philosophy

The approved design philosophy is:

> Translating daily habits into a plan towards optimal health.

This statement is not a public marketing slogan by default. It is the internal compass for evaluating whether a feature, design, data model, or AI behavior helps the user move from raw daily behavior to useful, explainable action.

## 3. Product Principles

1. Understanding over tracking: recording data is valuable only when it improves understanding.
2. Action over observation: meaningful insights should suggest a practical next step.
3. Clarity over complexity: the product should make health information easier to interpret.
4. Evidence over assumption: recommendations should explain their reasoning and confidence.
5. Consistency over novelty: approved patterns should be reused unless a change is justified.
6. Accessibility by default: the baseline experience must be inclusive.
7. Implementation-first: every standard should map to production code, assets, tokens, tests, or reviewable behavior.

## 4. Governance Model

PL-OS content moves through five statuses:

- Draft
- Review
- Approved
- Released
- Deprecated

Significant changes begin as RFCs. Accepted decisions become ADRs. Specifications implement approved decisions. Releases package stable states of the system.

## 5. Change Model

PL-OS uses semantic versioning:

- Patch: editorial corrections, clarifications, and non-behavioral fixes.
- Minor: additive standards that do not break existing implementation guidance.
- Major: breaking changes to names, tokens, behavior, APIs, governance, or core product meaning.

## 6. Repository Standards

Markdown is the authoritative source. Generated Word, PDF, image, site, or app artifacts must trace back to repository content.

Directory names use lowercase kebab-case. ADRs and RFCs are numbered. Specs are grouped by volume. Release artifacts are immutable after publication except for documented errata.

## 7. Decision Records

ADRs are permanent historical records. They capture context, the decision, alternatives, consequences, and supersession history. They explain why a standard exists.

## 8. RFCs

RFCs create space for review before a decision is locked. They should describe the problem, proposal, impact, risks, alternatives, open questions, and expected migration path.

## 9. Quality Bar

Every PL-OS addition must be:

- Clear enough for a future contributor to apply without extra oral history.
- Traceable to a principle, ADR, RFC, or release.
- Versioned.
- Implementation-ready.
- Accessible by default.
- Reviewed for privacy and user-safety impact where relevant.

## 10. Non-Negotiables

- Plectara is not a diagnostic medical device.
- AI assists understanding and decision-making; it does not replace professional medical advice.
- Users own and control their personal health data.
- Recommendations must be explainable.
- Privacy and accessibility are foundational requirements.
- Visual consistency takes priority over one-off novelty.

## 11. Initial Volume Roadmap

- Volume 01: Brand Identity
- Volume 02: Design Language
- Volume 03: Product Experience
- Volume 04: Engineering Standards
- Volume 05: AI Principles
- Volume 06: Product Architecture
- Volume 07: Marketing and Communications
- Volume 08: Governance Operations

## 12. Release Authority

v1.0.0 establishes the baseline. Future changes must update affected specifications, ADRs, release notes, and migration guidance.
