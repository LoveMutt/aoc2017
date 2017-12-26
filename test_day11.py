import unittest

from day11 import *
from common import get_logger

log = get_logger(__name__)

STR = 'string'
DIS = 'distance'


class TestDay(unittest.TestCase):
    def setUp(self):
        self.test_inputs = [
            {STR: 'ne,ne,ne', DIS: 3},
            {STR: 'ne,ne,sw,sw', DIS: 0},
            {STR: 'ne,ne,s,s', DIS: 2},
            {STR: 'se,sw,se,sw,sw', DIS: 3},
        ]

    def test_parse_input(self):
        for d in self.test_inputs:
            self.assertIsInstance(parse_input(d.get(STR)), list)

    def test_distance(self):
        for d_inputs in self.test_inputs:
            hg = Traveler()
            l_dirs = parse_input(d_inputs.get(STR))
            distance = d_inputs.get(DIS)
            hg.follow(l_dirs)
            self.assertEqual(distance, hg.distance)
