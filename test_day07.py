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


def get_test_towers():
    lines = parse_input(get_test_input())
    towers = create_towers_from_input(lines)
    return towers


def get_towers_with_parents(towers):
    # type: (list[Tower]) -> list[Tower]
    return [t for t in towers if t.parent]


def get_towers_with_children(towers):
    # type: (list[Tower]) -> list[Tower]
    return [t for t in towers if t.children]


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
            self.assertEqual(child.parent, t_parent)

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

        towers_with_parents = get_towers_with_parents(towers)
        towers_with_children = get_towers_with_children(towers)
        self.assertEqual(4, len(towers_with_children))
        self.assertEqual(12, len(towers_with_parents))

    def test_get_base_tower(self):
        lines = parse_input(get_test_input())
        towers = create_towers_from_input(lines)
        t_base = get_base_tower(towers)
        self.assertEqual(t_base.name, 'tknk')

    def test_get_subtower_weight(self):
        lines = parse_input(get_test_input())
        towers = create_towers_from_input(lines)
        t_base = get_base_tower(towers)
        actual_weights = []
        for i in range(len(t_base.children)):
            actual_weights.append(get_subtower_weight(t_base.children[i]))
        self.assertListEqual([251, 243, 243], actual_weights)
