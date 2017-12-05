import unittest

from day01 import *
from common import get_logger

log = get_logger(__name__)

class TestDay(unittest.TestCase):
	test1 = [1, 1, 2, 2]
	test2 = [1, 1, 1, 1]
	test3 = [1, 2, 3, 4]
	test4 = [9, 1, 2, 1, 2, 1, 2, 9]
	test5 = [1, 2, 1, 2]
	test6 = [1, 2, 2, 1]
	test7 = [1, 2, 3, 4, 2, 5]
	test8 = [1, 2, 3, 1, 2, 3]
	test9 = [1, 2, 1, 3, 1, 4, 1, 5]

	def test_matches_next(self):
		self.assertTrue(matches_next(self.test1, 0))
		self.assertFalse(matches_next(self.test1, 1))
		self.assertTrue(matches_next(self.test4, 7))

	def test_sum_matches(self):
		self.assertEqual(sum_matches(self.test1), 3)
		self.assertEqual(sum_matches(self.test2), 4)
		self.assertEqual(sum_matches(self.test3), 0)
		self.assertEqual(sum_matches(self.test4), 9)

	def test_sum_matches_part2(self):
		self.assertEqual(sum_matches_part2(self.test5), 6)
		self.assertEqual(sum_matches_part2(self.test6), 0)
		self.assertEqual(sum_matches_part2(self.test7), 4)
		self.assertEqual(sum_matches_part2(self.test8), 12)
		self.assertEqual(sum_matches_part2(self.test9), 4)
