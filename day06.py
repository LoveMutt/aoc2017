import common
from collections import namedtuple

log = common.get_logger(__name__)


Bank = namedtuple('Bank', 'blocks')


class Distributor:
    def __init__(self, banks):
        self.banks = banks
        self.index = 0
        self.memory = []
        self.steps = 0
        self.occurences = 0
        self.registers = []

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
        while len(self.registers) < 2:
            while self.banks not in self.memory:
                self.memory.append(self.banks.copy())
                self.steps += 1
                log.debug('Step {:04}'.format(self.steps))
                self.seek_next_index()
                boxes = self.banks[self.index]
                log.debug('Storing value {} for distribution'.format(boxes))
                log.debug('Clearing index {}'.format(self.index))
                log.debug('Banks before distribution: {}'.format(self.banks))
                self.banks[self.index] = 0
                while boxes:
                    self.index = (self.index + 1) % len(self.banks)
                    self.banks[self.index] += 1
                    boxes -= 1
                log.debug('Banks after distribution: {}'.format(self.banks))
            self.registers.append(self.steps)
            log.debug('Registering {} at step {}'.format(self.banks, self.steps))
            self.memory = []  # clear memory to build again


def init_banks():
    # type: () -> list
    return parse_input(common.read_input(6))


def parse_input(intext):
    return [int(n) for n in intext.split('\t')]


def main():
    banks = init_banks()
    d = Distributor(banks=banks)
    d.proc()

    answer_1 = d.registers[0]
    print('The answer to part 1 is: {}'.format(answer_1))
    answer_2 = d.registers[1] - d.registers[0]
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day06', level='INFO')
    main()
