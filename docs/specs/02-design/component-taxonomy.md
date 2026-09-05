# Component Taxonomy

Status: Released
Owner: Design System Working Group
Version: 1.2.0
Last updated: 2026-08-04

## Purpose

Defines how Plectara UI components are named, grouped, governed, and reviewed.

## Scope

- Design-system components
- Product-specific patterns
- Documentation examples and future Flutter/web packages
- Review and governance workflows

## Requirements

- Components must have a clear owner, purpose, anatomy, variants, states, and accessibility requirements.
- Shared components must use approved tokens and avoid feature-specific assumptions.
- Product patterns may compose shared components but must document domain-specific behavior.
- AI components must follow AI Purple reservation and label the AI source clearly.
- Health interpretation components must make evidence, confidence, and user action visible.

## Component Classes

| Class | Examples | Owner |
| --- | --- | --- |
| Foundation | color, typography, spacing, radius, elevation | Brand and Design System |
| Controls | buttons, inputs, toggles, segmented controls, sliders | Design System |
| Containers | cards, panels, sheets, modals, table rows | Design System |
| Data display | charts, metrics, timelines, evidence lists | Design System and Product |
| Feedback | empty, loading, error, success, warning, toast | Design System |
| AI-specific | insight card, confidence indicator, evidence callout | AI and Design System |
| Product patterns | daily log, health timeline, report summary | Product |

## Required Component Record

Each component specification should define:

- Purpose
- Anatomy
- Variants
- States
- Content rules
- Accessibility rules
- Token dependencies
- Do and do-not examples
- Release and migration notes when behavior changes

## Implementation Guidance

- Keep shared component APIs small and predictable.
- Avoid styling props that allow arbitrary one-off brand drift.
- Prefer explicit variants over open-ended visual overrides.
- Use RFCs when a component needs new behavior across multiple product areas.

## Acceptance Criteria

- Contributors can classify new UI work as a foundation, component, data display, feedback, AI, or product pattern.
- Reviewers can identify the required owner and review path.
- Components define all expected states before production use.
- Components can be implemented consistently across design and code.

## References

- core/SPEC.md
- specs/02-design/SPEC.md
- specs/02-design/accessibility.md

## Version History

- v1.2.0: Adds component classes, required records, and governance rules.
- v1.0.0: Initial repository baseline.
