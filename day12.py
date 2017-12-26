import common

log = common.get_logger(__name__)


class Program:
    def __init__(self):
        self._pid = -1
        self._gid = -1
        self._knows = set([])


class PManager:
    def __init__(self):
        self._pids = set([])

    def add_pid(self, pid):
        self._pids.add(pid)

    def knows(self, pid1, pid2):
        talkers = set([])
        while True:
            talkers.union(pid1._knows)
            break
        return pid2 in talkers

def parse_input(s_input):
    # type: (str) -> list[str]
    outs = []
    for line in [l for l in s_input.split('\n') if l]:
        pid, knows = line.split('<->')
        pid = int(pid.strip())
        knows = [int(pid.strip()) for pid in knows.split(',')]
        outs.append((pid, knows))
    return outs


def program_generator(pid_relation):
    for pid, knows in pid_relation:
        p


def main():
    intext = common.read_input(11)
    pid_relations = parse_input(s_input=intext)

    log.info('Starting part 1...')
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day12', level='INFO')
    main()
