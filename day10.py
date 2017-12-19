import common

log = common.get_logger(__name__)


def init_elements():
    # type: () -> list[int]
    return list(range(256))


def reverse_slice(in_l, start_index, num):
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


def hash(len_l, num_l):
    # type: (list[int]) -> int
    # init
    skip = 0
    pos = 0

    for i in range(len(len_l)):
        l = len_l[i]
        # ignore if longer than input list
        if l > len(len_l):
            log.debug('Ignoring index {} ({})'.format(i, len_l[i]))
            continue
        # step 1: reverse the order of a slice
        num_l = reverse_slice(num_l, start_index=pos, num=l)
        # step 2: advance
        pos = get_new_pos(in_l=num_l, lengths_l=len_l, idx=pos, skip=skip)
        # step 3: increase step size by 1
        skip += 1
    return len_l[0] * len_l[1]


def main():
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
