import common
from collections import namedtuple

log = common.get_logger(__name__)


Bank = namedtuple('Bank', 'blocks')


class Distributor:
    def __init__(self, banks):
        self.banks = banks
        self.index = 0
        self.memory = []

    def seek_next_index(self):
        maxval = max(self.banks)
        log.debug('Max value in banks is: {}'.format(maxval))
        indexes = []
        for i in range(len(self.banks)):
            if self.banks[i] == maxval:
                indexes.append(i)
        log.debug('Max value was found at indexes: {}'.format(indexes))
        self.index = min(indexes)
        log.debug('Choosing index {} with value {}'.format(self.index, self.banks[self.index]))

    def proc(self):
        while self.banks not in self.memory:
            self.seek_next_index()
            boxes = self.banks[self.index]
            self.banks[self.index] = 0
            while boxes:
                self.index = (self.index + 1) % len(self.banks)
                self.banks[self.index] += 1
                boxes -= 1
            self.memory.append(self.banks.copy)


def init_banks():
    # type: () -> list
    return parse_input(common.read_input(6))


def parse_input(intext):
    return [int(n) for n in intext.split('\t')]


def main():
    banks = init_banks()
    d = Distributor(banks=banks)
    d.proc()

    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day06', level='INFO')
    main()
