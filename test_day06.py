import unittest

from day06 import *
from common import get_logger

log = get_logger(__name__)

def get_test_input():
    return [0, 2, 7, 0]

class TestDay(unittest.TestCase):
    def test_distributor_ctx(self):
        d = Distributor(banks=get_test_input())
        self.assertIsInstance(d, Distributor)

    def test_seek_next_val(self):
        d = Distributor(banks=get_test_input())
        d.seek_next_index()
        self.assertEqual(d.index, 2)
