import itertools
import common

log = common.get_logger(__name__)


class Layer:
    def __init__(self, idepth=0, irange=-1):
        self._start_depth = 0
        self._end_depth = self._start_depth + 1
        self._range = irange
        self._scalar = 1  # switches from 1 to -1
        while idepth:
            self.move()
            idepth -= 1
        if irange == -1:
            self._start_depth = self._end_depth = -1  # this is a non-functional layer

    @property
    def start_depth(self):
        return self._start_depth

    @property
    def end_depth(self):
        return self._end_depth

    @property
    def range(self):
        return self._range

    def move(self, step_size=1):
        if self.range > 0:  # don't do any movement with range 0
            self._start_depth = self._end_depth
            if (self._start_depth == self.range - 1) or (self._start_depth == 0):
                self._scalar *= -1  # reverse direction of stepping
            end = self._end_depth + (step_size * self._scalar)
            self._end_depth = end

    def __repr__(self):
        return "<Layer start: {}, end: {}, range: {} />".format(self.start_depth, self.end_depth, self.range)


class Scanner:
    def __init__(self, layers, delay=0):
        # type: (list[Layer]) -> None
        self._layers = layers
        self._packet_pos = 0
        self._sec_value = 0
        self._steps = 0
        self._delay = delay
        if self.delay:
            for i in range(self.delay):
                self.step_layers()

    @property
    def delay(self):
        return self._delay

    @property
    def score(self):
        return self._sec_value

    def get_value(self, layer_idx):
        # type: (int) -> int
        layer = self._layers[layer_idx]  # type: Layer
        return layer.range * layer_idx

    def step_layers(self, step_size=1):
        for l in self._layers:  # type: Layer
            l.move(step_size=step_size)
        self._steps += 1

    def step(self, step_size=1):
        log.debug('Stepping size: {}...'.format(step_size))
        layer = self._layers[self._packet_pos]  # type: Layer
        if layer.start_depth == 0 and layer.range != 0:
            add_score = self.get_value(self._packet_pos)
            log.debug('Detected!!!! Layer: {}. Adding score: {}'.format(self._packet_pos, add_score))
            self._sec_value += add_score

        log.debug('Stepping layers...')
        self.step_layers(step_size=step_size)

        log.debug('Moving packet ahead...')
        self._packet_pos += step_size

    def run(self, short_circuit=False):
        for i in range(len(self._layers)):
            self.step()
            if short_circuit and self.score > 0:
                log.debug('Aborting delay {} at layer {}'.format(self._delay, self._packet_pos))
                break

    def __repr__(self):
        return "<Scanner packet_pos: {}, pos_layer: {} />".format(self._packet_pos, self._layers[self._packet_pos])


def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

def part_2_stolen():
    """ Straigh ganked from https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6bxce/ """
    lines = [line.split(': ') for line in common.read_input(13).split('\n')]

    heights = {int(pos): int(height) for pos, height in lines}

    part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)
    print('part1: {}'.format(part1))

    part2 = next(
        wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
    return part2

def parse_input(s_input):
    # type: (str) -> (list[Layer])
    tmp = {}
    out = []
    max_layer = -1
    for line in [l for l in s_input.split('\n') if l]:
        layer, irange = line.replace(' ', '').split(':')
        layer = int(layer)
        irange = int(irange)
        if layer > max_layer:
            max_layer = layer
        tmp[layer] = irange
    for i in range(max_layer + 1):
        irange = tmp.get(i, 0)
        layer = Layer(idepth=0, irange=irange)
        out.append(layer)
    return out


def main():
    intext = common.read_input(13)
    layers = parse_input(s_input=intext)
    s = Scanner(layers=layers)
    s.run()
    log.info('Starting part 1...')
    answer_1 = s.score
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    print('answer 2: {}'.format(part_2_stolen()))

    delay = 5500
    while False and delay < 10**4:
        # log.info('Trying delay: {}'.format(delay))
        layers = parse_input(s_input=intext)
        if delay % 2 == 1:
            delay += 1
            continue  # only even delays allow layer 1 to pass
        s = Scanner(layers=layers, delay=delay)
        s.run(short_circuit=True)
        if s.score == 0:
            break
        if delay % 500 == 0:
            log.info('Delay: {}'.format(delay))
        log.debug('Delay: {}, Score: {}'.format(delay, s.score))
        delay += 1
    answer_2 = delay
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day13', level='INFO')
    main()
