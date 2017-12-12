import common

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

    @property
    def total_weight(self):
        total = self.weight
        for child in self.children:
            total += child.total_weight
        return total

    @property
    def balanced(self):
        for t_test, t_rest in split_head(self.children):
            if not t_test.total_weight in [t.total_weight for t in t_rest]:
                return False
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
        return "<Tower name='{}', weight={}, children={}, parent={} />".format(self.name,
                                                                               self.weight,
                                                                               self.children,
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


def get_subtower_weights(tower):
    weights = [tower.weight]
    for i in range(len(tower.children)):
        weights.append(get_subtower_weight(tower.children[i]))
    return weights


def get_subtower_weight(tower):
    # type: (Tower) -> int
    return sum(get_subtower_weights(tower))


def find_leafs(towers):
    # type: (list[Tower]) -> set[Tower]
    return set([t for t in towers if t.parent and not t.children])


def get_off_weight_tower(towers):
    # type: (list[Tower]) -> tuple
    bad = list()
    good = list()


def find_anomaly(towers):
    # type: (list[Tower]) -> Tower
    sub_weights = []
    # depth-first traversal to find unbalanced disc
    unbalanced_tower = None
    for leaf in find_leafs(towers=towers):
        while leaf.parent:
            leaf = leaf.parent
            if not leaf.balanced:
                unbalanced_tower = leaf
                break
        if unbalanced_tower is None:
            break
    log.debug('Found unbalanced tower: {}'.format(unbalanced_tower.name))
    ub_children = unbalanced_tower.children
    log.debug('Testing weights of unbalanced tower\'s children')
    if ub_children[0] == ub_children[1] or ub_children[0] == ub_children[2]:
        if ub_children[0] == ub_children[1]:
            log.debug('{} weighs the same as {}, so {} is anomalous'.format(ub_children[0].name,
                                                                            ub_children[1].name,
                                                                            ub_children[2].name))
            return ub_children[2]
        log.debug('{} weighs the same as {}, so {} is anomalous'.format(ub_children[0].name,
                                                                        ub_children[2].name,
                                                                        ub_children[1].name))
        return ub_children[1]
    log.debug('{} does not weight the same as {} or {}'.format(ub_children[0].name,
                                                               ub_children[2].name,
                                                               ub_children[1].name))
    return ub_children[0]


def main():
    lines = parse_input(common.read_input(7))
    towers = create_towers_from_input(lines)
    t_base = get_base_tower(towers)
    answer_1 = t_base.name
    print('The answer to part 1 is: {}'.format(answer_1))
    unbalanced_tower = find_anomaly(towers)
    good_children = [t for t in unbalanced_tower.parent.children if t is not unbalanced_tower]
    weight_diff = good_children[0].weight - unbalanced_tower.weight
    new_weight = unbalanced_tower.weight + weight_diff
    answer_2 = new_weight
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day07', level='INFO')
    main()
