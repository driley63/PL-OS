# Logo Construction

Status: Owner-approved artwork
Version: 2.0.0
Last updated: 2026-09-04

## Canonical construction

Use the source SVGs in `assets/brand/plectara/source/`. The approved reconstruction retains the original concept PNG for provenance, but that PNG is not the source for subsequent exports.

The construction combines four colored strands into a human figure. Narrow separation channels have a shared six-unit clearance in construction coordinates. Offsets are computed from neighboring boundaries with subpixel approximation; do not independently reposition strand edges. The larger intentional openings around the head and between the legs are not separation channels.

The Plectara lettering is recovered from the approved artwork as outlines. It is not live text or an installable typeface. UI and supporting copy remain Inter.

## Export rules

- Preserve aspect ratio, colors, transparent channels, and head placement.
- Use the checked-in generator for symbol and derivative exports.
- Reuse `plectara-wordmark.svg` without retracing it during normal builds.
- Use a fully opaque, unrounded square for iOS and legacy launcher sources.
- Keep the Android foreground inside its adaptive safe area.
- Single-color variants must contain only one foreground fill.
- SVGs must not contain embedded bitmaps or external font dependencies.

## Review

Inspect color and monochrome versions on light and dark backgrounds. At 32 px and above, evaluate the weave; at 16 px, evaluate recognition of the silhouette, not preservation of every gap. Any future geometry change requires a new review.

The previous leaf-mark placeholder review applies only to archived files in `assets/brand/logos/`. It is not an unresolved approval gate for the approved Plectara master.
