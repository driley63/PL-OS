# Volume 01 - Brand Identity Specification v2.3.0

Status: Approved for v2.3.0
Owner: Brand Working Group
Last updated: 2026-09-11

## Purpose

This specification defines the canonical Plectara brand identity and the rules required to implement it consistently. It converts approved brand decisions into versioned standards for product design, web design, Flutter implementation, marketing, app store assets, and future asset production.

## Brand Foundation

Plectara is a personal health intelligence platform. It helps users understand how daily habits affect their health by uncovering patterns, identifying likely triggers, and recommending practical improvements.

The approved philosophy is:

> Translating daily habits into a plan towards optimal health.

## Personality

Plectara should feel intelligent, calm, positive, scientific, optimistic, human, data-driven, premium, and trustworthy.

It should not feel clinical, hospital-like, cold, sterile, overly technical, extreme, or trend-driven.

## System Boundaries

The brand system covers:

- Product naming and verbal identity
- Logo, icon, and wordmark usage
- Primitive, semantic, and state color tokens
- Typography standards for UI, marketing, and documentation
- Iconography and illustration direction
- Source and generated brand assets
- Governance for brand changes

The brand system does not define product features, medical claims, clinical policy, AI safety rules, or app architecture. Those decisions live in the Product, AI, Governance, and Engineering volumes.

## Logo System

The approved logo is a woven human figure in teal, jade, copper, and slate, paired with the restored outlined Plectara wordmark. The owner approved the final geometry, uniform separation channels, and lettering on 2026-09-04. The 2026-09-07 color standard requires a jade (`#76B7A5`) head in every full-color logo. Use ink lettering on light backgrounds and white lettering on dark backgrounds. Monochrome versions use a single ink or white fill for the whole figure and lettering. The icon must work as an iOS app icon, Android launcher icon, favicon, social avatar, wearable icon, and standalone product symbol.

Production logo files must be treated as source-controlled assets. Teams must not redraw, trace, approximate, or manually recreate the mark from screenshots.

The 2026-09-11 owner-approved Liquid Glass treatment adds a native iOS icon built from the same vector layers. System materials supply lighting and depth; clear and tinted appearances may render the whole figure monochromatically. Use the editable `Plectara.icon` document for iOS integration and the native PNG renders for review and communications. The flat logo masters and outlined wordmark retain their existing rules.

The owner-approved Android treatment (2026-09-11) uses an unmasked vector foreground, opaque ink background, and a dedicated monochrome vector for system theming. Its uniform size increase of about 13% and revised placement preserve all original shapes and six-unit channels. The figure remains within a 32 dp radius on a 108 dp canvas. Android supplies the launcher mask and theme colors. Use the native resources for the app and the illustrative previews for review or communications.

## Color System

The signature brand expression is the flat-color woven-person identity on ivory or ink. Purple is reserved primarily for AI-generated insights and machine-learning behavior.

Teal, jade, copper, ink, slate, and ivory form the canonical brand palette. AI Purple remains a separately reserved primitive. Product surfaces should use semantic tokens instead of primitive values when a semantic role exists.

## Typography System

Inter is the primary UI typeface. SF Pro, Roboto, and system-ui are platform fallbacks. The approved Plectara wordmark is outlined artwork; use its supplied files without retyping or altering the lettering.

Typography should feel calm, readable, and precise. Health explanations, insight summaries, and data labels must favor clarity over expressive display styling.

## Implementation Requirements

- Every color must exist as a token before production use.
- The logo must not be redrawn from memory.
- App icon exports must preserve safe area and contrast.
- AI-specific color use must follow the purple reservation rule.
- Brand assets must include source, generated export, and platform-specific paths.
- Design token changes must include a migration note when they affect existing consumers.
- Production asset updates must include an inventory update and reviewer-visible before/after context.

## Governance Requirements

- Clarifications to existing rules may ship as patch releases.
- Additive brand standards should ship as minor releases.
- Breaking changes to the approved brand direction require major version consideration and an ADR.
- Logo, color, typography, naming, and AI visual language changes require Brand Working Group review.
- Any exception granted for a production surface must be documented with scope, owner, expiry, and follow-up.

## Definition of Done

A Volume 01 change is complete when:

- The affected specification file is updated.
- Examples or implementation snippets are updated when behavior changes.
- Asset README or inventory files are updated when source assets change.
- MkDocs navigation exposes any new canonical documents.
- Release notes and manifest identify the change.
- Reviewers can classify the change as patch, minor, or major.

## Version History

- v2.3.0: Adds adaptive Android vectors, monochrome theming, approved optical placement, 21 preview combinations, and a dedicated download.
- v2.2.0: Adds native Liquid Glass iOS icon sources, six system appearances, three preview sizes, downloadable packages, and platform-specific usage guidance.
- v2.1.0: Standardizes jade heads in all full-color logos, ink/white lettering, complete monochrome variants, and visible SVG/PNG downloads.
- v2.0.0: Adopts the approved Plectara identity, restored outlined lettering, and light/dark semantic palette; preserves the component and UI typography systems.

- v1.1.0: Adds implementation-ready color, token, asset, logo usage, and governance standards.
- v1.0.0: Initial approved baseline.
