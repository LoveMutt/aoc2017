import common

log = common.get_logger(__name__)


def split_head(inlist):
    while len(inlist) > 1:
        head = inlist[0]
        tail = inlist[1:]
        yield head, tail
        inlist = tail


def has_duplicates(s, delim=' '):
    # type: (str) -> bool
    tokens = s.split(delim)
    for head, tail in split_head(tokens):
        if head in tail:
            return True
    return False


def is_anagram(s1, s2):
    l1 = list(s1)
    l1 = sorted(l1)
    l2 = list(s2)
    l2 = sorted(l2)
    return l1 == l2


def has_anagrams(s):
    tokens = s.split(' ')
    for head, tail in split_head(tokens):
        for t in tail:
            if is_anagram(head, t):
                return True
    return False


def is_valid(s):
    # type: (str) -> bool
    if not s:
        return False
    if has_duplicates(s):
        return False
    if has_anagrams(s):
        return False
    return True


def parse_input(intext):
    return intext.split('\n')


def main():
    passphrases = parse_input(common.read_input(4))
    answer_1 = 0
    answer_2 = 0
    idx = 1
    for p in passphrases:
        log.debug('Testing passphrase ({}/{})'.format(idx, len(passphrases)))
        idx += 1
        if not has_duplicates(p):
            answer_1 += 1
        if not has_anagrams(p):
            answer_2 += 1
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day04', level='INFO')
    main()
