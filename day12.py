import common

log = common.get_logger(__name__)


def program_generator(pid_relation):
    programs = {}
    for pid, k_pids in pid_relation:
        links = programs.get(pid, set([]))
        links = links.union(k_pids)
        programs[pid] = links
        for k_pid in k_pids:
            k_links = programs.get(k_pid, set([]))
            k_links.add(pid)
            programs[k_pid] = k_links
    return programs


def knows(progs, p1, p2):
    # type: (dict, int, int) -> bool
    if p1 == p2:
        return True
    if p2 in progs[p1]:
        return True
    for p in [child for child in progs[p1] if child != p1]:
        return knows(progs=progs, p1=p, p2=p2)
    return False


def parse_input(s_input):
    # type: (str) -> list[str]
    outs = []
    for line in [l for l in s_input.split('\n') if l]:
        pid, knows = line.split('<->')
        pid = int(pid.strip())
        knows = [int(pid.strip()) for pid in knows.split(',')]
        outs.append((pid, knows))
    return outs


def main():
    intext = common.read_input(11)
    pid_relations = parse_input(s_input=intext)
    programs = program_generator(pid_relations)

    log.info('Starting part 1...')
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day12', level='INFO')
    main()
