import unittest

from day05 import *
from common import get_logger

log = get_logger(__name__)

TEST_INPUT = ['0', '3', '0', '1', '-3']

class TestDay(unittest.TestCase):
    def test_proc(self):
        js = JmpSet(jmps=TEST_INPUT)
        js.proc()
        self.assertEqual(js.num_processed, 4)
