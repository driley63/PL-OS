# Release Notes - v1.7.0

Date: 2026-08-20
Status: Released minor

## Summary

This release establishes Capture, Habits, and Insights as the connected LifestyleIQ Product Experience pillars and defines how compact surfaces reduce repeated logging effort. It adds Capture-first widget behavior, Adaptive Capture, habit evolution, and a required feature-review test focused on helping users understand how lifestyle affects how they feel.

## Added

- Capture-first standards for home screen widgets, lock screen widgets, watch complications, shortcuts, and compact launch surfaces.
- Widget surface regions for brand or context, stable anchors, adaptive Capture, recent confirmation, and overflow.
- One-tap, guided, and freeform Capture behavior with correction and recovery paths.
- Adaptive Capture behavior based on frequency, recency, time, context, sequence, and user control.
- Favorite Capture, learned habit, and dormant habit states.
- Capture, Habits, and Insights as connected Product Experience pillars.
- The One Sentence Test: “How does this help users understand how their lifestyle affects how they feel?”
- v1.7.0 release manifest, checklist, notes, index entry, and documentation navigation.

## Changed

- Design Language now requires compact surfaces to prioritize Capture actions over charts, scores, summaries, or broad navigation.
- Product Experience now requires feature proposals to identify their product pillar, friction impact, contribution to user understanding, and alignment with the LifestyleIQ North Star.
- Daily logging now treats repeated Capture as an evolution from new Capture to Favorite Capture, learned habit, and dormant habit.
- Insight standards now explain how captured observations and learned habits support evidence-based interpretation.
- Product Philosophy now requires LifestyleIQ to adapt to the user's routine while keeping user control visible.

## Deprecated

- None.

## Removed

- None.

## Known Limitations

- This release does not specify exact iOS WidgetKit or Android widget-family dimensions and platform APIs.
- Sleep and general Capture are the only named default widget actions; the broader production capture catalog and default values remain to be defined.
- Deep-link routing, data schemas, authentication, local persistence, synchronization, analytics events, and backend contracts remain implementation work.
- Production widgets, wearable components, interactive prototypes, and automated widget tests are not included.
