# Status Model

Status: Released
Owner: PL-OS Maintainers
Version: 1.0.0
Last updated: 2026-08-02

## Purpose

Defines Draft, Review, Approved, Released, and Deprecated status semantics.

## Scope

- Lifecycle states
- Transitions
- Allowed changes
- Review expectations

## Requirements

- A status must mean the same thing in every volume.
- Released status requires release notes.

## Implementation Guidance

- Use status labels in document headers.
- Do not mark content Released without a version.

## Acceptance Criteria

- Status is clear from the file.
- Automation can eventually validate status metadata.

## References

- core/SPEC.md

## Version History

- v1.0.0: Initial repository baseline.
