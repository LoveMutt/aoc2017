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
