import unittest

from day07 import *
from common import get_logger

log = get_logger(__name__)

def get_test_input():
    s = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    return s

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
