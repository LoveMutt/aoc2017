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

    def test_has_anagrams(self):
        tuples = [
            ('abcde fghij', False),
            ('abcde xyz ecdab', True),
            ('a ab abc abd abf abj', False),
            ('iiii oiii ooii oooi oooo', False),
            ('oiii ioii iioi iiio', True),
        ]

        for s, b in tuples:
            self.assertEqual(has_anagrams(s), b)
