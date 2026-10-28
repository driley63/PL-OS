"""Validate captured pixels, generate the PL-OS gallery, and inventory references."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets/app/insights-presentation'
REF = ASSETS / 'approved-2026-10-27'
SCENES = json.loads((ROOT / 'tooling/insights-journey-reference/scenes.json').read_text())
observations = json.loads((REF / 'capture-observations.json').read_text())
files = []
for scene in SCENES:
    for theme in ('light', 'dark'):
        path = REF / 'screens' / f'{scene["id"]}-{theme}.png'
        with Image.open(path) as img:
            assert img.size == (1179,2556), (path, img.size)
            assert img.mode in ('RGB','RGBA'), (path, img.mode)
            assert img.convert('RGB').getextrema() != ((0,0),(0,0),(0,0)), path
        match = next(o for o in observations if o['scene']==scene['id'] and o['theme']==theme)
        assert match['images'] and match['icons'] > 0 and not match['overflow'], path
        files.append(dict(scene=scene['id'], theme=theme, path=str(path.relative_to(REF)),
            width=1179, height=2556, bytes=path.stat().st_size,
            sha256=hashlib.sha256(path.read_bytes()).hexdigest(), scroll_top=match['scroll']))
manifest = dict(version='2026-10-27', status='Approved design and specification; native implementation pending',
    method='Browser rasterization at 3x CSS zoom; app-only full-page clip, no resampling',
    logical_size=[393,852], pixel_size=[1179,2556], screenshots=len(files),
    approved_mockup_sha256='a924c15f55f87c6b7c23792f496aa953fe0a82938d01f3c0ed600e50ab8a3c07',
    consistency_revision='2026-10-27: preserve approved content hierarchy; align existing app chrome, primary actions, logo, navigation icons, control states and theme roles with PL-OS and the current app source.',
    sources=json.loads((REF/'source-hashes.json').read_text()),
    runtime_asset_sha256={str(p.relative_to(REF)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((REF/'source').glob('*')) if p.is_file()},
    artwork='Canonical Plectara gentle-focus yarn, horizontal reversed logo, Inter fonts, and approved stomach silhouette',
    fixture_provenance='Activity, digestion, energy and sleep/activity examples carried from the reviewed simulator walkthrough; plan, chat and state scenarios are design fixtures. Unknown prior counts remain unavailable.',
    exclusions=['Not a shipping app or Flutter screenshot','No production health data source','No native accessibility certification','No clinical thresholds or new cloud permissions'],
    scenes=SCENES, files=files)
(REF/'references.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')

def image_link(scene,theme,prefix,width=280):
    item=next(f for f in files if f['scene']==scene['id'] and f['theme']==theme)
    url=prefix+item['path']+'?v='+item['sha256'][:12]
    alt=scene['label']+' in '+theme+' appearance'
    return f'[![{alt}]({url}){{ width="{width}" loading="lazy" }}]({url})'

gallery=[]
groups=[('Today and Insights',['today','insights']),
        ('Goal summaries and comparisons',['insights-lower','goal-activity','goal-digestion','goal-energy','goal-sleep']),
        ('Evidence, plans, AI review, and chat',['connection','plan','plan-manage','ai-review','ai-review-more','chat']),
        ('Empty, unavailable, and alternate states',['goal-waiting','plan-paused','plan-assessment','insights-ai-off','insights-early','care'])]
for group_index,(title,ids) in enumerate(groups):
    indent='    ' if group_index else ''
    gallery += [f'??? example "{title} — light and dark references"' if group_index else f'### {title}','']
    for id in ids:
        scene=next(s for s in SCENES if s['id']==id)
        gallery += [indent+'**'+scene['label']+'** — '+scene['description'],'',
            indent+'| Light | Dark |',indent+'| --- | --- |',
            indent+'| '+image_link(scene,'light','../../assets/app/insights-presentation/approved-2026-10-27/')+' | '+image_link(scene,'dark','../../assets/app/insights-presentation/approved-2026-10-27/')+' |','']
    gallery += ['']
spec=ROOT/'docs/specs/03-product/insights-presentation.md'
text=spec.read_text()
block='<!-- APPROVED_GALLERY_START -->\n'+'\n'.join(gallery)+'\n<!-- APPROVED_GALLERY_END -->'
if '<!-- APPROVED_GALLERY -->' in text:
    text=text.replace('<!-- APPROVED_GALLERY -->',block)
else:
    text=re.sub(r'<!-- APPROVED_GALLERY_START -->.*?<!-- APPROVED_GALLERY_END -->',lambda _:block,text,flags=re.S)
if '<!-- CONNECTIONS_GALLERY_START -->' not in text:
    spec.write_text(text)

options='\n'.join(f'<option value="{s["id"]}">{escape(s["label"])}</option>' for s in SCENES)
viewer=(ROOT/'tooling/insights-journey-reference/gallery.html').read_text()
viewer=viewer.replace('__SCENE_OPTIONS__',options).replace('__SCENE_DATA__',json.dumps(SCENES,ensure_ascii=False)).replace('__FILE_DATA__',json.dumps(files))
destination = 'previous-goal-comparison-gallery.html' if '<!-- CONNECTIONS_GALLERY_START -->' in text else 'index.html'
if destination != 'index.html':
    viewer = viewer.replace('<body>', '<body><aside style="padding:16px;background:#faf8f4;color:#192d38">Historical comparison-first references. See the <a href="index.html">current connection-led gallery</a>.</aside>', 1)
(ASSETS/destination).write_text(viewer)
print(f'Validated and packaged {len(files)} full-resolution screenshots; generated gallery and specification image links.')
