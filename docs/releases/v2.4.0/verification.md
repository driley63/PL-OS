# v2.4.0 verification

Local checks completed on 2026-09-14 before publication.

- **Contrast:** 64 original palette checks and 140 additional component checks pass. The component report matches the current source palette and checker.
- **Regression tests:** Six tests pass, including alpha compositing and a near-threshold case that must fail despite rounding to 4.50.
- **Brand compatibility:** The approved asset validator passes. The palette adapters and released brand archives are unchanged.
- **Documentation:** Strict MkDocs build and whitespace checks pass.
- **Flutter example:** The extracted integration example and generated adapter were analyzed in an isolated directory against the installed Flutter SDK; no issues were reported.
- **Preview review:** Light and dark samples were inspected at a narrow 319 px viewport and a 1200 px desktop breakpoint. Fields, badges, chart patterns, and values render correctly. Desktop layout has no horizontal page overflow. Pointer/keyboard selection works; Tab reaches the primary action with a visible 3 px focus outline and 3 px offset.
- **App audit provenance:** The nine recorded source-file hashes match the inspected app revision. The 16 fixed measurements intentionally include 14 failing pairs and two passing controls; these are evidence for the audit, not the PL-OS passing CI set.

The release follows the existing push-to-main deployment workflow. Deployment status and the public pages must be checked after that workflow completes. This record does not claim device accessibility verification or an app release.
