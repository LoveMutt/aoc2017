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

    def test_move(self):
        # See http://keekerdc.com/wp-content/uploads/2011/03/HexGridLandscapeTriCoordinates.gif
        # Rotate the axes in that image by 30 degrees to the right (so the flat top is North)
        hg = HexGrid()
        hg.move('n')
        self.assertTupleEqual(hg.coordinates, (0, 1, -1))

        hg.reset()
        hg.move('s')
        self.assertTupleEqual(hg.coordinates, (0, -1, 1))

        hg.reset()
        hg.move('e')
        self.assertTupleEqual(hg.coordinates, (1, -1, 0))

        hg.reset()
        hg.move('w')
        self.assertTupleEqual(hg.coordinates, (-1, 1, 0))

        hg.reset()
        hg.move('se')
        self.assertTupleEqual(hg.coordinates, (1, -2, 1))

        hg.reset()
        hg.move('sw')
        self.assertTupleEqual(hg.coordinates, (-1, 0, 1))

        hg.reset()
        hg.move('ne')
        self.assertTupleEqual(hg.coordinates, (1, 0, -1))

        hg.reset()
        hg.move('nw')
        self.assertTupleEqual(hg.coordinates, (-1, 2, -1))

    def test_distance(self):
        for d_inputs in self.test_inputs:
            hg = HexGrid()
            l_dirs = parse_input(d_inputs.get(STR))
            distance = d_inputs.get(DIS)
            hg.follow(l_dirs)
            self.assertEqual(distance, hg.distance)
