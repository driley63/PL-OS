# Unreleased

The current released bundle remains [PL-OS v2.7.0](v2.7.0/README.md).

## Insights presentation

Approved design: 2026-10-27
Status: Owner-approved design and detailed specification; consuming-app implementation pending
Change type: Product and presentation amendment for a future minor release

The [Insights Presentation specification](../specs/03-product/insights-presentation.md) defines compact plan tracking and one highlighted finding on Today; a single horizontally scrolling **Filter Insights** row drawn from the app's fixed goal catalog; concise goal cards with **Explore more about [Goal Name]** footers; and connected routes for comparisons, evidence, AI review, chat, and plans. It documents automatic plan statuses, outlined management buttons, missing data, display fields, consent boundaries, a state matrix, precise light/dark visual roles, and 18 native acceptance criteria.

The accompanying gallery contains 38 app-only references: 19 matched views per theme at 1179 × 2556 pixels, with source provenance and checksums. These are high-fidelity browser-rendered design references. See [RFC-0011](../rfc/0011-goal-led-insights-presentation.md) and [ADR-0017](../adr/0017-adopt-goal-led-insights-presentation.md).

This amendment supersedes the long-form Today/Insights hierarchy and October 25 custom-goal/log-filter studies. Implementers must map existing goal identities, eligibility, evidence versions, record-driven plan states, and consent to the display contract, then complete the native acceptance criteria. Canonical artwork, theme foundations, unrelated Today content, clinical rules and cloud exclusions remain governed by their current contracts. The owner approved publication of this documentation amendment on October 27, 2026. Application implementation, application deployment, and a tagged release remain pending.

## Wearable visual specification

Prepared: 2026-10-23
Status: Owner-approved visual direction; specification prepared for main, unreleased bundle addition
Change type: Additive standard for a future minor PL-OS release

The [Wearable Visual Specification](../specs/02-design/wearable-visuals.md) covers Quick Log, Today's Steps and symptom severity on watchOS and Wear OS. It includes six exact approved mockups, two review boards, scoped design values, a vector interpretation of the symptom icon, 37 passing palette checks, and checksummed assets.

The accepted direction uses quiet ink/slate surfaces, jade actions, ivory type, straight copper header accents, a person outline with an inset health cross for Log Symptoms, and initial capitals for every word of English button text. See [RFC-0010](../rfc/0010-wearable-visuals.md) and [ADR-0016](../adr/0016-adopt-wearable-visuals.md).

The severity-screen correction removes the enclosing green picker outline, retains compact jade selection cues and accessible adjustment, and places the symptom heading below native Back/clock controls. Show `Severity` once and omit the separate visible `1–10` label on Apple Watch. Preserve the picker range, accessible range hint and cancellation without saving.

## Migration

Apply the values only to native watch surfaces. Preserve real sections/goals, pinned/adaptive ordering, existing queues and acknowledgment-driven save status, supported phone handoffs, and the 1–10 severity contract/default 5. Initial geometry and type sizes require small-device and large-text review. Use a vector icon and scalable native controls; the generated concepts are not app screenshots.

Phone/tablet themes, widget styling, global tokens, canonical artwork and PL-213 app spacing remain unchanged. This documentation change does not implement or publish the watch apps. Follow the specification's native acceptance checks before a consuming-app release.
