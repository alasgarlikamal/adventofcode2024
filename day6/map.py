class Map:
    rows: list[list[str]]
    starting_position: tuple[int, int]
    height: int
    width: int

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.starting_position = self.get_starting_position()

    def get_starting_position(self) -> tuple[int, int]:
        for idx1, row in enumerate(self.rows):
            for idx2, col in enumerate(row):
                if col == "^":
                    return idx2, idx1

        return (0, 0)

    def in_bounds(self, position: tuple[int, int]) -> bool:
        (x, y) = position
        return (0 <= x < self.width) and (0 <= y < self.height)

    def print(self):
        for row in reversed(self.rows):
            print("".join(row))
        print("\n")
