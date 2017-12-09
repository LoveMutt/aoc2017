import unittest

from day05 import *
from common import get_logger

log = get_logger(__name__)

def get_test_input():
    return [0, 3, 0, 1, -3]

class TestDay(unittest.TestCase):
    def test_proc(self):
        js = JmpSet(jmps=get_test_input())
        js.proc()
        self.assertEqual(js.steps, 5)

    def test_proc_part2(self):
        js = JmpSet(jmps=get_test_input())
        js.proc(part2=True)
        self.assertEqual(js.steps, 10)
        log.debug('Array is: {}'.format(js.jmps))
