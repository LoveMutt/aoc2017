import unittest

from day08 import *
from common import get_logger

log = get_logger(__name__)


def get_test_input():
    return """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


class TestDay(unittest.TestCase):
    def setUp(self):
        self.ra = Register(id='a')
        self.rb = Register(id='b')
        self.registers = RegisterCollection(registers=[self.ra, self.rb])

    def test_test_conditon(self):
        self.ra.value = 5
        cond = 'a == 5'
        self.assertTrue(self.registers.test_condition(cond))
        cond = 'a == 4'
        self.assertFalse(self.registers.test_condition(cond))

    def test_reg_inst(self):
        self.ra.exec_inst('inc 5')
        self.assertEqual(5, self.ra.value)
        self.ra.exec_inst('dec 4')
        self.assertEqual(1, self.ra.value)

    def test_get_register_by_id(self):
        id = 'a'
        self.assertEqual(self.ra, self.registers.get_register_by_id(id))
        id = 'b'
        self.assertEqual(self.rb, self.registers.get_register_by_id(id))

    def test_exec_instruction(self):
        self.assertEqual(0, self.registers.get_register_by_id('a'))
        inst = 'a inc 1 if a == 0'
        self.assertEqual(0, self.registers.get_register_by_id('a'))
        self.registers.exec_instruction(inst)
        self.assertEqual(1, self.registers.get_register_by_id('a'))

    def test_init_collection(self):
        rc = init_collection_from_input(get_test_input())
        self.assertEqual(3, len(rc.registers))
        self.assertTrue('a' in rc.ids)
        self.assertTrue('b' in rc.ids)
        self.assertTrue('c' in rc.ids)
