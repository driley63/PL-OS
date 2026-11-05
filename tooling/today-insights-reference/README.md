# Today Insights overview — approved November 5, 2026

Design-only addition to PL-OS. The owner approved the compact selected-goal card, strong unread treatment in both themes, contrast correction, distinct no-finding states, and individual-finding review behavior. App implementation and publication remain separate work.

`approved-fragment.html` is the exact approved interactive review source. It is an input artifact, not a screenshot of the conversation. The builder removes the review carousel, preview frame and host state APIs to produce an independent app-only capture surface. It retains the approved layout, artwork, fonts, icons, copy and interactions.

1. Run `.venv/bin/python tooling/build-today-insights-reference.py`.
2. Serve `docs/` and open `assets/app/insights-presentation/today-overview-2026-11-05/reference.html?scene=today-new&theme=light` through the approved browser tool. `scale=1` is the interactive logical-size version; the default renders at 3×.
3. Wait for `html[data-capture-ready=true]`; record the phone's 1179 × 2556 bounds, loaded assets, text, overflow and source hashes. Capture the app only at native raster dimensions; retain the original screenshot bytes without resampling.
4. Save paired images in `screens/`, then run `.venv/bin/python tooling/package-today-insights-reference.py`. The packager validates capture provenance, dimensions and theme parity, then updates the local gallery and marked specification block.
5. Build PL-OS strictly and check the local site. Do not push without user authorization.

Scenes use deterministic illustrative evidence. They do not prove analyzer output or coverage support. The November 5 source mapping and remaining production contracts are documented in Insights Findings Capabilities. Full evidence charts, attribution, limitations and record controls retain the broader Insights specification even where these navigation-focused examples omit them.

Fonts and artwork are embedded from existing approved assets. The local Lucide runtime and font/icon licenses are copied from the prior reference package. The custom stomach SVG is the existing approved asset. No foundation palette values are added; component-colors.json maps the scoped unread roles to existing registered colors.
