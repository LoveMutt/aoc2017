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
        if self._range > 0:  # don't do any movement with range 0
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
        self._layers = layers
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
        layer = self._layers[self._packet_pos]  # type: Layer
        if layer.start_depth == 0:
            add_score = self.get_value(self._packet_pos)
            log.warning('Detected!!!! Layer: {}. Adding score: {}'.format(self._packet_pos, add_score))
            self._sec_value += add_score
        log.debug('Stepping layers...')
        for l in self._layers:  # type: Layer
            l.move(step_size=step_size)

        log.debug('Moving packet ahead...')
        self._packet_pos += step_size

    def run(self):
        for i in range(len(self._layers)):
            self.step()

    def __repr__(self):
        return "<Scanner packet_pos: {}, pos_layer: {} />".format(self._packet_pos, self._layers[self._packet_pos])


def parse_input(s_input):
    # type: (str) -> (list[Layer])
    tmp = {}
    out = []
    log.info('Pre-processing input to get max layers...')
    max_layer = -1
    for line in [l for l in s_input.split('\n') if l]:
        layer, irange = line.replace(' ', '').split(':')
        layer = int(layer)
        irange = int(irange)
        if layer > max_layer:
            max_layer = layer
        tmp[layer] = irange
    log.info('Generating layers for scanner...')
    for i in range(max_layer + 1):
        irange = tmp.get(i, 0)
        log.debug('Creating Layer idx: {} with range: {}'.format(i, irange))
        layer = Layer(irange=irange)
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
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day13', level='INFO')
    main()
