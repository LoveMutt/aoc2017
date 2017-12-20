import unittest

from day10 import *
from common import get_logger

log = get_logger(__name__)


def get_test_inputs():
    return [3, 4, 1, 5]


def init_test_elements():
    return [0, 1, 2, 3, 4]


class TestDay(unittest.TestCase):
    def setUp(self):
        self.elements = init_test_elements()
        self.inputs = get_test_inputs()

    def test_reverse_sublist(self):
        l_rev = reverse_slice(init_test_elements(), 0, 2)
        self.assertListEqual([1, 0, 2, 3, 4], l_rev)
        l_rev = reverse_slice(l_rev, 2, 2)
        self.assertListEqual([1, 0, 3, 2, 4], l_rev)
        l_rev = reverse_slice(l_rev, 4, 2)
        self.assertListEqual([4, 0, 3, 2, 1], l_rev)

    def test_hash(self):
        self.assertEqual(12, hash(get_test_inputs(), init_test_elements()))
