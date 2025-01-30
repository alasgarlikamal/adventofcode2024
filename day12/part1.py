INPUT_FILE = "input.txt"

farm: list[list[str]] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        farm.append(list(line.strip()))

WIDTH = len(farm[0])
HEIGHT = len(farm)


def in_bounds(coords: tuple[int, int]):
    row, col = coords
    return (0 <= row < HEIGHT) and (0 <= col < WIDTH)


def get_char(coords: tuple[int, int], farm: list[list[str]]):
    return farm[coords[0]][coords[1]]


def sides(coords: tuple[int, int]):
    row, col = coords
    top = (row - 1, col)
    bottom = (row + 1, col)
    left = (row, col - 1)
    right = (row, col + 1)
    return [top, bottom, left, right]


def inc_perimeter_by(coords: tuple[int, int], checked: set[tuple[int, int]]):
    count = 0
    for coord in sides(coords):
        if in_bounds(coord) and coord in checked:
            count += 1

    return (-2 * count) + 4


def bfs(farm: list[list[str]], coords: tuple[int, int]):
    char = farm[coords[0]][coords[1]]

    queue: list[tuple[int, int]] = [coords]
    checked: set[tuple[int, int]] = set([coords])
    area, perimeter = 1, 4

    while len(queue) > 0:
        for idx, (row, col) in enumerate(queue):
            for coord in sides((row, col)):
                if (
                    in_bounds(coord)
                    and coord not in checked
                    and get_char(coord, farm) == char
                ):
                    queue.append(coord)
                    checked.add(coord)
                    area += 1
                    perimeter += inc_perimeter_by(coord, checked)

            queue.pop(idx)

    for i, j in checked:
        farm[i][j] = "."
    return area * perimeter


total_price = 0
for idx_row, row in enumerate(farm):
    for idx_col, col in enumerate(row):
        if col != ".":
            total_price += bfs(farm, (idx_row, idx_col))

print(total_price)
