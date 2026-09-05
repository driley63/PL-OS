# RFC-0002: Component Library

Status: Draft
Date opened: 2026-08-03
Owner: PL-OS Maintainers

## Problem

The product will require repeated UI surfaces for logging, insights, correlations, trends, and reports.

## Proposal

Define a component library before feature screens are built, including buttons, inputs, cards, navigation, charts, states, and domain-specific health components.

## Expected Impact

- Screens are assembled from approved primitives.
- Visual drift is reduced.
- Testing can focus on reusable contracts.

## Open Questions

- Which components belong in v1?
- Which components should be pure Flutter widgets versus app-level compositions?

## Decision Path

This RFC may become an ADR when the scope, tradeoffs, and implementation path are accepted.
