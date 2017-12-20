import unittest

from day10 import *
from common import get_logger

log = get_logger(__name__)


def get_test_lengths():
    return [3, 4, 1, 5]


def get_test_inputs():
    return [0, 1, 2, 3, 4]


class TestDay(unittest.TestCase):
    def setUp(self):
        self.inputs = get_test_inputs()
        self.lengths = get_test_lengths()

    def test_reverse_sublist(self):
        l_rev = reverse_slice(get_test_inputs(), 0, 2)
        self.assertListEqual([1, 0, 2, 3, 4], l_rev)
        l_rev = reverse_slice(l_rev, 2, 2)
        self.assertListEqual([1, 0, 3, 2, 4], l_rev)
        l_rev = reverse_slice(l_rev, 4, 2)
        self.assertListEqual([4, 0, 3, 2, 1], l_rev)

    def test_hash(self):
        hash_val, _, _ = hash(self.lengths, self.inputs)
        self.assertEqual(12, hash_val)

    def test_convert_list_to_code(self):
        self.assertListEqual([49,44,50,44,51], convert_list_to_ascii('1,2,3'))

    def test_hash_n(self):
        self.assertEqual(hash(l_lengths=self.lengths, l_numbers=self.inputs)[0],
                         hash_n(l_lengths=self.lengths, l_numbers=self.inputs, n=1)[0])
        
    def test_dense_hash(self):
        input = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        vals = dense_hash(input)
        self.assertEqual(64, vals[0])
