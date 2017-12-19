import unittest

from day10 import *
from common import get_logger

log = get_logger(__name__)


def get_test_inputs():
    return [3, 4, 1, 5]


def init_test_elements():
    return list(range(5))


class TestDay(unittest.TestCase):
    def setUp(self):
        self.elements = init_test_elements()
        self.inputs = get_test_inputs()

    def test_reverse_sublist(self):
        reverse_sublist(init_elements(), 0, 2)
