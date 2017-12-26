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


class Traveler:
    """    \ n  /
        nw +--+ ne
          /    \
        -+      +- X
          \    /
        sw +--+ se
          / s  \
        Z       Y
"""

    def __init__(self):
        self.origin = None  # type: tuple(int, int, int)
        self.coordinates = None  # type: tuple(int, int, int)
        self.max_distance = -1
        self.reset()

    def reset(self):
        self.origin = (0, 0, 0)  # x, y, z
        self.coordinates = self.origin
        self.max_distance = -1

    def move(self, direction):
        # type: (str) -> None
        # See http://keekerdc.com/wp-content/uploads/2011/03/HexGridLandscapeTriCoordinates.gif
        # N = y+, S = y-  and E = x+, W = x-
        x, y, z = self.coordinates
        if direction == NE:
            z -= 1
            x += 1
        elif direction == SW:
            z += 1
            x -= 1
        elif direction == SE:
            y -= 1
            x += 1
        elif direction == NW:
            y += 1
            x -= 1
        elif direction == N:
            y += 1
            z -= 1
        elif direction == S:
            y -= 1
            z += 1

        self.coordinates = (x, y, z)
        if self.max_distance < self.distance:
            self.max_distance = self.distance

    def follow(self, l_directions):
        # type: (list[str]) -> None
        for direction in l_directions:
            self.move(direction)

    @property
    def distance(self):
        hex_distance = self.distance_from_hex(self.origin)
        return hex_distance

    def distance_from_hex(self, h2):
        # http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = (0, 0, 0)
        if isinstance(h2, Traveler):
            x_2, y_2, z_2 = h2.origin
        elif isinstance(h2, tuple):
            x_2, y_2, z_2 = h2
        dist1 = abs(y_2 - y_1)
        dist2 = abs(x_2 - x_1)
        dist3 = abs(z_2 - z_1)
        hex_distance = max(dist1, dist2, dist3)
        return hex_distance

    def __repr__(self):
        return "<HexGrid (x, y, z)={}, distance={} />".format(self.coordinates, self.distance)


def parse_input(s_input):
    # type: (str) -> list[str]
    return [s.strip() for s in s_input.split(',')]


def main():
    intext = common.read_input(11)
    directions = parse_input(s_input=intext)
    t = Traveler()
    t.follow(directions)
    log.info('Starting part 1...')
    answer_1 = t.distance
    print('The answer to part 1 is: {}'.format(answer_1))

    log.info('Starting part 2...')
    answer_2 = t.max_distance
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day11', level='INFO')
    main()
