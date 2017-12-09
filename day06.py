import common
from collections import namedtuple

log = common.get_logger(__name__)


Bank = namedtuple('Bank', 'blocks')


def set_banks(inlist):
    # type: (list) -> list
    pass


def distrib(banks):
    # type: (list[Bank]) -> None
    for b in banks:
        pass

def parse_input(intext):
    return [int(c) for c in intext.split('\n') if c]


def main():
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day06', level='INFO')
    main()
