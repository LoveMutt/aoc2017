import common

log = common.get_logger(__name__)

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'


class CartesianSpiral:
    def __init__(self):
        # starting values
        self._target_val = 1
        self._max_x = 0
        self._max_y = 0
        self.squares = [self.Square(1, 0, 0)]
        self._direction = RIGHT

    class Square:
        def __init__(self, value=0, x=0, y=0):
            self.value = value
            self.x = x
            self.y = y
            self.adjacents = self.set_adjacents()

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
        last_sq = self.squares[-1]
        if self._direction == RIGHT:
            self._max_x = last_sq.x + 1
        elif self._direction == UP:
            self._max_y = last_sq.y + 1
        elif self._direction == LEFT:
            self._max_x = last_sq.x - 1
        else:
            self._max_y = last_sq.y - 1
        return (self._max_x, self._max_y)

    def incr_value(self):
        last_sq = self.squares[-1]
        return last_sq.value + 1

    def spiral_to(self, val, part1=True):
        step = 0
        sq = self.squares[0]
        while True:
            step = step + 1
            for i in range(2):
                for j in range(step):
                    if sq.value == val:
                        return
                    sq = self.Square()
                    x, y = self.incr_coordinates()
                    sq.x = x
                    sq.y = y
                    if part1:
                        sq.value = self.incr_value()
                    else:
                        sq.value = self.adj_sum(sq)
                    log.debug('Square: {}'.format(sq))
                    self.squares.append(sq)
                self.turn()

    def distance_to_target(self, val, part1=True):
        self.spiral_to(val, part1=part1)
        sq = self.squares[-1]
        return abs(sq.x) + abs(sq.y)

    def adj_sum(self, sq):
        """0, 0
           1, 0
           1, 1
           0, 1
           -1, 1
           -1, 0
           -1, -1
           0, -1
           -1, -1

           Do I just scan the list looking at coordinates or do I store them initially in a plane w/ queue/pop properties
        """
        x = sq.x
        y = sq.y
        x += 1


def main():
    input_part_1 = 265149
    s = CartesianSpiral()
    answer_1 = s.distance_to_target(input_part_1, part1=True)
    answer_2 = s.distance_to_target(input_part_1, part1=False)
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format(answer_2))


if __name__ == '__main__':
    log = common.get_logger('day02', level='INFO')
    main()
