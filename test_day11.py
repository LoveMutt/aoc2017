import unittest

from day11 import *
from common import get_logger

log = get_logger(__name__)


def get_test_lengths():
    return [3, 4, 1, 5]


def get_test_inputs():
    return [0, 1, 2, 3, 4]


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

    def test_move(self):
        hg = HexGrid()
        hg.move('n')
        self.assertTupleEqual(hg.coordinates, (0, 1))

        hg.reset()
        hg.move('s')
        self.assertTupleEqual(hg.coordinates, (0, -1))

        hg.reset()
        hg.move('e')
        self.assertTupleEqual(hg.coordinates, (1, 0))

        hg.reset()
        hg.move('w')
        self.assertTupleEqual(hg.coordinates, (-1, 0))

        hg.reset()
        hg.move('se')
        self.assertTupleEqual(hg.coordinates, (1, -1))

        hg.reset()
        hg.move('sw')
        self.assertTupleEqual(hg.coordinates, (-1, -1))

        hg.reset()
        hg.move('ne')
        self.assertTupleEqual(hg.coordinates, (1, 1))

        hg.reset()
        hg.move('nw')
        self.assertTupleEqual(hg.coordinates, (-1, 1))

    def test_distance(self):
        hg = HexGrid()
        hg.move('n')
        self.assertEqual(1, hg.distance)
        hg.move('n')
        self.assertEqual(2, hg.distance)
        hg.move('s')
        hg.move('s')
        self.assertEqual(0, hg.distance)