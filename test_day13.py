import unittest

from day13 import *
from common import get_logger

log = get_logger(__name__)

S_INPUT = '''0: 3
1: 2
4: 4
6: 4'''


def get_init_layers():
    return parse_input(S_INPUT)


class TestDay(unittest.TestCase):
    def setUp(self):
        self.t1 = (0, 3)
        self.t2 = (1, 2)
        self.t3 = (0, 4)

        self.layer1 = Layer(idepth=self.t1[0], irange=self.t1[1])
        self.layer2 = Layer(idepth=self.t2[0], irange=self.t2[1])
        self.layer3 = Layer(idepth=self.t3[0], irange=self.t3[1])

    def test_parse(self):
        inputs = parse_input(S_INPUT)
        self.assertIsInstance(inputs, list)
        self.assertEqual(7, len(inputs))
        for i in inputs:
            self.assertIsInstance(i, Layer)

    def test_move(self):
        lyr = Layer(irange=3)
        self.assertEqual(0, lyr.start_depth)
        self.assertEqual(1, lyr.end_depth)
        lyr.move()
        self.assertEqual(1, lyr.start_depth)
        self.assertEqual(2, lyr.end_depth)
        lyr.move()
        self.assertEqual(2, lyr.start_depth)
        self.assertEqual(1, lyr.end_depth)
        lyr.move()
        self.assertEqual(1, lyr.start_depth)
        self.assertEqual(0, lyr.end_depth)
        lyr.move()
        self.assertEqual(0, lyr.start_depth)
        self.assertEqual(1, lyr.end_depth)
        lyr = Layer(idepth=1, irange=2)
        self.assertEqual(1, lyr.start_depth)
        self.assertEqual(0, lyr.end_depth)
        lyr.move()
        self.assertEqual(0, lyr.start_depth)
        self.assertEqual(1, lyr.end_depth)

    def test_step(self):
        s = Scanner(layers=[self.layer1, self.layer2])
        self.assertEqual(0, s.score)
        s.step()
        self.assertEqual(0, s.score)
        s.step()
        self.assertEqual(2, s.score)

    def test_run(self):
        layers = parse_input(S_INPUT)
        s = Scanner(layers=layers)
        s.run()
        self.assertEqual(24, s.score)

    def test_delay(self):
        delay = 0
        s = Scanner(delay=delay, layers=get_init_layers())
        s.run()
        self.assertEqual(24, s.score)
        delay = 1
        s = Scanner(delay=delay, layers=get_init_layers())
        layer = s._layers[0]  # type: Layer
        self.assertEqual(1, layer.start_depth)
        delay = 10
        s = Scanner(delay=delay, layers=get_init_layers())
        s.run()
        self.assertEqual(0, s.score)
        for i in [0, 1, 4, 6]:
            self.assertEqual(1, s._layers[i].start_depth)
        self.assertEqual(delay + len(s._layers), s._steps)
