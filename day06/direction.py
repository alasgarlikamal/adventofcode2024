from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def turn_right(self):
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
            case Direction.RIGHT:
                return Direction.DOWN
