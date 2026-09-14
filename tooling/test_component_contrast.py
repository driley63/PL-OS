"""Reference calculations and regressions found in the consuming app."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'component_contrast', Path(__file__).with_name('check-component-contrast.py'))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class ContrastTests(unittest.TestCase):
    def test_reference_extremes(self):
        self.assertEqual(checks.contrast(checks.rgb('#000000'), checks.rgb('#FFFFFF')), 21)
        self.assertEqual(checks.contrast(checks.rgb('#223D49'), checks.rgb('#223D49')), 1)

    def test_alpha_is_composited_before_luminance(self):
        pair = dict(foreground='#FFFFFF', foregroundAlpha=.5,
                    background='#000000', minimum=4.5)
        actual, passed = checks.evaluate(pair)
        self.assertAlmostEqual(actual, 5.280822809644651)
        self.assertTrue(passed)

    def test_multiple_background_layers(self):
        pair = dict(foreground='#FFFFFF', background='#000000', minimum=4.5,
                    backgroundLayers=[dict(color='#FFFFFF', alpha=.5),
                                      dict(color='#000000', alpha=.5)])
        actual, _ = checks.evaluate(pair)
        self.assertAlmostEqual(actual, checks.contrast((1, 1, 1), (.25, .25, .25)))

    def test_do_not_round_a_near_pass(self):
        pair = dict(foreground='#B7A7FF', background='#264C4B', minimum=4.5)
        self.assertTrue(checks.evaluate(pair)[1])
        pair['foregroundAlpha'] = .9995
        actual, passed = checks.evaluate(pair)
        self.assertEqual(f'{actual:.2f}', '4.50')
        self.assertFalse(passed)

    def test_app_regressions(self):
        for fg, bg, minimum in [('#567788', '#2F5560', 4.5),
                                ('#B53E3E', '#2F5560', 3),
                                ('#287E80', '#223D49', 3),
                                ('#7B61FF', '#223D49', 4.5),
                                ('#FFFFFF', '#7B61FF', 4.5)]:
            with self.subTest(foreground=fg, background=bg):
                self.assertFalse(checks.evaluate(dict(
                    foreground=fg, background=bg, minimum=minimum))[1])

    def test_invalid_alpha(self):
        with self.assertRaises(ValueError):
            checks.composite((1, 1, 1), (0, 0, 0), 1.1)


if __name__ == '__main__':
    unittest.main()
