# ADR-0016: Adopt the Plectara wearable visuals

Status: Accepted for specification implementation; unreleased
Date: 2026-10-23
Owner: Design System Working Group / Native App Engineering
Proposal: [RFC-0010](../rfc/0010-wearable-visuals.md)

## Context

The owner approved six wearable mockups after reviewing and refining the header accent, symptom icon and button capitalization. The request is to make those decisions durable in PL-OS. Generated references alone do not define native interaction, data states, accessibility, or device dimensions.

## Decision

Adopt the [Wearable Visual Specification](../specs/02-design/wearable-visuals.md) for watchOS and Wear OS. Use local ink/slate surfaces, ivory text, jade primary actions and a short straight copper heading rule. Left-align the rule on Apple Watch and center it on Wear OS. Retain the platform-specific jade severity picker cues.

Approve the person outline with a small centered health cross as the Log Symptoms product icon. It remains beside the explicit action label, is distinct from the Plectara logo, and carries no diagnostic or clinician-authority meaning. Use the same motif on both platforms.

Use initial capitals for every word of first-party English wearable button labels and supporting text within action cards, including short words. Preserve user-authored names, acronyms, medication names, units and locale-specific casing. Do not change stored health records to satisfy a display style.

Preserve Inter and native scalable text, the 1–10 severity contract/default 5, existing real sections/goals, explicit phone handoffs, durable queued requests and acknowledgment-driven saved states. Use adaptive native layouts rather than scaling raster mockups to fit.

## Implementation clarification — 2026-10-23

Following the owner's review of the native severity screen, prohibit an enclosing green/jade picker outline. Retain compact selected-row cues and native accessibility/Crown operation. Reserve the system navigation area above the custom heading and copper rule, retain Back/cancellation, and render the Severity label only once. The owner requested this correction in both PL-OS and the Apple Watch app; the six approved reference images remain unchanged.

## Consequences

The wearable canvas and action surfaces become documented local overrides rather than changes to global dark tokens. Phone/tablet themes, widget appearance, canonical artwork and PL-213 app spacing are unaffected.

Store the exact approved references, a vector interpretation of the symptom motif, machine-readable design values and contrast fixtures in `docs/assets/wearables/plectara/`. The normative specification takes precedence over incidental raster detail. Native geometry, icon conversion, large text, state feedback and assistive technology require consuming-app review.

This is an additive, unreleased specification change. It does not authorize a deployment, claim native implementation is complete, or publish a new operating-system release.
