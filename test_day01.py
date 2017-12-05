import unittest

from day01 import matches_next, sum_matches
from common import get_logger

log = get_logger(__name__)

class TestDay01(unittest.TestCase):
	test1 = [1, 1, 2, 2]
	test2 = [1, 1, 1, 1]
	test3 = [1, 2, 3, 4]
	test4 = [9, 1, 2, 1, 2, 1, 2, 9]

	def test_matches_next(self):
		self.assertTrue(matches_next(self.test1, 0))
		self.assertFalse(matches_next(self.test1, 1))
		self.assertTrue(matches_next(self.test4, 7))

	def test_sum_matches(self):
		self.assertEqual(sum_matches(self.test1), 3)
		self.assertEqual(sum_matches(self.test2), 4)
		self.assertEqual(sum_matches(self.test3), 0)
		self.assertEqual(sum_matches(self.test4), 9)
