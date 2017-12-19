import common

log = common.get_logger(__name__)


def init_elements():
    # type: () -> list[int]
    return list(range(256))


def reverse_sublist(in_l, start_index, num):
    # type: (list[int], int, int) -> list[int]
    sub_l = []
    for i in range(num):
        idx = (start_index + i) % len(in_l)
        sub_l.append(in_l[idx])
    sub_l.reverse()
    for i in range(num):
        idx = (start_index + i) % len(in_l)
        in_l[idx] = sub_l[i]
    return in_l


def get_new_pos(in_l, lengths_l, idx, skip):
    # type: (list[int], list[int], int, int) -> int
    length = lengths_l[idx]
    target_idx = (length + skip) % len(in_l)
    return target_idx


def main():
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
