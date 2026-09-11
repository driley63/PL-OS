# v2.3.0 Android asset and gallery verification

Local verification on September 11, 2026, before repository publication.

- **Approved artwork parity:** All 104 native resources, editable SVG sources, and appearance previews exactly match the owner-approved review files. Only packaging, provenance, and publication guidance are added.
- **Android resources:** AAPT2 2.20-14042983 compiles the production resources and links them against Android API 36. Both standard and round launcher references resolve.
- **Geometry and color:** Six ribbon paths retain the original coordinates and fills. The circular head is represented by equivalent arcs in VectorDrawable. Both vectors share the approved transform. The full figure stays inside a 32 dp radius on the 108 dp canvas, preserving a 1 dp reserve within the safe circle.
- **Preview and package checks:** The validator passes all 63 Android PNGs, 21 SVG previews, ten legacy-density icons, resource references, source and per-file checksums, ZIP contents, and site-copy parity. The complete brand ZIP includes the Android package. Existing iOS and flat logo checks also pass.
- **Small-size review:** The approved full-color and monochrome figures were reviewed at 48, 72, and 160 px. The silhouette remains clear; the finest ribbon gaps compress at small sizes. Theme colors and launcher masks in the previews are illustrative.
- **Documentation build:** Strict MkDocs build passes; all 28,382 local file references resolve.
- **Published gallery layout:** Reviewed at desktop width and 390 px in light and dark documentation themes. Cards stack in one column on narrow screens; download links remain readable, and the additional theme gallery expands correctly.
- **Contrast and whitespace:** The 64 existing palette checks and whitespace validation pass.

The release uses a commit and push through the repository's existing automatic deployment. The shipping Android application, app-store listing, and physical-device launcher behavior are outside this PL-OS asset publication.
