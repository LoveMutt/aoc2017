import common
import sys
from collections import namedtuple

log = common.get_logger(__name__)

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'


CoordSquare = namedtuple('CoordSquare', 'coordinates square')


class CartesianSpiral:
    def __init__(self):
        # starting values
        self._target_val = 0
        self._max_x = 0
        self._max_y = 0
        self.coodsquares = []
        self._direction = ''
        self.reset()

    class Square:
        def __init__(self, value=0, x=0, y=0):
            self.value = value
            self.x = x
            self.y = y
            self.set_adjacents()

        def set_adjacents(self):
            adjacents = set([])
            adjacents.add((self.x + 1, self.y))
            adjacents.add((self.x + 1, self.y + 1))
            adjacents.add((self.x, self.y + 1))
            adjacents.add((self.x - 1, self.y + 1))
            adjacents.add((self.x - 1, self.y))
            adjacents.add((self.x - 1, self.y - 1))
            adjacents.add((self.x, self.y - 1))
            adjacents.add((self.x + 1, self.y - 1))
            self.adjacents = adjacents

        def __repr__(self):
            return '<Square: value={}, x={}, y={}'.format(self.value, self.x, self.y)

    @property
    def origin(self):
        return (0, 0)

    @property
    def origin_square(self):
        x, y = self.origin
        return self.Square(1, x, y)

    def reset(self):
        self._target_val = 1
        self.max_val = -1
        self._max_x = 0
        self._max_y = 0
        csq = CoordSquare(coordinates=self.origin, square=self.origin_square)
        self.coodsquares = [csq]
        self._direction = RIGHT

    def turn(self):
        if self._direction == RIGHT:
            self._direction = UP
        elif self._direction == UP:
            self._direction = LEFT
        elif self._direction == LEFT:
            self._direction = DOWN
        else:
            self._direction = RIGHT


    def incr_coordinates(self):
        last_sq = self.coodsquares[-1]  # type: CoordSquare
        if self._direction == RIGHT:
            self._max_x = last_sq.square.x + 1
        elif self._direction == UP:
            self._max_y = last_sq.square.y + 1
        elif self._direction == LEFT:
            self._max_x = last_sq.square.x - 1
        else:
            self._max_y = last_sq.square.y - 1
        return (self._max_x, self._max_y)

    def part1_val(self):
        last_sq = self.coodsquares[-1]  # type: CoordSquare
        return last_sq.square.value + 1

    def spiral_to(self, val=0, index=0, part1=True):
        # type: (int) -> None
        """
        Spiral until either a value is reached or an index is reached. Part1 tells this function how to assign a value
        """
        self.reset()
        if index:
            part1 = False  # shortcut to not rewrite code
        step = 0
        csq = self.coodsquares[0]  # type: CoordSquare
        while True:
            log.debug('increasing step to move around existing coodsquares')
            step = step + 1
            for i in range(2):
                for j in range(step):
                    if val:
                        if csq.square.value == val:
                            return
                    elif index:
                        if len(self.coodsquares) == index:
                            return
                    x, y = self.incr_coordinates()
                    if part1:
                        nxt_val = self.part1_val()
                    else:
                        new_sq = CartesianSpiral.Square(value=0, x=x, y=y)
                        nxt_val = self.part2_val(new_sq)
                    self.max_val = nxt_val
                    csq = CoordSquare(coordinates=(x, y), square=self.Square(value=nxt_val, x=x, y=y))
                    log.debug('Square: {}'.format(csq))
                    self.coodsquares.append(csq)
                self.turn()

    def distance_to_target(self, val, part1=True):
        self.spiral_to(val, part1=part1)
        csq = self.coodsquares[-1]  # type: CoordSquare
        x, y = csq.coordinates
        return abs(x) + abs(y)

    def part2_val(self, sq):
        # type: (CartesianSpiral.Square) -> int
        """
        Sum the adjacent coodsquares to a square
        """
        sumval = 0
        for adj_coord in sq.adjacents:
            adjsq = self.get_square_by_coord(adj_coord)
            adj_val = adjsq.value
            sumval += adj_val
        return sumval

    def get_square_by_coord(self, coord_tup):
        # type: (tuple) -> CartesianSpiral.Square
        for squareplot in self.coodsquares:  # type: CoordSquare
            if squareplot.coordinates == coord_tup:
                return squareplot.square
        return CartesianSpiral.Square(0, -1000000000, -100000000)

    def get_coordsquare(self, num):
        # type: (int) -> CoordSquare
        """
        Allow indexing by 1-based
        """
        return self.coodsquares[num - 1]


def main():
    input_val = 265149
    s = CartesianSpiral()
    # answer_1 = s.distance_to_target(input_val, part1=True)
    # print('The answer to part 1 is: {}'.format(answer_1))
    n = 0
    while True:
        n += 100
        s.spiral_to(index=n, part1=False)
        if not s.max_val > input_val:
            continue
        else:
            answer_2 = -1
            values = [t.square.value for t in s.coodsquares]
            values = sorted(values)
            for v in values:
                if v > input_val:
                    answer_2 = v
                    break
            break
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day02', level='INFO')
    main()
