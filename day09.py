import common

log = common.get_logger(__name__)


def parse_input():
    text = parse_input(common.read_input(9))


def main():
    text = parse_input()
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
