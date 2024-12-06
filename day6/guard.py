from direction import Direction
from position import Position


class Guard:
    position: tuple[int, int]
    direction: Direction
    path: set[tuple[tuple[int, int], Direction]]

    def __init__(self, position: tuple[int, int]):
        self.position = position
        self.direction = Direction.UP
        self.path = {(position, self.direction)}

    def rotate_right(self):
        self.direction = self.direction.turn_right()

    def go_to(self, position: tuple[int, int]):
        self.position = position
        self.path.add((position, self.direction))

    def go_back(self):
        self.path.remove((self.position, self.direction))
        self.position = Position.backwards(self.position, self.direction)
