import binascii
import common

log = common.get_logger(__name__)

N = 'n'
S = 's'
E = 'e'
W = 'w'
NE = 'ne'
NW = 'nw'
SE = 'se'
SW = 'sw'


class HexGrid:
    def __init__(self):
        self.origin = None  # type: tuple(int, int, int)
        self.coordinates = None  # type: tuple(int, int, int)
        self.reset()

    def reset(self):
        self.origin = (0, 0, 0)  # x, y, z
        self.coordinates = self.origin

    def move(self, direction):
        # type: (str) -> None
        x, y = self.coordinates
        if direction.startswith('n'):
            y += 1
        elif direction.startswith('s'):
            y -= 1
        if direction.endswith('e'):
            x += 1
        elif direction.endswith('w'):
            x -= 1
        self.coordinates = (x, y)

    def follow(self, l_directions):
        # type: (list[str]) -> None
        for direction in l_directions:
            self.move(direction)

    @property
    def distance(self):
        path_x = self.coordinates[0]
        path_y = self.coordinates[1]
        origin_x = self.origin[0]
        origin_y = self.origin[1]
        return abs(path_x - origin_x) + abs(path_y - origin_y)


def parse_input(s_input):
    # type: (str) -> list[str]
    return [s.strip() for s in s_input.split(',')]


def main():
    intext = common.read_input(11)
    directions = parse_input(s_input=intext)
    log.info('Starting part 1...')
    answer_1 = 'Unknown'
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = 'Unknown'
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day11', level='INFO')
    main()
