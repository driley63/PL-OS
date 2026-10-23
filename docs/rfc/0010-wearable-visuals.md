# RFC-0010: Wearable visual specification

Status: Accepted visual direction; specification prepared, unreleased
Owner: Design System Working Group / Native App Engineering
Date: 2026-10-23

## Problem and accepted proposal

The owner requested a more distinctive Plectara wearable appearance for Apple Watch and Wear OS. The reviewed direction uses deep ink canvas, quieter slate surfaces, jade actions, ivory text and a prominent severity picker. Six mockups cover Quick Log, Today's Steps and symptom severity on both platforms.

During review, the owner requested a straight copper header line on every design, a better Log Symptoms icon, and capitalized button text. The final set uses a person outline with an inset health cross and initial capitals on every word of action labels/supporting card text. The owner approved that set and asked for PL-OS specifications.

## Alternatives and boundaries

The initial curving two-color header accent and wave symptom icon are superseded. The existing broad teal fields give way to scoped darker neutral surfaces. The phone/tablet and home-screen-widget visual contracts remain unchanged. These watch designs do not introduce full-screen yarn, health scores or clinical severity interpretation.

The [Wearable Visual Specification](../specs/02-design/wearable-visuals.md) records the approved visuals, local values, wording, icon, accessible states and native migration. Numeric geometry is a starting target for device validation, not a claim that the generated concepts are measured native layouts. Existing capture/queue/goal functionality must remain present.

## Acceptance and delivery

[ADR-0016](../adr/0016-adopt-wearable-visuals.md) records this decision. Preserve the six final approved assets in the repository with checksums, link them from site navigation, and validate scoped color pairs and the strict documentation build. The changelog records an unreleased additive standard; a new published release and consuming-app implementation are separate steps.
