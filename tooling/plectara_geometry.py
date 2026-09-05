"""Vector-only clearance construction and outline recovery for the brand build."""
import xml.etree.ElementTree as ET
from fontTools.pens.basePen import BasePen
from fontTools.svgLib.path import parse_path
from shapely.geometry import Polygon
from shapely.ops import unary_union
from PIL import Image
import vtracer

GAP = 6.0


class OutlinePen(BasePen):
    def __init__(self):
        super().__init__(None)
        self.points = []

    def _moveTo(self, p):
        self.points.append(p)

    def _lineTo(self, p):
        self.points.append(p)

    def _curveToOne(self, p1, p2, p3):
        p0 = self._getCurrentPoint()
        # Subpixel approximation of each Bezier before geometric offsets.
        for i in range(1, 257):
            t = i / 256
            u = 1 - t
            self.points.append(tuple(u**3*p0[k] + 3*u*u*t*p1[k] +
                                     3*u*t*t*p2[k] + t**3*p3[k] for k in (0, 1)))

    def _closePath(self):
        pass


def polygon(d):
    pen = OutlinePen()
    parse_path(d, pen)
    result = Polygon(pen.points)
    assert result.is_valid, 'Invalid ribbon outline'
    return result


def path_data(shape):
    # Dense vector outlines retain the true offset, with <0.01 source-unit
    # simplification tolerance. No raster masks or background-colored strokes.
    def ring(coords):
        points = list(coords)
        return 'M' + ' L'.join(f'{x:.4f} {y:.4f}' for x, y in points[:-1]) + ' Z'
    shape = shape.simplify(.008, preserve_topology=True)
    polygons = [shape] if shape.geom_type == 'Polygon' else list(shape.geoms)
    return ' '.join(ring(p.exterior.coords) + ' ' +
                    ' '.join(ring(h.coords) for h in p.interiors) for p in polygons)


def spaced_ribbons(ribbons):
    raw = [polygon(d) for _, d in ribbons]
    # Foreground boundaries define the gap, never two independently drawn edges.
    finished = {1: raw[1]}
    dependencies = {0: [1], 3: [1], 2: [1, 3], 4: [3], 5: [3, 4]}
    for index in (0, 3, 2, 4, 5):
        neighbors = unary_union([finished[n] for n in dependencies[index]])
        finished[index] = raw[index].difference(neighbors.buffer(GAP, quad_segs=64))
        assert finished[index].geom_type == 'Polygon' and not finished[index].is_empty
        distance = finished[index].distance(neighbors)
        assert abs(distance - GAP) < .015, (index, distance)
    # Every adjacent pair must remain separated after all clipping operations.
    for i, neighbors in dependencies.items():
        for j in neighbors:
            assert finished[i].distance(finished[j]) >= GAP - .015
    return [(color, path_data(finished[i])) for i, (color, _) in enumerate(ribbons)]


def approved_wordmark(reference, retrace=False):
    """Recover the actual approved lettering, not a guessed substitute font."""
    cached = reference.parent.parent / 'source/plectara-wordmark.svg'
    if cached.exists() and not retrace:
        root = ET.parse(cached).getroot()
        paths = [dict(n.attrib) for n in root.iter() if n.tag.endswith('}path')]
        return (float(root.attrib['width']), float(root.attrib['height'])), paths
    region = Image.open(reference).convert('RGB').crop((510, 280, 1440, 485))
    mask = region.convert('L').point(lambda p: 255 if p < 125 else 0)
    bounds = mask.getbbox()
    assert bounds is not None
    mask = mask.crop(bounds)
    pixels = [(0, 0, 0, 255) if p else (255, 255, 255, 255)
              for p in mask.get_flattened_data()]
    traced = vtracer.convert_pixels_to_svg(
        pixels, mask.size, colormode='binary', mode='spline',
        filter_speckle=8, corner_threshold=70, length_threshold=3.5,
        max_iterations=10, splice_threshold=45, path_precision=4)
    root = ET.fromstring(traced)
    paths = [dict(n.attrib) for n in root.iter() if n.tag.endswith('}path')]
    assert len(paths) >= 8, 'Expected all eight wordmark letters'
    return mask.size, paths


def wordmark_body(paths, color):
    return ''.join('<path ' + ' '.join(f'{key}="{value}"' for key, value in
                   {**attrs, 'fill': color}.items()) + '/>' for attrs in paths)
