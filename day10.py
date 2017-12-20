import binascii
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


def hash(l_lengths, l_numbers, skip=0, pos=0):
    # type: (list[int]) -> (int, int, int)
    # init
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
    return l_numbers[0] * l_numbers[1], skip, pos  # what is the result of multiplying the first two numbers in the list


def hash_n(l_lengths, l_numbers, skip=0, pos=0, n=64):
    # type: (list[int], list[int], int, int) -> (int, int, int)
    hash_val = -1
    for i in range(n):
        hash_val, skip, pos = hash(l_lengths=l_lengths.copy(), l_numbers=l_numbers.copy(), skip=skip, pos=pos)
    return hash_val, skip, pos


def dense_hash(l_numbers):
    # type: (list[int]) -> list[int]
    MAGIC = 16
    l_dense_hash = []
    for i in range(int(len(l_numbers) / MAGIC)):
        start = i * MAGIC
        val = 0
        for j in range(MAGIC):
            idx = start + j
            val ^= l_numbers[idx]
        l_dense_hash.append(val)
    return l_dense_hash


def hexlify_dense_hash(l_dh):
    # type: (list[int]) -> str
    out = ''
    for n in l_dh:
        out += '{0:02x}'.format(n)  # from https://stackoverflow.com/a/10218221/761829
    return out


def convert_to_ord(c):
    if not isinstance(c, str):
        c = str(c)
    return ord(c)


def convert_list_to_ascii(s):
    # type: (str) -> list[int]
    l_code = []
    for c in s:
        l_code.append(convert_to_ord(c))
    return l_code


def get_ascii_sequence(intext):
    l_inputs = convert_list_to_ascii(intext)
    l_inputs.extend([17, 31, 73, 47, 23])


def main():
    intext = common.read_input(10)
    log.info('Initializing lists...')
    l_lengths = [int(n.strip()) for n in intext.split(',')]
    l_numbers = init_elements()
    log.info('Starting hash for part 1...')
    answer_1, _, _ = hash(l_lengths, l_numbers)
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
