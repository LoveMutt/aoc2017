import unittest

from day13 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
    def setUp(self):
        self.t1 = (0, 3)
        self.t2 = (1, 2)
        self.t3 = (0, 4)

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
        s = Scanner(layers=[self.t1, self.t2])
        self.assertEqual(0, s.score)
        s.step()
        self.assertEqual(0, s.score)
        s.step()
        self.assertEqual(2, s.score)
