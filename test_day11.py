import unittest

from day11 import *
from common import get_logger

log = get_logger(__name__)


def get_test_lengths():
    return [3, 4, 1, 5]


def get_test_inputs():
    return [0, 1, 2, 3, 4]


class TestDay(unittest.TestCase):
    def setUp(self):
        pass
