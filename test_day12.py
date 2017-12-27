import unittest

from day12 import *
from common import get_logger

log = get_logger(__name__)


T_STR = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''


class TestDay(unittest.TestCase):
    def test_program_generator(self):
        pid_relations = parse_input(T_STR)
        programs = program_generator(pid_relations)
        self.assertIsInstance(programs[0], set)
        self.assertSetEqual({2}, programs[0])
        self.assertIsInstance(programs[2], set)
        self.assertIn(0, programs[2])

    def test_knows(self):
        progs = program_generator(parse_input(T_STR))
        self.assertTrue(knows(progs, 2, 0))
        self.assertTrue(knows(progs, 0, 2))
        self.assertFalse(knows(progs, 1, 2))
        self.assertTrue(knows(progs, 0, 4))

    def test_count(self):
        progs = program_generator(parse_input(T_STR))
        self.assertEqual(6, count_linking_to(progs, 0))
