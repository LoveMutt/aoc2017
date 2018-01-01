import common

from apgl.graph import SparseGraph

log = common.get_logger(__name__)


def graph_generator(pid_relation, num_relations):
    graph = SparseGraph(num_relations)
    for pid, k_pids in pid_relation:
        for k_pid in k_pids:
            graph[pid, k_pid] = 1
    return graph


def knows(graph, p1, p2):
    # type: (SparseGraph, int, int) -> bool
    for relations in graph.findConnectedComponents():
        if p1 in relations:
            return p2 in relations
    return False


def links_to(graph, p):
    # type: (SparseGraph, int) -> list[int]
    group = [l for l in graph.findConnectedComponents() if p in l]
    return group[0]


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
