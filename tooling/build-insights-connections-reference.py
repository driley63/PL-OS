"""Build the scope-corrected Insights reference; never changes app code."""
from pathlib import Path
import hashlib
import json
from component_color_tokens import bind_component_colors
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tooling/insights-connections-reference'
OUT = ROOT / 'docs/assets/app/insights-presentation/connections-first-2026-10-27'
PREVIOUS = ROOT / 'docs/assets/app/insights-presentation/approved-2026-10-27/source'
(OUT / 'source').mkdir(parents=True, exist_ok=True)
(OUT / 'screens').mkdir(exist_ok=True)
for name in ['inter-regular.woff', 'inter-medium.woff', 'inter-semibold.woff', 'inter-bold.woff',
             'material-chrome.woff', 'stomach.svg', 'lucide.js', 'OFL.txt', 'LUCIDE-LICENSE',
             'MATERIAL-ICONS-LICENSE', 'HEALTHICONS-LICENSE']:
    shutil.copy2(PREVIOUS / name, OUT / 'source' / name)
for original, destination in [('textures/plectara-widget-yarn-gentle-focus-v1.webp', 'yarn.webp'),
                              ('logos/plectara-horizontal-reversed.svg', 'logo.svg')]:
    shutil.copy2(ROOT / 'docs/assets/app/plectara' / original, OUT / 'source' / destination)
css = (ROOT / 'tooling/insights-journey-reference/styles.css').read_text()
css = bind_component_colors(css, ROOT)
for key, value in {'__INTER_REGULAR__': 'inter-regular.woff', '__INTER_MEDIUM__': 'inter-medium.woff',
                   '__INTER_SEMIBOLD__': 'inter-semibold.woff', '__INTER_BOLD__': 'inter-bold.woff',
                   '__MATERIAL_CHROME__': 'material-chrome.woff', '__STOMACH__': 'stomach.svg'}.items():
    css = css.replace(key, value)
(OUT / 'source/base.css').write_text(css)
for name in ['screens.js', 'direction.css']:
    shutil.copy2(SOURCE / name, OUT / name)
html = (SOURCE / 'index.html').read_text()
for asset in ['source/base.css', 'source/lucide.js', 'direction.css', 'screens.js']:
    digest = hashlib.sha256((OUT / asset).read_bytes()).hexdigest()[:12]
    html = html.replace('"' + asset + '"', '"' + asset + '?v=' + digest + '"')
(OUT / 'reference.html').write_text(html)
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(SOURCE.glob('*')) if p.is_file()}
hashes['tooling/insights-journey-reference/styles.css'] = hashlib.sha256(
    (ROOT / 'tooling/insights-journey-reference/styles.css').read_bytes()).hexdigest()
for dependency in ['assets/tokens/color.tokens.json', 'tooling/component_color_tokens.py']:
    hashes[dependency] = hashlib.sha256((ROOT / dependency).read_bytes()).hexdigest()
(OUT / 'source-hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
print(OUT)
