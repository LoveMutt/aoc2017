import unittest

from day09 import *
from common import get_logger

log = get_logger(__name__)

TEXT = 'text'
SCORE = 'score'


class TestDay(unittest.TestCase):
    def setUp(self):
        self.inputs = {
            1: {TEXT: '{}',
                SCORE: 1},
            2: {TEXT: '{{{}}}',
                SCORE: 6},
            3: {TEXT: '{{},{}}',
                SCORE: 6},
            4: {TEXT: '{{{},{},{{}}}}',
                SCORE: 16},
            5: {TEXT: '{<a>,<a>,<a>,<a>}',
                SCORE: 1},
            6: {TEXT: '{{<ab>},{<ab>},{<ab>},{<ab>}}',
                SCORE: 9},
            7: {TEXT: '{{<!!>},{<!!>},{<!!>},{<!!>}}',
                SCORE: 9},
            8: {TEXT: '{{<a!>},{<a!>},{<a!>},{<ab>}}',
                SCORE: 3}
        }

        self.garbages = {
            1: {TEXT: '<>'},
            2: {TEXT: '<random characters>'},
            3: {TEXT: '<<<<>'},
            4: {TEXT: '<{!>}>'},
            5: {TEXT: '<!!>'},
            6: {TEXT: '<!!!>>'},
            7: {TEXT: '<{o"i!a,<{i<a>'},
        }

    def test_garbage_cleanup(self):
        txt = self.inputs.get(5).get(TEXT)
        self.assertEqual('{,,,}', GarbageCleaner.cleanup_garbage(txt))
        txt = self.inputs.get(6).get(TEXT)
        self.assertEqual('{{},{},{},{}}', GarbageCleaner.cleanup_garbage(txt))
        txt = self.inputs.get(7).get(TEXT)
        self.assertEqual('{{},{},{},{}}', GarbageCleaner.cleanup_garbage(txt))
        txt = self.inputs.get(8).get(TEXT)
        self.assertEqual('{{}}', GarbageCleaner.cleanup_garbage(txt))

        for idx, d_garbage in self.garbages.items():
            text = d_garbage.get(TEXT)
            self.assertEqual('', GarbageCleaner.cleanup_garbage(text))
