import common

log = common.get_logger(__name__)


class GarbageCleaner:
    GARBAGE_START = '<'
    GARBAGE_END = '>'
    NEGATOR = '!'

    def __init__(self):
        pass

    @classmethod
    def cleanup_garbage(cls, intext):
        # type: (str) -> str
        txt_ptr = 0
        clean_str = ''
        in_garbage = False
        while txt_ptr < len(intext):  # starting reading all input
            if in_garbage:
                if intext[txt_ptr] == cls.NEGATOR:
                    log.debug('Skipping {} and {} (index: {})'.format(intext[txt_ptr],
                                                                      intext[txt_ptr + 1],
                                                                      txt_ptr))
                    txt_ptr += 1
                elif intext[txt_ptr] == cls.GARBAGE_END:
                    in_garbage = False
            else:
                if intext[txt_ptr] == cls.GARBAGE_START:
                    log.debug('Found start of garbage at character index: {}'.format(txt_ptr))
                    in_garbage = True
                else:
                    clean_str += intext[txt_ptr]
            txt_ptr += 1
        return clean_str


def main():
    text = common.read_input(9)
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
