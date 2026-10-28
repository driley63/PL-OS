"""Validate captures and publish the Section Hub reference gallery locally."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tooling/preferences-reference'
DEST = ROOT / 'docs/assets/app/preferences-organization'
SCENES = json.loads((SOURCE / 'scenes.json').read_text())
observations = json.loads((DEST / 'capture-observations.json').read_text())
assert len(observations) == len(SCENES) * 2
files = []
for scene in SCENES:
    assert scene['layout'] == 'hub'
    for theme in ('light', 'dark'):
        path = DEST / 'screens' / f'{scene["id"]}-{theme}.png'
        with Image.open(path) as img:
            assert img.size == (1179, 2556), (path, img.size)
            assert img.mode in ('RGB', 'RGBA'), (path, img.mode)
            assert img.convert('RGB').getextrema() != ((0, 0), (0, 0), (0, 0)), path
        obs = next(o for o in observations if o['scene'] == scene['id'] and o['theme'] == theme)
        assert obs['images'] and obs['fonts'] and obs['icons'] > 0, path
        assert obs['missingIcons'] == 0 and not obs['overflow'], path
        assert obs['themeTextParity'], path
        assert all(t['width'] >= 44 and t['height'] >= 44 for t in obs['targets']), path
        files.append(dict(scene=scene['id'], theme=theme, path=str(path.relative_to(DEST)),
                          width=1179, height=2556, bytes=path.stat().st_size,
                          sha256=hashlib.sha256(path.read_bytes()).hexdigest(), scroll_top=obs['scroll']))

manifest = dict(version='2026-10-27', decision=json.loads((SOURCE/'decision.json').read_text()),
    method='Browser rasterization at 3x CSS zoom; app-only full-page clip; no resampling',
    logical_size=[393, 852], pixel_size=[1179, 2556], screenshots=len(files),
    provenance=json.loads((SOURCE/'provenance.json').read_text()),
    sources=json.loads((DEST/'source-hashes.json').read_text()),
    runtime_asset_sha256={str(p.relative_to(DEST)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted((DEST/'source').glob('*')) if p.is_file()},
    exclusions=['Not shipping native screenshots', 'No real user data or consent changes',
                'Existing editor rows are placement references', 'Permission and connection states need further design',
                'No native accessibility certification'], scenes=SCENES, files=files)
(DEST/'references.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')

def image_link(scene, theme):
    item = next(f for f in files if f['scene'] == scene['id'] and f['theme'] == theme)
    url = '../../assets/app/preferences-organization/'+item['path']+'?v='+item['sha256'][:12]
    return f'[![{scene["label"]} in {theme} appearance]({url}){{ width="280" loading="lazy" }}]({url})'

gallery = []
groups = [('Section Hub', ['preferences', 'preferences-lower']),
          ('Your Health', ['health-profile', 'tracking', 'tracking-cycle', 'quick-log']),
          ('Settings', ['ai', 'ai-details', 'reminders', 'appearance', 'progress']),
          ('Connections & Account', ['connections', 'account', 'account-actions'])]
for group_index, (title, ids) in enumerate(groups):
    indent = '    ' if group_index else ''
    gallery += [f'??? example "{title} — light and dark references"' if group_index else f'### {title}', '']
    for scene_id in ids:
        scene = next(s for s in SCENES if s['id'] == scene_id)
        gallery += [indent+'**'+scene['label']+'** — '+scene['description'], '',
                    indent+'| Light | Dark |', indent+'| --- | --- |',
                    indent+'| '+image_link(scene, 'light')+' | '+image_link(scene, 'dark')+' |', '']
spec = ROOT/'docs/specs/03-product/preferences-organization.md'
content = spec.read_text()
block = '<!-- PREFERENCES_GALLERY_START -->\n'+'\n'.join(gallery)+'\n<!-- PREFERENCES_GALLERY_END -->'
if '<!-- PREFERENCES_GALLERY -->' in content:
    content = content.replace('<!-- PREFERENCES_GALLERY -->', block)
else:
    content = re.sub(r'<!-- PREFERENCES_GALLERY_START -->.*?<!-- PREFERENCES_GALLERY_END -->', lambda _:block, content, flags=re.S)
spec.write_text(content)
options = '\n'.join(f'<option value="{s["id"]}">{escape(s["label"])}</option>' for s in SCENES)
viewer = (SOURCE/'gallery.html').read_text()
viewer = viewer.replace('__SCENE_OPTIONS__', options).replace('__SCENE_DATA__', json.dumps(SCENES, ensure_ascii=False)).replace('__FILE_DATA__', json.dumps(files))
(DEST/'index.html').write_text(viewer)
print(f'Validated and packaged {len(files)} Section Hub captures and paired gallery.')
