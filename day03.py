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
        self._target_x = 0
        self._target_y = 0
        self._direction = RIGHT

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
        if self._direction == RIGHT:
            self._target_x = self._target_x + 1
        elif self._direction == UP:
            self._target_y = self._target_y + 1
        elif self._direction == LEFT:
            self._target_x = self._target_x - 1
        else:
            self._target_y = self._target_y - 1

    def spiral_to(self, val):
        step = 0
        while True:
            step = step + 1
            for i in range(2):
                for j in range(step):
                    if self._target_val == val:
                        return
                    self._target_val += 1
                    self.incr_coordinates()
                self.turn()

    def distance_to_target(self, val):
        self.spiral_to(val)
        return abs(self._target_y) + abs(self._target_x)


def main():
    input_part_1 = 265149
    s = CartesianSpiral()
    answer_1 = s.distance_to_target(input_part_1)
    print('The answer to part 1 is: {}'.format(answer_1))
    print('The answer to part 2 is: {}'.format('unknown'))


if __name__ == '__main__':
    log = common.get_logger('day02', level='INFO')
    main()
