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
        pid_relations, num_relations = parse_input(T_STR)
        graph = graph_generator(pid_relations, num_relations)
        self.assertIsInstance(graph, SparseGraph)
        self.assertEqual(len(links_to(graph, 0)), 6)

    def test_knows(self):
        pid_relations, num_relations = parse_input(T_STR)
        graph = graph_generator(pid_relations, num_relations)
        self.assertTrue(knows(graph, 2, 0))
        self.assertTrue(knows(graph, 0, 2))
        self.assertFalse(knows(graph, 1, 2))
        self.assertTrue(knows(graph, 0, 4))
