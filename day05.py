import common

log = common.get_logger(__name__)


class JmpSet:
    def __init__(self, jmps):
        self.cur_idx = 0
        self.jmps = jmps
        self.steps = 0

    @property
    def __len__(self):
        return len(self.jmps)

    def proc(self):
        while self.cur_idx < len(self.jmps) and self.cur_idx >= 0:
            jmp = self.jmps[self.cur_idx]
            tmp_idx = self.cur_idx
            self.cur_idx += jmp
            self.jmps[tmp_idx] += 1
            self.steps += 1


def parse_input(intext):
    return [int(c) for c in intext.split('\n') if c]


def main():
    jmps = parse_input(common.read_input(5))
    js = JmpSet(jmps=jmps)
    js.proc()
    answer_1 = js.steps
    answer_2 = 'Not Known'
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day05', level='INFO')
    main()
