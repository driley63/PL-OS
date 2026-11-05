"""Validate the approved Today captures and assemble the current local PL-OS gallery."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets/app/insights-presentation'
REF = ASSETS / 'today-overview-2026-11-05'
OLD = ASSETS / 'connections-first-2026-10-27'
SCENES = json.loads((ROOT / 'tooling/today-insights-reference/scenes.json').read_text())
CAPTURE = json.loads((REF / 'capture-observations.json').read_text())
SOURCES = json.loads((REF / 'source-hashes.json').read_text())
CONTRAST = json.loads((REF / 'contrast-checks.json').read_text())
ROLES = json.loads((REF / 'component-colors.json').read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert CAPTURE['sourceHashes'] == SOURCES, 'Recapture after changing reference inputs'
for path, expected in SOURCES.items():
    assert digest(ROOT / path) == expected, path
assert len(CONTRAST['checks']) == 10
assert all(c['passed'] and c['ratio'] >= c['minimum'] for c in CONTRAST['checks'])
assert len(CAPTURE['observations']) == 2 * len(SCENES)
files = []
for scene in SCENES:
    observations = []
    for theme in ('light', 'dark'):
        path = REF / 'screens' / f'{scene["id"]}-{theme}.jpg'
        with Image.open(path) as im:
            assert im.format == 'JPEG' and im.mode == 'RGB' and im.size == (1179, 2556), path
        matches = [o for o in CAPTURE['observations'] if o['scene'] == scene['id'] and o['theme'] == theme]
        assert len(matches) == 1, path
        o = matches[0]
        assert o['ready'] and o['fonts'] == 'loaded' and o['images'] and o['icons'] > 0, path
        assert not o['overflow'] and not o['unrendered'], path
        assert o['phone']['width'] == 1179 and o['phone']['height'] == 2556, path
        assert o['scroll'] == 0, path
        required = {
            'today-new': ['4 Unread', '2 Unread', 'Updated'],
            'today-partial': ['3 Unread', 'Possible activity–bowel link'],
            'today-reviewed': ['All reviewed', 'Possible dairy–bloating link'],
            'goal-unread': ['2 unread findings', 'Dairy meals and bloating', 'Activity and bowel changes'],
            'goal-partial': ['1 unread finding', 'Reviewed', 'Activity and bowel changes'],
            'unread-list': ['4 findings to explore', 'Reduce Symptoms · Improved Digestion'],
            'updated-finding': ['What changed', 'Earlier records were mixed.', 'Energy findings stay on this device.'],
        }[scene['id']]
        if scene['id'].startswith('today-'):
            required += ['Reduce Symptoms', 'Improved Digestion', 'Improved Sleep', 'Be More Active',
                         'Improve Blood Pressure', 'See If a Treatment Is Working', 'More Energy', 'Less Stress',
                         'No clear pattern yet', 'Add symptom logs', 'Gathering context', 'Explore Insights']
            assert len(o['unreadRows']) == 8
        assert all(x in o['text'] for x in required), (path, required)
        if scene['id'] == 'today-reviewed':
            assert not any(r['unread'] == 'true' for r in o['unreadRows'])
        for row in o['unreadRows']:
            if row['unread'] != 'true':
                continue
            for field, role in [('background', 'unreadBackground'), ('text', 'unreadForeground')]:
                h = ROLES[role][theme]
                rgb = 'rgb('+', '.join(str(int(h[i:i+2], 16)) for i in (1, 3, 5))+')'
                assert row[field] == rgb, (path, field, row[field], rgb)
        observations.append(o)
        files.append(dict(scene=scene['id'], theme=theme, path=str(path.relative_to(REF)),
                          width=1179, height=2556, bytes=path.stat().st_size, sha256=digest(path), scroll_top=o['scroll']))
    assert observations[0]['text'] == observations[1]['text'], scene['id']

manifest = dict(
    version='today-overview-2026-11-05',
    status='Design and documentation approved; native implementation and publication pending',
    method=CAPTURE['method'], logical_size=[393, 852], pixel_size=[1179, 2556], screenshots=len(files),
    fixture_provenance='Illustrative relationships, coverage states and meaningful revisions. Not personal records or end-to-end analyzer validation.',
    reference_scope='Today overview and finding-review navigation. Existing full evidence, source, limitations and care contracts remain required.',
    source_audit='Local Plectara 9e4fb3d on 2026-11-05; support and remaining production contracts in Insights Findings Capabilities.',
    sources=SOURCES,
    runtime_asset_sha256={str(p.relative_to(REF)):digest(p) for p in sorted(REF.iterdir()) if p.suffix in ('.html', '.js', '.css')},
    scenes=SCENES, files=files)
(REF / 'references.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')

old = json.loads((OLD / 'references.json').read_text())
old_scenes = [s for s in old['scenes'] if s['id'] != 'today']
archive = ASSETS / 'connections-first-gallery-2026-10-27.html'
if not archive.exists():
    assert 'today-overview-2026-11-05' not in (ASSETS / 'index.html').read_text(), 'Cannot archive an already replaced gallery'
    shutil.copy2(ASSETS / 'index.html', archive)

def markdown_gallery(scenes, captures, base, heading):
    md = []
    for scene in scenes:
        md += [f'{heading} {scene["label"]}', '', scene['description'], '', '| Light | Dark |', '| --- | --- |']
        cells = []
        for theme in ('light', 'dark'):
            f = next(f for f in captures if f['scene'] == scene['id'] and f['theme'] == theme)
            path = ASSETS / base / f['path']
            assert digest(path) == f['sha256'], path
            url = '../../assets/app/insights-presentation/'+base+'/'+f['path']+'?v='+f['sha256'][:12]
            cells.append(f'[![{scene["label"]} — {theme}]({url}){{ width="280" loading="lazy" }}]({url})')
        md += ['| '+' | '.join(cells)+' |', '']
    return '\n'.join(md)

spec = ROOT / 'docs/specs/03-product/insights-presentation.md'
s = spec.read_text()
for marker, md in [
    ('TODAY_OVERVIEW', markdown_gallery(SCENES, files, REF.name, '###')),
    ('CONNECTIONS', markdown_gallery(old_scenes, old['files'], OLD.name, '####')),
]:
    s, n = re.subn(r'<!-- '+marker+r'_GALLERY_START -->.*?<!-- '+marker+r'_GALLERY_END -->',
                  lambda _: '<!-- '+marker+'_GALLERY_START -->\n'+md+'\n<!-- '+marker+'_GALLERY_END -->', s, flags=re.S)
    assert n == 1, marker
spec.write_text(s)

entries = []
for group, scenes, captures, base in [('Today · November 5', SCENES, files, REF.name), ('Insights and evidence · October 27', old_scenes, old['files'], OLD.name)]:
    for scene in scenes:
        entries.append(dict(key=base+'/'+scene['id'], group=group, base=base, scene=scene,
                            files=[f for f in captures if f['scene'] == scene['id']]))
options = ''
for group in dict.fromkeys(e['group'] for e in entries):
    options += '<optgroup label="'+escape(group)+'">'
    options += ''.join('<option value="'+escape(e['key'])+'">'+escape(e['scene']['label'])+'</option>' for e in entries if e['group'] == group)
    options += '</optgroup>'
html = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Today and Insights · Approved Design References · PL-OS</title>
<style>@font-face{font-family:Inter;src:url(connections-first-2026-10-27/source/inter-regular.woff)}@font-face{font-family:Inter;src:url(connections-first-2026-10-27/source/inter-semibold.woff);font-weight:600}*{box-sizing:border-box}body{margin:0;background:#f1f0ec;color:#192d38;font:16px/1.6 Inter,system-ui,sans-serif}main{max-width:1024px;margin:auto;padding:28px 24px}h1{font-size:28px;line-height:1.3;margin:8px 0}p{max-width:840px}a{color:#206668}select{font:inherit;min-height:48px;border:1px solid #567788;border-radius:9px;padding:8px 12px;background:#faf8f4;color:#192d38;max-width:100%}.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:24px}figure{margin:0;max-width:393px}img{display:block;width:100%;height:auto;border-radius:16px;box-shadow:0 4px 20px #192d3822}figcaption{font-weight:600;margin-bottom:12px}.notes{font-size:14px;color:#506f7e}.links{display:flex;gap:20px;flex-wrap:wrap;margin:16px 0}a:focus-visible,select:focus-visible{outline:3px solid #287e80;outline-offset:4px}@media(max-width:620px){.pair{grid-template-columns:1fr}main{padding:20px 16px}}</style></head><body>
<main><div class="links"><a href="../../../specs/03-product/insights-presentation/">Written specification</a><a href="../../../specs/03-product/insights-findings-capabilities/">Capability scope and source audit</a></div><h1>Today: a glance at every goal</h1><p>One compact card shows what is new, what is worth opening, and where more context is needed. Every selected goal stays visible; detailed evidence lives in Insights.</p><p class="notes">Today design and documentation approved November 5 · Publication and native implementation pending.</p><label for="scene">Reference view</label><br><select id="scene">__OPTIONS__</select><p id="description"></p><p class="notes" id="scope"></p><div class="pair" id="pair"></div><p class="notes">Original app-only captures: 1179 × 2556 pixels, directly rendered at 3×. Select an image to inspect full resolution. Browser-rendered design fixtures are not personal records or proof of analyzer behavior. Navigation examples supplement the complete written evidence and accessibility requirements.</p><div class="links"><a href="today-overview-2026-11-05/references.json">Today capture manifest</a><a href="connections-first-gallery-2026-10-27.html">Historical October 27 gallery</a></div></main><script>
const entries=__ENTRIES__,select=document.querySelector('#scene');
function render(){const e=entries.find(x=>x.key===select.value);document.querySelector('#description').textContent=e.scene.description;document.querySelector('#scope').textContent=e.base.startsWith('today-')?'November 5 · Current Today design and review-state references.':'October 27 · Retained Insights/evidence design. Older goal wording is historical; use the current catalog and no-finding rules in the written specification.';const pair=document.querySelector('#pair');pair.replaceChildren();for(const theme of ['light','dark']){const f=e.files.find(f=>f.theme===theme),fig=document.createElement('figure'),caption=document.createElement('figcaption'),a=document.createElement('a'),img=document.createElement('img'),live=document.createElement('a');caption.textContent=theme==='light'?'Light appearance':'Dark appearance';a.href=e.base+'/'+f.path+'?v='+f.sha256.slice(0,12);img.src=a.href;img.alt=e.scene.label+' in '+theme+' appearance';img.width=1179;img.height=2556;a.append(img);live.href=e.base+'/reference.html?scene='+e.scene.id+'&theme='+theme+'&scale=1';live.textContent='Open inspectable '+theme+' reference';fig.append(caption,a,live);pair.append(fig)}}select.addEventListener('change',render);render();</script></body></html>'''
html = html.replace('__OPTIONS__', options).replace('__ENTRIES__', json.dumps(entries))
(ASSETS / 'index.html').write_text(html)
print(f'Validated {len(files)} Today captures, seven matched theme pairs, 10 unread contrasts, provenance and states. Gallery retains 10 earlier Insights/evidence images; superseded Today archived.')
