import unittest

from day03 import *
from common import get_logger

log = get_logger(__name__)

class TestDay(unittest.TestCase):
	def test_turn(self):
		s = CartesianSpiral()
		self.assertEqual(s._direction, RIGHT)
		s.turn()
		self.assertEqual(s._direction, UP)
		s.turn()
		self.assertEqual(s._direction, LEFT)
		s.turn()
		self.assertEqual(s._direction, DOWN)
		s.turn()
		self.assertEqual(s._direction, RIGHT)

	def test_incr_coordinates(self):
		s = CartesianSpiral()
		self.assertEqual(s._target_x, 0)
		self.assertEqual(s._target_y, 0)
		s.incr_coordinates()
		self.assertEqual(s._target_x, 1)
		self.assertEqual(s._target_y, 0)
		s.turn()
		s.incr_coordinates()
		self.assertEqual(s._target_x, 1)
		self.assertEqual(s._target_y, 1)
		s.turn()
		s.incr_coordinates()
		self.assertEqual(s._target_x, 0)
		self.assertEqual(s._target_y, 1)
		s.incr_coordinates()
		self.assertEqual(s._target_x, -1)
		self.assertEqual(s._target_y, 1)
		s.turn()
		s.incr_coordinates()
		self.assertEqual(s._target_x, -1)
		self.assertEqual(s._target_y, 0)

	def test_spiral_to(self):
		s = CartesianSpiral()
		val = 1
		log.info('spiral_to: {}'.format(val))
		s.spiral_to(val)
		self.assertEqual(s._target_val, 1)
		self.assertEqual(s._target_x, 0)
		self.assertEqual(s._target_y, 0)
		val = 2
		s = CartesianSpiral()
		log.info('spiral_to: {}'.format(val))
		s.spiral_to(val)
		self.assertEqual(s._target_val, 2)
		self.assertEqual(s._target_x, 1)
		self.assertEqual(s._target_y, 0)
		val = 3
		s = CartesianSpiral()
		log.info('spiral_to: {}'.format(val))
		s.spiral_to(val)
		self.assertEqual(s._target_val, 3)
		self.assertEqual(s._target_x, 1)
		self.assertEqual(s._target_y, 1)
		val = 23
		s = CartesianSpiral()
		log.info('spiral_to: {}'.format(val))
		s.spiral_to(val)
		self.assertEqual(s._target_val, 23)
		self.assertEqual(s._target_x, 0)
		self.assertEqual(s._target_y, -2)

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
