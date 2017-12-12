import unittest

from day08 import *
from common import get_logger

log = get_logger(__name__)


class TestDay(unittest.TestCase):
    def setUp(self):
        self.ra = Register(id='a', value=5)
        self.rb = Register(id='b', value=3)
        self.registers = RegisterCollection(registers=[self.ra, self.rb])

    def test_test_conditon(self):
        cond = 'a == 5'
        self.assertTrue(self.registers.test_condition(cond))
        cond = 'a == 4'
        self.assertFalse(self.registers.test_condition(cond))
