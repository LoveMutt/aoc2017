import unittest

from day04 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
    def test_has_duplicate(self):
        self.assertFalse(has_duplicates('aa bb cc dd ee'))
        self.assertTrue(has_duplicates('aa bb cc dd aa'))
        self.assertFalse(has_duplicates('aa bb cc dd aaa'))
