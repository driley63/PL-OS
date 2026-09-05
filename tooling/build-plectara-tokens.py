"""Generate PL-OS color adapters and verify declared contrast pairs."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'assets/tokens/color.tokens.json').read_text())

def kebab(name):
    return re.sub(r'([A-Z])', r'-\1', name).lower()

def write(path, content):
    p = ROOT/path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

legacy = {'evergreen':'teal', 'fresh-lime':'jade', 'growth-green':'jade',
          'wellness-teal':'teal', 'deep-navy':'ink', 'slate-blue':'slate',
          'wellness-blue':'wellness-blue', 'energy-yellow':'energy-yellow',
          'coral':'coral', 'ai-purple':'ai-purple'}
components = {'button-primary-background':'primary', 'button-primary-label':'onPrimary',
              'button-primary-hover':'primaryHover', 'button-secondary-label':'link',
              'input-background':'surface', 'input-border':'border', 'input-text':'text',
              'card-background':'surface', 'card-border':'divider', 'focus-ring':'focus',
              'link':'link', 'selected-background':'selected', 'chart-primary':'primary',
              'chart-secondary':'textSecondary', 'chart-ai':'ai'}

css = '/* Generated from assets/tokens/color.tokens.json. Do not edit. */\n:root {\n'
for group in ('brand', 'accent'):
    for name, entry in data[group].items():
        css += f'  --plectara-{kebab(name)}: {entry["hex"]};\n'
for old, new in legacy.items():
    css += f'  --liq-color-{old}: var(--plectara-{new});\n'
css += '  --liq-gradient-brand: linear-gradient(var(--plectara-teal), var(--plectara-teal));\n}\n'
for mode, selector in [('light', ':root'), ('dark', '[data-theme="dark"], [data-md-color-scheme="slate"]')]:
    css += selector + ' {\n'
    for name, value in data[mode].items():
        css += f'  --plectara-color-{kebab(name)}: {value};\n'
    for name, role in components.items():
        css += f'  --plectara-{name}: var(--plectara-color-{kebab(role)});\n'
    css += '}\n'
write('assets/web/plectara-tokens.css', css)
write('docs/stylesheets/plectara-tokens.css', css)
write('assets/web/lifestyleiq-tokens.css', '/* Deprecated import path; retained for compatibility. */\n@import "./plectara-tokens.css";\n')

dart = "// Generated from color.tokens.json.\nimport 'package:flutter/material.dart';\n\n"
for cls, values in [('PlectaraColors', {k:v['hex'] for group in ('brand','accent') for k,v in data[group].items()}),
                    ('PlectaraLightColors', data['light']), ('PlectaraDarkColors', data['dark'])]:
    dart += f'class {cls} {{\n  const {cls}._();\n'
    for key, value in values.items():
        dart += f'  static const {key} = Color(0xFF{value[1:]});\n'
    dart += '}\n\n'
write('assets/flutter/plectara_colors.dart', dart.rstrip() + '\n')
old = "// Deprecated import path; use plectara_colors.dart.\nimport 'plectara_colors.dart';\nexport 'plectara_colors.dart';\n\n@Deprecated('Use PlectaraColors and theme-specific semantic colors')\nclass LifestyleIQColors {\n  const LifestyleIQColors._();\n"
for name in ('evergreen','freshLime','deepNavy','slateBlue','wellnessBlue','energyYellow','coral','aiPurple'):
    old += f'  static const {name} = PlectaraColors.{name};\n'
for name in ('background','surface','text','textSecondary','divider'):
    old += f'  static const {name} = PlectaraLightColors.{name};\n'
write('assets/flutter/lifestyleiq_colors.dart', old + '}\n')

def luminance(color):
    rgb = [int(color[i:i+2],16)/255 for i in (1,3,5)]
    linear = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in rgb]
    return sum(x*w for x,w in zip(linear, (.2126,.7152,.0722)))

def ratio(a,b):
    values = sorted((luminance(a),luminance(b)))
    return (values[1]+.05)/(values[0]+.05)

rows = []
for mode in ('light','dark'):
    palette = data[mode]
    pairs = [('onPrimary','primary',4.5), ('onPrimary','primaryHover',4.5)]
    for background in ('background','surface','surfaceMuted'):
        for fg in ('text','textSecondary','link','success','warning','critical','info','ai'):
            pairs.append((fg,background,4.5))
        for fg in ('border','focus'):
            pairs.append((fg,background,3.0))
    for fg,bg,minimum in pairs:
        actual = ratio(palette[fg],palette[bg])
        assert actual >= minimum, (mode,fg,bg,actual,minimum)
        rows.append(f'| {mode} | {fg} / {bg} | {actual:.2f}:1 | {minimum}:1 | Pass |')
report = '# Plectara color contrast checks\n\nGenerated from color.tokens.json. Tests declared text pairs at 4.5:1 and required control/focus boundaries at 3:1. This is a palette check, not a complete product accessibility audit. Decorative dividers, logo strands, and disabled states are not included.\n\n| Theme | Pair | Contrast | Minimum | Result |\n| --- | --- | --- | --- | --- |\n'+'\n'.join(rows)+'\n'
write('assets/brand/plectara/contrast-report.md', report)
write('docs/specs/02-design/plectara-contrast-report.md', report)
print(f'Generated CSS/Flutter adapters; {len(rows)} contrast checks passed.')
