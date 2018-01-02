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
        self._start_depth = self._end_depth
        if (self._start_depth == self._range - 1) or (self._start_depth == 0):
            self._scalar *= -1  # reverse direction of stepping
        end = self._end_depth + (step_size * self._scalar)
        self._end_depth = end

    def __repr__(self):
        return "<Layer start: {}, end: {}, range: {} />".format(self.start_depth, self.end_depth, self.range)


class Scanner:
    def __init__(self, layers):
        # type: (list[(int, int)]) -> None
        self._layers = []
        for idepth, irange in layers:
            layer = Layer(idepth=idepth, irange=irange)
            self._layers.append(layer)

        self._packet_pos = 0
        self._sec_value = 0

    @property
    def score(self):
        return self._sec_value

    def get_value(self, layer_idx):
        # type: (int) -> int
        layer = self._layers[layer_idx]  # type: Layer
        return layer.range * layer_idx

    def step(self, step_size=1):
        log.info('Stepping size: {}...'.format(step_size))
        for l in self._layers:  # type: Layer
            idx = self._layers.index(l)
            if self._packet_pos == idx and l.start_depth == 0:
                log.warning('Detected!!!! Layer: {}, Step: {}'.format(idx, self._packet_pos))
                self._sec_value += self.get_value(idx)
            log.debug('Stepping layer {}...'.format(idx))
            l.move(step_size=step_size)

        log.debug('Moving packet ahead...')
        self._packet_pos += step_size


def parse_input(s_input):
    # type: (str) -> (list[str], int)
    outs = []
    relations = 0
    for line in [l for l in s_input.split('\n') if l]:
        pid, knows = line.split('<->')
        pid = int(pid.strip())
        knows = [int(pid.strip()) for pid in knows.split(',')]
        outs.append((pid, knows))
        relations += 1
    return outs, relations


def main():
    intext = common.read_input(12)
    pid_relations, num_relations = parse_input(s_input=intext)
    graph = graph_generator(pid_relations, num_relations)

    log.info('Starting part 1...')
    answer_1 = len(links_to(graph, 0))
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = len(graph.findConnectedComponents())
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day12', level='INFO')
    main()
