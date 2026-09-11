# v2.2.0 asset and gallery verification

Verified locally on September 11, 2026, before repository publication.

- **Native rendering:** Apple Icon Composer 1.1 (build 59) successfully read the native document and exported all six iOS appearances at 1024 px, 60 pt at 3×, and 20 pt at 3×. The per-file evidence is the `render-manifest.json` included in the download.
- **Geometry and color:** All seven SVG layers retain the exact source shape attributes and nested transforms. The full-color jade head and original ribbon palette are unchanged. The native document uses a consistent white fill specialization for the system's monochrome/tinted modes.
- **Packaging:** Layer references, source hashes, 18 rendered PNG hashes, dimensions, transparent outer corners, ZIP contents, and published-file copies pass the brand validator. Existing flat source and PNG assets have no changes.
- **Visual review:** All 18 renders were reviewed together. The head and woven silhouette remain recognizable at 60 pt; at 20 pt, the mark reads primarily as a silhouette and fine ribbon gaps compress. This is a preview review, not a claim that every strand is separately legible in notification-sized artwork.
- **Gallery:** The six-card gallery, labels, and individual downloads were reviewed at desktop width. At 390 px, the cards form one column, the page and download links fit, and both light and dark documentation themes remain readable.
- **Build:** The strict MkDocs build passes. The existing 64 contrast checks and the expanded brand validator pass. Whitespace checks pass.

The publishing step is a commit and push to the existing repository deployment workflow. The shipping Plectara application and physical-device behavior are not changed or validated by this documentation release.
