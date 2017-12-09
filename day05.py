import common
import timeit

log = common.get_logger(__name__)


class JmpSet:
    def __init__(self, jmps):
        self.cur_idx = 0
        self.jmps = jmps
        self.steps = 0

    @property
    def __len__(self):
        return len(self.jmps)

    def proc2(self):
        self.proc(part2=True)

    def proc(self, part2=False):
        while self.cur_idx < len(self.jmps) and self.cur_idx >= 0:
            jmp = self.jmps[self.cur_idx]
            tmp_idx = self.cur_idx
            self.cur_idx += jmp
            # part2 says, if offset is 3+, decrement by 1
            if not part2 or jmp < 3:
                self.jmps[tmp_idx] += 1
            elif part2:
                self.jmps[tmp_idx] -= 1
            self.steps += 1


def parse_input(intext):
    return [int(c) for c in intext.split('\n') if c]


def main():
    jmps = parse_input(common.read_input(5))
    js = JmpSet(jmps=jmps.copy())
    t1 = timeit.timeit(js.proc)
    answer_1 = js.steps
    print('The answer to part 1 is: {} (took {} seconds)'.format(answer_1, t1))
    js = JmpSet(jmps=jmps.copy())
    t2 = timeit.timeit(js.proc2)
    answer_2 = js.steps
    print('The answer to part 2 is: {} (took {} seconds)'.format(answer_2, t2))


if __name__ == '__main__':
    log = common.get_logger('day05', level='INFO')
    main()
