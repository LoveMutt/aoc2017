import unittest

from day02 import *
from common import get_logger

log = get_logger(__name__)

class TestDay02(unittest.TestCase):
	test = \
'''5	1	9	5
7	5	3
2	4	6	8'''

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
