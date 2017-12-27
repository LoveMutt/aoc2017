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


def knows(progs, p1, p2, checked=None):
    # type: (dict, int, int) -> bool
    if checked == None:
        checked = set([])
    children = progs[p1].difference({p1})  # remove p from its own children
    if p2 in children or \
            p1 == p2:
        return True

    for p in children:
        if p not in checked:
            checked.add(p)
        else:
            continue
        return knows(progs=progs, p1=p, p2=p2, checked=checked)
    return False


def count_linking_to(progs, p):
    count = 0
    for sub_p in progs:
        if knows(progs, sub_p, p):
            count += 1
    return count


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
    intext = common.read_input(12)
    pid_relations = parse_input(s_input=intext)
    programs = program_generator(pid_relations)

    log.info('Starting part 1...')
    target = 0
    answer_1 = count_linking_to(programs, target)
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day12', level='INFO')
    main()
