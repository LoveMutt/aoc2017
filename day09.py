import common

log = common.get_logger(__name__)


class Group:
    def __init__(self):
        self.parent = None

    @property
    def score(self):
        p_score = 0
        if self.parent is not None:
            p_score = self.parent.score
        return p_score + 1


class StrParser:
    GARBAGE_START = '<'
    GARBAGE_END = '>'
    GROUP_START = '{'
    GROUP_END = '}'
    NEGATOR = '!'

    def __init__(self):
        self.groups = []

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

    @classmethod
    def build_groups(cls, intext):
        # type: (str) -> list[int]
        txt_ptr = 0
        grp_ptr = -1
        groups = []
        while txt_ptr < len(intext):
            if intext[txt_ptr] == cls.GROUP_START:
                grp_ptr += 1
                if len(groups) <= grp_ptr:
                    groups.append(1)
                else:
                    groups[grp_ptr] += 1
            elif intext[txt_ptr] == cls.GROUP_END:
                grp_ptr -= 1
            else:
                # just skip because we're inside a group
                pass
            txt_ptr += 1
        return groups

    @classmethod
    def count_group_score(cls, groups):
        # type: (list[int]) -> int
        score = 0
        for i in range(len(groups)):
            multiplier = i + 1
            score += multiplier * groups[i]
        return score


def main():
    text = common.read_input(9)
    groups = StrParser.build_groups(text)
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day09', level='INFO')
    main()
