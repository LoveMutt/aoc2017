import unittest

from day03 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
    def test_distance_to_target(self):
        s = CartesianSpiral()
        val = 1
        log.info('val: {}'.format(val))
        self.assertEqual(s.distance_to_target(val), 0)
        val = 12
        s = CartesianSpiral()
        log.info('val: {}'.format(val))
        self.assertEqual(s.distance_to_target(val), 3)
        val = 23
        s = CartesianSpiral()
        log.info('val: {}'.format(val))
        self.assertEqual(s.distance_to_target(val), 2)
        val = 1024
        s = CartesianSpiral()
        log.info('val: {}'.format(val))
        self.assertEqual(s.distance_to_target(val), 31)

    def test_square(self):
        square = CartesianSpiral.Square()
        self.assertIsInstance(square, CartesianSpiral.Square)

    def test_square_adjacents(self):
        sq = CartesianSpiral.Square(1, 0, 0)
        adj_set = {(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)}
        self.assertTrue(set(sq.adjacents).issubset(adj_set))
        self.assertTrue(set(sq.adjacents).issuperset(adj_set))

    def test_square_adj(self):
        cs = CartesianSpiral()
        index = 1
        cs.spiral_to(index=index, part1=False)
        csq = cs.get_coordsquare(index)  # type: CoordSquare
        self.assertEqual(csq.square.value, 1)
        index = 2
        cs.spiral_to(index=index, part1=False)
        csq = cs.get_coordsquare(index)  # type: CoordSquare
        self.assertEqual(csq.square.value, 1)
        index = 3
        cs.spiral_to(index=index, part1=False)
        csq = cs.get_coordsquare(index)  # type: CoordSquare
        self.assertEqual(csq.square.value, 2)
        index = 4
        cs.spiral_to(index=index, part1=False)
        csq = cs.get_coordsquare(index)  # type: CoordSquare
        self.assertEqual(csq.square.value, 4)
        index = 5
        cs.spiral_to(index=index, part1=False)
        csq = cs.get_coordsquare(index)  # type: CoordSquare
        self.assertEqual(csq.square.value, 5)
