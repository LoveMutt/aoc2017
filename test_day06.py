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

    def test_proc(self):
        d = Distributor(banks=get_test_input())
        d.proc()
        log.debug('Found repeating sequence: {}'.format(d.banks))
        self.assertEqual(d.registers[0], 5)
        self.assertEqual(d.registers[1], 4 + 5)
