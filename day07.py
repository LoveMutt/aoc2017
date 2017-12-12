import common
import sys

log = common.get_logger(__name__)


class Tower:
    def __init__(self, name='', weight=0, children=None, parent=None):
        # type: (str, int, list[Tower]) -> None
        self.weight = weight
        if isinstance(self.weight, str):
            self.weight = int(self.weight)
        self.name = name
        self.children = children
        if self.children is None:
            self.children = []
        self.parent = parent
        self._ancestors = None
        self._descendants = None
        self._total_weight = 0

    @property
    def total_weight(self):
        if self._total_weight:
            return self._total_weight
        total = self.weight
        for child in self.children:
            total += child.total_weight
        self._total_weight = total
        return self._total_weight

    @property
    def balanced(self):
        # select one child
        if self.children:
            child = self.children[0]
            return [child.total_weight] * len(self.children) == [c.total_weight for c in self.children]
        return True

    @property
    def ancestors(self):
        if self._ancestors:
            return self._ancestors
        ancestors = []
        t_parent = self.parent
        while t_parent is not None:
            ancestors.append(t_parent)
            t_parent = t_parent.parent
        self._ancestors = ancestors
        return self._ancestors

    @property
    def descendants(self):
        if self._descendants:
            return self._descendants
        descendants = []
        t_child = self
        for t_child in t_child.children:
            descendants.append(t_child)
            descendants.extend(t_child.descendants)
        self._descendants = descendants
        return self._descendants


    def __repr__(self):
        return "<Tower name='{}', weight={}, total_weight={}, children={}, parent={} />".format(self.name,
                                                                                                self.weight,
                                                                                                self.total_weight,
                                                                                                len(self.children),
                                                                                                self.parent,
                                                                                                )

def parse_input(intext):
    return [line for line in intext.split('\n') if line]


def get_towers_except(t, towers):
    # type: (Tower, list[Tower]) -> list[Tower]
    return [tw for tw in towers if tw is not t]


def create_towers_from_text(intext):
    lines = parse_input(intext=intext)
    return create_towers_from_input(lines)


def tower_from_input(s):
    # type: (str) -> Tower
    s = s.strip()
    parts = s.split(' ')  # type: str, str
    name = parts[0]
    weight = parts[1]
    # cleanup weight
    weight = weight.replace(')', '').replace('(', '')
    weight = int(weight)
    t = Tower(name=name, weight=weight)
    return t


def get_tower_name(s):
    parts = s.split(' ')
    name = parts[0].strip()
    return name


def split_head(inlist):
    while len(inlist) > 1:
        head = inlist[0]
        tail = inlist[1:]
        yield head, tail
        inlist = tail


def get_tower_by_name(name, towers):
    # type: (str, list[Tower]) -> Tower
    name = get_tower_name(name)
    return [t for t in towers if t.name == name][0]  # type: Tower


DELIM = ' -> '
def create_towers_from_input(lines):
    # type: (list[str]) -> list[Tower]
    # first, create all towers with no children
    towers = []
    for line in lines:
        t = tower_from_input(line)
        towers.append(t)
    towers = add_children_from_input(lines, towers)
    return towers


def add_children_from_input(lines, towers):
    # type: (list) -> list
    for line in [l for l in lines if DELIM in l]:
        tower_info, stack_info = line.split(DELIM)
        t_parent = get_tower_by_name(tower_info, towers)
        children = [c.strip() for c in stack_info.split(',')]
        for s_child in children:
            t_child = get_tower_by_name(s_child, towers)
            t_child.parent = t_parent
            t_parent.children.append(t_child)
    return towers


def get_base_tower(towers):
    # type: (list[Tower]) -> Tower
    for t in towers:  # type: Tower
        if t.parent is None:
            return t
    return None


def find_leafs(towers):
    # type: (list[Tower]) -> set[Tower]
    return set([t for t in towers if t.parent and not t.children])


def find_anomaly(towers):
    # type: (list[Tower]) -> Tower
    # depth-first traversal to find unbalanced disc
    unbalanced_tower = None
    for leaf in find_leafs(towers=towers):
        log.debug('Working from leaves to base to find unbalanced tower')
        while leaf.parent:
            t_parent = leaf.parent
            if not t_parent.balanced:
                log.info('Found unbalanced tower at {}'.format(t_parent))
                unbalanced_tower = t_parent
                break
            leaf = t_parent
        if unbalanced_tower is None:
            break
    log.debug('Found unbalanced tower: {}'.format(unbalanced_tower.name))
    log.debug('Testing weights of unbalanced tower\'s children')
    log.info('finding any unbalanced children of the current tower')
    ub_children = [c for c in unbalanced_tower.children if not c.balanced]
    ub_child = unbalanced_tower
    while ub_children:
        assert len(ub_children) == 1
        ub_child = ub_children[0]
        ub_children = [c for c in ub_child.children if not c.balanced]
    log.info('Found top-most unbalanced tower: {}'.format(ub_child))
    ub_children = ub_child.children
    if ub_children[0] == ub_children[1] or ub_children[0] == ub_children[2]:
        if ub_children[0] == ub_children[1]:
            log.debug('{} weighs the same as {}, so {} is anomalous'.format(ub_children[0].name,
                                                                            ub_children[1].name,
                                                                            ub_children[2].name))
            anomaly = ub_children[2]
        else:
            log.debug('{} weighs the same as {}, so {} is anomalous'.format(ub_children[0].name,
                                                                            ub_children[2].name,
                                                                            ub_children[1].name))
            anomaly = ub_children[1]
    else:
        log.debug('{} does not weight the same as {} or {}'.format(ub_children[0].name,
                                                                   ub_children[2].name,
                                                                   ub_children[1].name))

        anomaly = ub_children[0]
    return anomaly

def get_weight_correction(tower):
    # type: (Tower) -> int
    t_parent = tower.parent
    equal_children = [t for t in t_parent.children if t != tower]  # type: list(Tower)
    return equal_children[0].total_weight - tower.total_weight


def verify_wrong_weight(bad_tower, towers):
    # type: (Tower, list[Tower]) -> bool
    most_towers = [t for t in towers if t is not bad_tower and t not in bad_tower.ancestors]
    for t in most_towers:
        if t.children:
            test_weight = t.children[0].total_weight
            if not [test_weight] * len(t.children) == [c.total_weight for c in t.children]:
                return False
    return True


def main():
    lines = parse_input(common.read_input(7))
    towers = create_towers_from_input(lines)
    t_base = get_base_tower(towers)
    answer_1 = t_base.name
    print('The answer to part 1 is: {}'.format(answer_1))
    unbalanced_tower = find_anomaly(towers)
    weight_corr = get_weight_correction(unbalanced_tower)
    new_weight = unbalanced_tower.weight + weight_corr
    if not verify_wrong_weight(unbalanced_tower, towers):
        log.error('The bad tower was not correct')
        sys.exit(1)
    answer_2 = new_weight
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day07', level='INFO')
    main()
