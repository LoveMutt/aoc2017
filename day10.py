import common

log = common.get_logger(__name__)


def init_elements():
    # type: () -> list[int]
    return list(range(256))


def reverse_slice(in_l, start_index, num):
    # type: (list[int], int, int) -> list[int]
    if num < 2:
        return in_l
    sub_l = []
    for i in range(num):
        idx = (start_index + i) % len(in_l)
        sub_l.append(in_l[idx])
    sub_l.reverse()
    l_copy = in_l.copy()
    for i in range(num):
        idx = (start_index + i) % len(l_copy)
        l_copy[idx] = sub_l[i]
    return l_copy


def hash(l_lengths, l_numbers):
    # type: (list[int]) -> int
    # init
    skip = 0
    pos = 0

    for l in l_lengths:
        # ignore if longer than input list
        if l > len(l_numbers):
            log.debug('Ignoring length {}'.format(l))
            continue
        # step 1: reverse the order of a slice
        l_new = reverse_slice(l_numbers, start_index=pos, num=l)
        l_numbers = l_new
        # step 2: Move the current position forward by that length plus the skip size
        pos = (pos + l + skip) % len(l_numbers)
        # step 3: increase step size by 1
        skip += 1
    log.info('first two values are {}, {}'.format(l_numbers[0], l_numbers[1]))
    return l_numbers[0] * l_numbers[1]  # what is the result of multiplying the first two numbers in the list


def main():
    intext = common.read_input(10)
    log.info('Initializing lists...')
    l_lengths = [int(n.strip()) for n in intext.split(',')]
    l_numbers = init_elements()
    log.info('Starting hash for part 1...')
    answer_1 = hash(l_lengths, l_numbers)
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
