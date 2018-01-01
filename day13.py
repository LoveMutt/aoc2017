import common

log = common.get_logger(__name__)


class Layer:
    def __init__(self, idepth=0, irange=-1):
        self._start_depth = idepth
        self._end_depth = self._start_depth + 1
        self._range = irange
        self._scalar = 1  # switches from 1 to -1

    @property
    def start_depth(self):
        return self._start_depth

    @property
    def end_depth(self):
        return self._end_depth

    def move(self, step_size=1):
        self._start_depth = self._end_depth
        if (self._end_depth == self._range - 1) or (self._end_depth == 0):
            self._scalar *= -1  # reverse direction of stepping
        end = self._end_depth + (step_size * self._scalar)
        self._end_depth = end


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
