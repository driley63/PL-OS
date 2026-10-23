# Wearable color contrast evidence

Calculated 2026-10-23 from `design-values.json` using the existing PL-OS component contrast evaluator. All 37 opaque role checks pass using unrounded ratios. This is palette evidence, not a native-device, assistive-technology or raster-image audit. Copper is decorative; disabled alpha treatments need separate measurement if introduced.

Run from the repository root:

```bash
.venv/bin/python tooling/check-component-contrast.py --fixtures docs/assets/wearables/plectara/contrast-fixtures.json
```

| Use | Foreground | Background | Ratio | Minimum | Result |
| --- | --- | --- | --- | --- | --- |
| Primary text on canvas | `#FAF8F4` | `#101B22` | 16.4723:1 | 4.5:1 | Pass |
| Supporting text on canvas | `#B8CBCB` | `#101B22` | 10.3526:1 | 4.5:1 | Pass |
| Saved text on canvas | `#87CBA7` | `#101B22` | 9.2608:1 | 4.5:1 | Pass |
| Waiting text on canvas | `#EAC477` | `#101B22` | 10.5340:1 | 4.5:1 | Pass |
| Error text on canvas | `#FFAAAA` | `#101B22` | 9.6367:1 | 4.5:1 | Pass |
| Essential icon on canvas | `#FAF8F4` | `#101B22` | 16.4723:1 | 3:1 | Pass |
| Primary text on surface | `#FAF8F4` | `#22313A` | 12.6228:1 | 4.5:1 | Pass |
| Supporting text on surface | `#B8CBCB` | `#22313A` | 7.9332:1 | 4.5:1 | Pass |
| Saved text on surface | `#87CBA7` | `#22313A` | 7.0966:1 | 4.5:1 | Pass |
| Waiting text on surface | `#EAC477` | `#22313A` | 8.0723:1 | 4.5:1 | Pass |
| Error text on surface | `#FFAAAA` | `#22313A` | 7.3846:1 | 4.5:1 | Pass |
| Essential icon on surface | `#FAF8F4` | `#22313A` | 12.6228:1 | 3:1 | Pass |
| Primary text on iconContainer | `#FAF8F4` | `#192D38` | 13.4334:1 | 4.5:1 | Pass |
| Supporting text on iconContainer | `#B8CBCB` | `#192D38` | 8.4427:1 | 4.5:1 | Pass |
| Saved text on iconContainer | `#87CBA7` | `#192D38` | 7.5523:1 | 4.5:1 | Pass |
| Waiting text on iconContainer | `#EAC477` | `#192D38` | 8.5906:1 | 4.5:1 | Pass |
| Error text on iconContainer | `#FFAAAA` | `#192D38` | 7.8589:1 | 4.5:1 | Pass |
| Essential icon on iconContainer | `#FAF8F4` | `#192D38` | 13.4334:1 | 3:1 | Pass |
| Primary text on surfacePressed | `#FAF8F4` | `#264C4B` | 8.9269:1 | 4.5:1 | Pass |
| Supporting text on surfacePressed | `#B8CBCB` | `#264C4B` | 5.6105:1 | 4.5:1 | Pass |
| Saved text on surfacePressed | `#87CBA7` | `#264C4B` | 5.0188:1 | 4.5:1 | Pass |
| Waiting text on surfacePressed | `#EAC477` | `#264C4B` | 5.7088:1 | 4.5:1 | Pass |
| Error text on surfacePressed | `#FFAAAA` | `#264C4B` | 5.2225:1 | 4.5:1 | Pass |
| Essential icon on surfacePressed | `#FAF8F4` | `#264C4B` | 8.9269:1 | 3:1 | Pass |
| Action text on primary | `#192D38` | `#76B7A5` | 6.1657:1 | 4.5:1 | Pass |
| Action icon on primary | `#192D38` | `#76B7A5` | 6.1657:1 | 3:1 | Pass |
| Action text on primaryPressed | `#192D38` | `#8DC7B7` | 7.4540:1 | 4.5:1 | Pass |
| Action icon on primaryPressed | `#192D38` | `#8DC7B7` | 7.4540:1 | 3:1 | Pass |
| Focus outline against canvas | `#76B7A5` | `#101B22` | 7.5605:1 | 3:1 | Pass |
| Required boundary against canvas | `#8DA4A6` | `#101B22` | 6.6506:1 | 3:1 | Pass |
| Focus outline against surface | `#76B7A5` | `#22313A` | 5.7937:1 | 3:1 | Pass |
| Required boundary against surface | `#8DA4A6` | `#22313A` | 5.0964:1 | 3:1 | Pass |
| Focus outline against surfacePressed | `#76B7A5` | `#264C4B` | 4.0973:1 | 3:1 | Pass |
| Required boundary against surfacePressed | `#8DA4A6` | `#264C4B` | 3.6042:1 | 3:1 | Pass |
| Activity icon on badge | `#76B7A5` | `#192D38` | 6.1657:1 | 3:1 | Pass |
| Picker selection indicators on canvas | `#76B7A5` | `#101B22` | 7.5605:1 | 3:1 | Pass |
| Wear plus on supporting accent | `#FAF8F4` | `#287E80` | 4.5137:1 | 3:1 | Pass |
