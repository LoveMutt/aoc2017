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

    def __repr__(self):
        return "<Tower name='{}', weight={}, children={} />".format(self.name, self.weight, self.children)

def parse_input(intext):
    return [line for line in intext.split('\n') if line]


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

    return towers


def add_children_from_input(lines, towers):
    # type: (list) -> list
    for line in [l for l in lines if DELIM in l]:
        tower_info, stack_info = line.split(DELIM)
        t_parent = get_tower_by_name(tower_info, towers)
        children = [c.strip() for c in stack_info.split(',')]
        for s_child in children:
            t_child = get_tower_by_name(s_child, towers)
            t_parent.children.append(t_child)
    return towers


def main():
    lines = parse_input(common.read_input(7))

    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day07', level='INFO')
    main()
