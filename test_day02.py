import unittest

from day02 import *
from common import get_logger

log = get_logger(__name__)

class TestDay02(unittest.TestCase):
	test = \
'''5	1	9	5
7	5	3
2	4	6	8'''

	test2 = \
'''5	9	2	8
9	4	7	3
3	8	6	5'''

	def test_parse_input(self):
		A = parse_input(self.test)
		self.assertIsInstance(A, list)
		for a in A:
			self.assertIsInstance(a, list)
			for i in a:
				self.assertIsInstance(i, int)

	def test_checksum(self):
		cs = checksum(parse_input(self.test))
		self.assertEqual(cs, 18)

	def test_checksum_part2(self):
		cs = checksum_part2(parse_input(self.test2))
		self.assertEqual(cs, 9)

	def test_evenly_divisible(self):
		self.assertTrue(evenly_divisible(2, 6))
		self.assertTrue(evenly_divisible(3, 6))
		self.assertFalse(evenly_divisible(3, 4))
