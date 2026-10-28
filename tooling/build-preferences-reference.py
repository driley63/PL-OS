"""Build the standalone Preferences design reference; no app mutation."""
from pathlib import Path
import hashlib
import json
from component_color_tokens import bind_component_colors

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tooling/preferences-reference'
DEST = ROOT / 'docs/assets/app/preferences-organization'
PUBLIC = DEST / 'source'
PUBLIC.mkdir(parents=True, exist_ok=True)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

css = (SOURCE/'styles.css').read_text()
css = bind_component_colors(css, ROOT)
for token, filename in [('__INTER_REGULAR__','inter-regular.woff'),('__INTER_MEDIUM__','inter-medium.woff')]:
    css = css.replace(token, filename+'?v='+digest(PUBLIC/filename)[:12])
js = (SOURCE/'preferences.js').read_text().replace('__YARN__','../plectara/textures/plectara-widget-yarn-gentle-focus-v1.webp')
(PUBLIC/'styles.css').write_text(css)
(PUBLIC/'preferences.js').write_text(js)
scenes = json.loads((SOURCE/'scenes.json').read_text())
(PUBLIC/'scenes.json').write_text(json.dumps(scenes,indent=2)+'\n')
html = (SOURCE/'reference.html').read_text().replace('__SCENES__',json.dumps(scenes,ensure_ascii=False))
for name in ['styles.css','preferences.js','lucide.js']:
    html = html.replace('source/'+name+'"','source/'+name+'?v='+digest(PUBLIC/name)[:12]+'"')
(DEST/'reference.html').write_text(html)
hashes={str(p.relative_to(ROOT)):digest(p) for p in sorted(SOURCE.glob('*')) if p.is_file()}
for dependency in ['assets/tokens/color.tokens.json', 'tooling/component_color_tokens.py']:
    hashes[dependency] = hashlib.sha256((ROOT / dependency).read_bytes()).hexdigest()
(DEST/'source-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(f'Built {len(scenes)} Preferences reference scenes.')
