import unittest

from day13 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
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
