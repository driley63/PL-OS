"""Validate current reference captures and publish local documentation assets."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets/app/insights-presentation'
REF = ASSETS / 'connections-first-2026-10-27'
SCENES = json.loads((ROOT / 'tooling/insights-connections-reference/scenes.json').read_text())
CAPTURE = json.loads((REF / 'capture-observations.json').read_text())
SOURCES = json.loads((REF / 'source-hashes.json').read_text())
assert CAPTURE['sourceHashes'] == SOURCES, 'Recapture changed reference sources'
for path, expected in SOURCES.items():
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path
files = []
for scene in SCENES:
    observations = []
    for theme in ('light', 'dark'):
        path = REF / 'screens' / f'{scene["id"]}-{theme}.jpg'
        with Image.open(path) as image:
            assert image.format == 'JPEG' and image.size == (1179, 2556) and image.mode == 'RGB', path
        observation = next(o for o in CAPTURE['observations'] if o['scene'] == scene['id'] and o['theme'] == theme)
        assert observation['ready'] and observation['images'] and observation['icons'] > 0, path
        assert not observation['unrendered'] and not observation['overflow'], path
        assert observation['contrasts'] and all(c['ratio'] >= 4.5 for c in observation['contrasts']), path
        assert observation['phone'] == {'width':1179, 'height':2556}, path
        for unsupported in ['Consistent Pattern', 'Developing Pattern', 'three weeks', 'No Walk Reported', '4.1 / 5', 'Sleep and Activity Check']:
            assert unsupported not in observation['text'], (path, unsupported)
        if scene['id'] == 'energy':
            assert '7.2 / 10' in observation['text'] and '5.1 / 10' in observation['text']
            assert 'Ask About' not in observation['text'] and 'stays on your device' in observation['text']
        if scene['id'] == 'details':
            assert '3 of 8' in observation['text'] and '3 of 12' in observation['text']
            assert 'before or after' in observation['text'] and 'unknown, not symptom-free' in observation['text']
        observations.append(observation)
        files.append(dict(scene=scene['id'], theme=theme, path=str(path.relative_to(REF)),
                          width=1179, height=2556, bytes=path.stat().st_size,
                          sha256=hashlib.sha256(path.read_bytes()).hexdigest(), scroll_top=observation['scroll']))
    assert observations[0]['text'] == observations[1]['text'], f'Theme content mismatch: {scene["id"]}'
manifest = dict(version='connections-first-2026-10-27', status='Approved design, capability scope and documentation publication; native implementation pending',
    method='Browser rasterization at 3x CSS zoom; full app region; original JPEG bytes, no resampling',
    logical_size=[393,852], pixel_size=[1179,2556], screenshots=len(files),
    fixture_provenance='Illustrative fixture values shaped to existing meal-tag and wellbeing analyzer families. Not real user data or end-to-end analyzer verification.',
    maturity='Neutral Possible Connection until evaluated G2/G3-lite support is implemented.',
    source_audit='Plectara 3044e87, reviewed 2026-10-27; owner decisions retained in the capability specification',
    sources=SOURCES, runtime_asset_sha256={str(p.relative_to(REF)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(REF.rglob('*')) if p.is_file() and p.suffix in ('.css','.js','.woff','.svg','.webp','.html')},
    scenes=SCENES, files=files)
(REF/'references.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')

md=[]
for scene in SCENES:
    md += [f'### {scene["label"]}', '', scene['description'], '', '| Light | Dark |', '| --- | --- |']
    columns=[]
    for theme in ('light','dark'):
        f=next(f for f in files if f['scene']==scene['id'] and f['theme']==theme)
        url='../../assets/app/insights-presentation/connections-first-2026-10-27/'+f['path']+'?v='+f['sha256'][:12]
        columns.append(f'[![{scene["label"]} — {theme}]({url}){{ width="280" loading="lazy" }}]({url})')
    md += ['| '+' | '.join(columns)+' |','']
p=ROOT/'docs/specs/03-product/insights-presentation.md'
s=p.read_text()
s,n=re.subn(r'<!-- CONNECTIONS_GALLERY_START -->.*?<!-- CONNECTIONS_GALLERY_END -->',lambda _:'<!-- CONNECTIONS_GALLERY_START -->\n'+'\n'.join(md)+'\n<!-- CONNECTIONS_GALLERY_END -->',s,flags=re.S)
assert n==1
p.write_text(s)
options=''.join(f'<option value="{x["id"]}">{escape(x["label"])}</option>' for x in SCENES)
html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Insights · Connection-led Design References · PL-OS</title>
<style>@font-face{font-family:Inter;src:url(connections-first-2026-10-27/source/inter-regular.woff)}@font-face{font-family:Inter;src:url(connections-first-2026-10-27/source/inter-semibold.woff);font-weight:600}*{box-sizing:border-box}body{margin:0;background:#f1f0ec;color:#192d38;font:16px/1.6 Inter,system-ui,sans-serif}main{max-width:1024px;margin:auto;padding:28px 24px}h1{font-size:28px;line-height:1.3;margin:8px 0}h2{font-size:18px}p{max-width:820px}a{color:#206668}select{font:inherit;min-height:48px;border:1px solid #567788;border-radius:9px;padding:8px 12px;background:#faf8f4;color:#192d38;max-width:100%}.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:24px}figure{margin:0;max-width:393px}img{display:block;width:100%;height:auto;border-radius:16px;box-shadow:0 4px 20px #192d3822}figcaption{font-weight:600;margin-bottom:12px}.notes{font-size:14px;color:#506f7e}.links{display:flex;gap:20px;flex-wrap:wrap;margin:16px 0}a:focus-visible,select:focus-visible{outline:3px solid #287e80;outline-offset:4px}@media(max-width:620px){.pair{grid-template-columns:1fr}main{padding:20px 16px}}</style>
<main><div class="links"><a href="../../../specs/03-product/insights-presentation/">Written specification</a><a href="../../../specs/03-product/insights-findings-capabilities/">Capability decisions</a></div><h1>Insights: connections first</h1><p>Potential links between habits and symptoms or wellbeing lead each card. Evidence, counts and limitations are available in the detail view.</p><p class="notes">Approved design and documentation · Native implementation pending. Current references use Possible Connection until evaluated maturity support exists.</p><label for="scene">Reference view</label><br><select id="scene">__OPTIONS__</select><p id="description"></p><div class="pair" id="pair"></div><p class="notes">Each app-only image is 1179 × 2556 pixels, rendered directly at 3×. Select an image to inspect its original resolution. Values and dates are illustrative, not actual user findings. These browser-rendered references do not implement analysis, persistence or native services.</p><div class="links"><a href="connections-first-2026-10-27/references.json">Capture manifest</a><a href="previous-goal-comparison-gallery.html">Historical comparison-first gallery</a></div></main><script>
const scenes=__SCENES__,files=__FILES__,base='connections-first-2026-10-27/';
function render(){const scene=scenes.find(s=>s.id===document.querySelector('#scene').value);document.querySelector('#description').textContent=scene.description;const pair=document.querySelector('#pair');pair.replaceChildren();for(const theme of ['light','dark']){const f=files.find(f=>f.scene===scene.id&&f.theme===theme);const figure=document.createElement('figure'),caption=document.createElement('figcaption'),a=document.createElement('a'),img=document.createElement('img'),live=document.createElement('a');caption.textContent=theme==='light'?'Light appearance':'Dark appearance';a.href=base+f.path+'?v='+f.sha256.slice(0,12);img.src=a.href;img.alt=scene.label+' in '+theme+' appearance';img.width=1179;img.height=2556;a.append(img);live.href=base+'reference.html?scene='+scene.id+'&theme='+theme+'&scale=1';live.textContent='Open inspectable '+theme+' reference';figure.append(caption,a,live);pair.append(figure)}}document.querySelector('#scene').addEventListener('change',render);render();</script></html>'''
html=html.replace('__OPTIONS__',options).replace('__SCENES__',json.dumps(SCENES)).replace('__FILES__',json.dumps(files))
(ASSETS/'index.html').write_text(html)
print(f'Validated {len(files)} captures: original RGB JPEG, 1179x2556, identical theme content, loaded assets, scope-correct fixtures and source hashes. Gallery and specification updated.')
