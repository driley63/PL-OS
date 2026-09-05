# Plectara component color migration

Version: 2.0.0
Status: Implemented in shared tokens and documentation theme

Keep the existing component library's typography, spacing, radii, layout, motion, and behavior. Change its color roles as follows. An application consuming these specifications must import the new tokens to receive the update; this repository contains no separate running product app.

| Component role | Light surface | Dark surface |
| --- | --- | --- |
| Primary button | Teal background, white label | Jade background, ink label |
| Primary hover | Deep teal #206668, white label | Jade #8DC7B7, ink label |
| Links / active navigation | Deep teal #206668 | Light jade #8DC7B7 |
| Focus ring | Teal #287E80 with 3 px offset | Jade #76B7A5 with 3 px offset |
| Page / card | Ivory #FAF8F4 / white | Ink #192D38 / #223D49 |
| Main / secondary text | Ink / readable slate #506F7E | Ivory / #B8CBCB |
| Input boundary / disabled outline | #738B8D | #8DA4A6 |
| Selected card / chip | #E9F3EF, ink label, teal outline | #264C4B, ivory label, jade outline |
| Decorative accent | Copper #C88764 or jade | Copper or jade |
| Chart series | Teal, slate, copper, jade | Same identities on dark surface |

Copper and jade are not normal-sized text colors on ivory and do not carry critical state alone. Charts require labels, marker shapes, or line patterns, and must be checked for adjacent-series contrast. Add ink outlines where a light series needs a visible boundary. AI Purple stays exclusive to AI; use accessible #6748D8 for text on light surfaces and #B7A7FF on ink. Error, warning, success, and info remain independent semantic roles, with labels/icons as well as color.

Use `assets/web/plectara-tokens.css` or `assets/flutter/plectara_colors.dart`. CSS includes light/dark semantic roles and component aliases. Existing `--liq-*` and Flutter `LifestyleIQColors` names are compatibility aliases; adopt `--plectara-*` and `PlectaraColors` in new components. The former signature-gradient alias now resolves to solid teal so existing consumers no longer display lime gradients.
