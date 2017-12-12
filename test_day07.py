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
        towers = create_towers_from_text(get_test_input())
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
        towers = create_towers_from_text(get_test_input())
        t_base = get_base_tower(towers)
        self.assertEqual(t_base.name, 'tknk')

    def test_total_weight(self):
        towers = create_towers_from_text(get_test_input())
        t_ugml = get_tower_by_name('ugml', towers)
        t_padx = get_tower_by_name('padx', towers)
        t_fwft = get_tower_by_name('fwft', towers)
        self.assertEqual(251, t_ugml.total_weight)
        self.assertEqual(243, t_padx.total_weight)
        self.assertEqual(243, t_fwft.total_weight)

    def test_balanced(self):
        towers = create_towers_from_text(get_test_input())
        t_ugml = get_tower_by_name('ugml', towers)
        t_padx = get_tower_by_name('padx', towers)
        t_fwft = get_tower_by_name('fwft', towers)
        self.assertTrue(t_ugml.balanced)
        self.assertTrue(t_padx.balanced)
        self.assertTrue(t_fwft.balanced)
        t_base = get_base_tower(towers)
        self.assertFalse(t_base.balanced)

    def test_find_leafs(self):
        towers = create_towers_from_text(get_test_input())
        expected_leafs = set([t for t in towers if t.parent and not t.children])
        self.assertSetEqual(expected_leafs, find_leafs(towers))

    def test_find_anomaly(self):
        towers = create_towers_from_text(get_test_input())
        bad_tower = get_tower_by_name('ugml', towers)
        self.assertEqual(bad_tower, find_anomaly(towers))

    def test_get_weight_correction(self):
        towers = create_towers_from_text(get_test_input())
        bad_tower = find_anomaly(towers)
        weight_corr = get_weight_correction(bad_tower)
        self.assertEqual(-8, weight_corr)
        self.assertEqual(60, bad_tower.weight + weight_corr)

    def test_ancestors(self):
        towers = create_towers_from_text(get_test_input())
        t_1 = get_tower_by_name('gyxo', towers)
        t_2 = get_tower_by_name('ugml', towers)
        t_3 = get_tower_by_name('tknk', towers)
        self.assertListEqual([t_2, t_3], t_1.ancestors)
        self.assertListEqual([t_3], t_2.ancestors)

    def test_descendants(self):
        towers = create_towers_from_text(get_test_input())
        t_1 = get_tower_by_name('tknk', towers)
        t_2 = get_tower_by_name('ugml', towers)
        t_3 = get_tower_by_name('gyxo', towers)
        t_4 = get_tower_by_name('ebii', towers)
        t_5 = get_tower_by_name('jptl', towers)
        self.assertListEqual([t_3, t_4, t_5], t_2.descendants)
        self.assertSetEqual(set(get_towers_except(t_1, towers)), set(t_1.descendants))
        self.assertListEqual([], t_3.descendants)

    def test_verify(self):
        towers = create_towers_from_text(get_test_input())
        bad_tower = find_anomaly(towers)
        self.assertTrue(verify_wrong_weight(bad_tower=bad_tower, towers=towers))
