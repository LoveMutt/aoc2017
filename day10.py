import common

log = common.get_logger(__name__)


def _init_elements():
    return list(range(256))


def reverse_sublist(in_l, start_index, num):
    sub_l = []
    for i in range(num):
        idx = (start_index + i) % len(in_l)
        sub_l.append(in_l[idx])
    sub_l.reverse()
    for i in range(num):
        idx = (start_index + i) % len(in_l)
        in_l[idx] = sub_l[i]
    return in_l


def main():
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
