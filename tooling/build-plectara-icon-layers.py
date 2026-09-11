"""Export exact, unmasked SVG layers for the approved Liquid Glass app icon."""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'assets/brand/plectara'
DEST = BASE / 'platform/ios/liquid-glass/layers'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
source = ET.parse(BASE / 'source/plectara-app-icon.svg').getroot()
outer = source.find(f'{{{NS}}}g')
figure = outer.find(f'{{{NS}}}g')
names = ['07-jade-head', '01-jade-upper', '06-teal-ribbon',
         '02-slate-ribbon', '05-copper-front', '03-copper-lower', '04-jade-lower']
assert len(figure) == len(names) == 7
DEST.mkdir(parents=True, exist_ok=True)
for name, shape in zip(names, figure):
    layer = ET.Element(f'{{{NS}}}svg', {
        'width': '1024', 'height': '1024', 'viewBox': '0 0 1024 1024',
        'role': 'img', 'aria-labelledby': 'title',
    })
    ET.SubElement(layer, f'{{{NS}}}title', {'id': 'title'}).text = f'Plectara — {name[3:]}'
    placement = ET.SubElement(layer, outer.tag, dict(outer.attrib))
    group = ET.SubElement(placement, figure.tag, dict(figure.attrib))
    group.append(deepcopy(shape))
    (DEST / f'{name}.svg').write_text(ET.tostring(layer, encoding='unicode') + '\n')
print('Exported seven exact SVG layers, preserving all original paths and transforms.')
