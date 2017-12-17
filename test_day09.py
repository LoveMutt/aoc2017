import unittest

from day08 import *
from common import get_logger

log = get_logger(__name__)

TEXT = 'text'
SCORE = 'score'


class TestDay(unittest.TestCase):
    def setUp(self):
        inputs = {
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

    