import unittest

from day07 import *
from common import get_logger

log = get_logger(__name__)

def get_test_input():
    s = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    return s


class TestDay(unittest.TestCase):
    def test_parse_input(self):
        for line in parse_input(get_test_input()):
            parts = line.split(' ')
            self.assertGreater(len(parts), 1)

    def test_tower_from_input(self):
        lines = parse_input(get_test_input())
        good_1 = lines[0]
        good_2 = lines[1]
        good_3 = lines[5]
        t = tower_from_input(good_1)
        self.assertEqual(t.name, 'pbga')
        self.assertEqual(t.weight, 66)
        t = tower_from_input(good_2)
        self.assertEqual(t.name, 'xhth')
        self.assertEqual(t.weight, 57)
        t = tower_from_input(good_3)
        self.assertEqual(t.name, 'fwft')
        self.assertEqual(t.weight, 72)

    def test_add_children_from_input(self):
        lines = parse_input(get_test_input())
        lines = [lines[1], lines[4], lines[5], lines[-1]]

        towers = [tower_from_input(l) for l in lines]
        t_parent = get_tower_by_name('fwft', towers)
        towers = add_children_from_input(lines=lines, towers=towers)
        self.assertEqual(len(t_parent.children), 3)
        for child in t_parent.children:
            self.assertIsInstance(child, Tower)
            self.assertIn(child, towers)


    def test_create_towers_from_input(self):
        lines = parse_input(get_test_input())
        towers = create_towers_from_input(lines)
        for t in towers:
            self.assertIsInstance(t, Tower)
            self.assertTrue(t.name)
            self.assertTrue(t.weight)
            self.assertIsInstance(t.children, list)
            for t_child in t.children:
                self.assertIn(t_child, towers)
