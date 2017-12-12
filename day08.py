import common
import sys

log = common.get_logger(__name__)


class Register:
    def __init__(self, id=''):
        self.id = id
        self.value = 0

    def exec_inst(self, s_inst):
        parts = s_inst.split(' ')
        if len(parts) == 3:
            _, direction, value = parts
        else:
            direction, value = parts
        value = int(value)
        if direction == 'inc':
            self.value += value
        elif direction == 'dec':
            self.value -= value
        else:
            log.error('Bad instruction: {}'.format(s_inst))
            sys.exit(3)


class RegisterCollection:
    def __init__(self, registers=None):
        self.registers = []
        if isinstance(registers, list):
            for r in registers:
                self.add_register(r)
        self._max_seen = -1

    @property
    def ids(self):
        return [r.id for r in self.registers]

    @property
    def max_seen(self):
        return self._max_seen

    def add_register(self, register):
        if not register.id in [r.id for r in self.registers]:
            self.registers.append(register)
            if register.value > self._max_seen:
                self._max_seen = register.value

    @staticmethod
    def parse_instruction(s_inst):
        # type: (str) -> list(str)
        predicate, conditon = [s.strip() for s in s_inst.split('if')]
        target_reg, direction, value = predicate.split(' ')
        return target_reg, direction, value, conditon

    def get_register_by_id(self, id):
        registers = [r for r in self.registers if r.id == id]
        return registers[0]

    def test_condition(self, s_cond):
        reg_id, cond, value = s_cond.split(' ')
        register = self.get_register_by_id(reg_id)
        if not isinstance(register.value, int) or \
                not isinstance(int(value), int) or \
                ';' in s_cond or 'import' in s_cond:
            log.error('Stop hacking me')
            sys.exit(2)
        s_test = '{} {} {}'.format(register.value, cond, value)
        b = eval(s_test)
        return b

    def exec_instruction(self, s):
        # type: (str) -> None
        tgt_reg, direction, val, s_cond = RegisterCollection.parse_instruction(s)
        if self.test_condition(s_cond):
            r = self.get_register_by_id(tgt_reg)  # type: Register
            s_inst = '{} {}'.format(direction, val)
            r.exec_inst(s_inst)
            if r.value > self._max_seen:
                self._max_seen = r.value

    def proc(self, instructions):
        # type: (list(str)) -> None
        for inst in instructions:
            self.exec_instruction(inst)


def parse_input(intext):
    return [r.strip() for r in intext.split('\n') if r]


def init_collection_from_input(intext):
    lines = parse_input(intext)
    rc = RegisterCollection()
    for line in lines:
        try:
            r_name1, _, _, _, r_name2, _, _ = line.split(' ')
        except ValueError as e:
            log.exception('Error on input: {}'.format(line))
            raise e
        reg1 = Register(id=r_name1)
        reg2 = Register(id=r_name2)
        rc.add_register(register=reg1)
        rc.add_register(register=reg2)
    return rc


def main():
    s_instr = common.read_input(8)
    rc = init_collection_from_input(s_instr)
    rc.proc(parse_input(s_instr))
    answer_1 = max([r.value for r in rc.registers])
    answer_2 = rc.max_seen
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day08', level='INFO')
    main()
