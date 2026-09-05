# RFC-0005: Documentation Publishing Workflow

Status: Draft
Date opened: 2026-08-03
Owner: PL-OS Maintainers

## Problem

The repository should publish readable documentation without making generated artifacts authoritative.

## Proposal

Use MkDocs for GitHub Pages, keep Markdown as source, and add CI validation for documentation builds.

## Expected Impact

- Reviewers can preview docs.
- The source remains version-controlled.
- Non-technical stakeholders can read a site.

## Open Questions

- Should PDF generation be part of CI?
- Should releases include generated archives?

## Decision Path

This RFC may become an ADR when the scope, tradeoffs, and implementation path are accepted.
