import common

log = common.get_logger(__name__)


class Register:
    def __init__(self, id='', value=0):
        self.id = id
        self.value = value


class RegisterCollection:
    def __init__(self, registers=None):
        self.registers = registers
        if self.registers is None:
            self.registers = []

    def add_register(self, register):
        self.registers.append(register)

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

    def do_instruction(self, s):
        tgt, mod, val, c_reg, c_mod, c_val = parse_input(s)



def parse_input(intext):
    return intext.split('\n')


def main():
    answer_1 = 'Unknown'
    answer_2 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day08', level='INFO')
    main()
