from direction import Direction


class Position:
    @staticmethod
    def turn(position: tuple[int, int], direction: Direction):
        x, y = position
        match direction:
            case Direction.UP:
                return (x, y + 1)
            case Direction.DOWN:
                return (x, y - 1)
            case Direction.LEFT:
                return (x - 1, y)
            case Direction.RIGHT:
                return (x + 1, y)

    @staticmethod
    def backwards(position: tuple[int, int], direction: Direction):
        x, y = position
        match direction:
            case Direction.UP:
                return Position.turn(position, Direction.DOWN)
            case Direction.DOWN:
                return Position.turn(position, Direction.UP)
            case Direction.LEFT:
                return Position.turn(position, Direction.RIGHT)
            case Direction.RIGHT:
                return Position.turn(position, Direction.LEFT)
