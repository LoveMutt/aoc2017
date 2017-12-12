import common

log = common.get_logger(__name__)


def parse_input(intext):
    return intext.split('\n')


def main():
    answer_1 = 'Unknown'
    answer_2 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day08', level='INFO')
    main()
