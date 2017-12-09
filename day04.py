import common

log = common.get_logger(__name__)


def has_duplicates(s, delim=' '):
    # type: (str) -> bool
    tokens = s.split(delim)
    while len(tokens) > 0:
        head = tokens[0]
        tail = tokens[1:]
        if head in tail:
            return True
        tokens = tail
    return False

def is_valid(s):
    # type: (str) -> bool
    if not s:
        return False
    if has_duplicates(s):
        return False
    return True


def parse_input(intext):
    return intext.split('\n')


def main():
    passphrases = parse_input(common.read_input(4))
    answer_1 = 0
    idx = 1
    for p in passphrases:
        log.debug('Testing passphrase ({}/{})'.format(idx, len(passphrases)))
        idx += 1
        if not has_duplicates(p):
            answer_1 += 1
    print('The answer to part 1 is: {}'.format(answer_1))


if __name__ == '__main__':
    log = common.get_logger('day04', level='INFO')
    main()
