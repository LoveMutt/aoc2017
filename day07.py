import common

log = common.get_logger(__name__)


class Tower:
    def __init__(self, name='', weight=0, children=list()):
        # type: (str, int, list[Tower]) -> None
        self.weight = weight
        self.name = name
        self.children = children



def parse_input(intext):
    return [line for line in intext.split('\n') if line]


def main():
    lines = parse_input(common.read_input(7))

    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day07', level='INFO')
    main()
