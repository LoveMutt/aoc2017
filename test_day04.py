import unittest

from day04 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
    def test_has_duplicate(self):
        self.assertFalse(has_duplicates('aa bb cc dd ee'))
        self.assertTrue(has_duplicates('aa bb cc dd aa'))
        self.assertFalse(has_duplicates('aa bb cc dd aaa'))

    def test_is_anagram(self):
        tuples = [
            ('a', 'a', True),
            ('ab', 'a', False),
            ('ab', 'ba', True),
            ('abcdefgh', 'cdabfgeh', True),
        ]

        for s1, s2, b in tuples:
            self.assertEqual(is_anagram(s1, s2), b)
