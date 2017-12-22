import binascii
import common

log = common.get_logger(__name__)


def main():
    intext = common.read_input(11)
    log.info('Starting part 1...')
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day11', level='INFO')
    main()
