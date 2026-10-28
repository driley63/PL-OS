# Connection-led Insights reference

Current editable design source for the October 27 capability-scoped amendment. This is a browser design reference, not a Flutter implementation or analysis engine.

- `python3 tooling/build-insights-connections-reference.py` builds the self-contained public reference at `docs/assets/app/insights-presentation/connections-first-2026-10-27/`.
- Serve `docs/` locally and open `reference.html?scene=insights&theme=light`. Scene definitions are in `scenes.json`; both themes must use identical fixtures. Default 3× output is 1179 × 2556. `scale=1` is an interactive logical-size preview; `pair=1` produces a review board outside the app frame.
- Use the approved browser capture tool, wait for `html[data-capture-ready=true]`, and capture the full app region at (0,0,1179,2556). Save the returned JPEG bytes as `screens/{scene}-{theme}.jpg` without resampling. Record DOM observations and capture-time source hashes in `capture-observations.json`.
- `python3 tooling/package-insights-connections-reference.py` checks dimensions, theme parity, loaded assets, no horizontal body overflow, observed source hashes, and fixture scope; generates the checksummed manifest, default gallery and specification image links.

Assets are copied from canonical Plectara sources. Shared shell CSS remains sourced from `tooling/insights-journey-reference/styles.css`; local overrides define the connection hierarchy. Older reference packages are retained as historical assets. The old packager is guarded against replacing the current default gallery/spec.

The approved capability scope is `docs/specs/03-product/insights-findings-capabilities.md`. Current fixtures use Possible Connection, bidirectional meal timing, /10 energy ratings, unknown missing observations, and current domain plans. G2/G3-lite are required future implementation work; this reference must not fabricate evaluated maturity or recurrence. Records, AI, shell destinations and plan-state interactions are limited previews; they do not persist state or implement production services.
