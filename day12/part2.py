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


def get_sides(coords: tuple[int, int]):
    row, col = coords
    top = (row - 1, col)
    bottom = (row + 1, col)
    left = (row, col - 1)
    right = (row, col + 1)
    return [(top, "top"), (bottom, "bottom"), (left, "left"), (right, "right")]


def get_corners(coords: tuple[int, int]):
    row, col = coords
    top_left = (row - 1, col - 1)
    top_right = (row - 1, col + 1)
    bottom_right = (row + 1, col + 1)
    bottom_left = (row + 1, col - 1)
    return [
        (top_left, "top_left"),
        (top_right, "top_right"),
        (bottom_right, "bottom_right"),
        (bottom_left, "bottom_left"),
    ]


def inc_corners_by(coords: tuple[int, int], checked: set[tuple[int, int]]):
    adjacent = get_sides(coords) + get_corners(coords)
    corners = {
        "top_right": 0,
        "top_left": 0,
        "bottom_left": 0,
        "bottom_right": 0,
    }
    sole_corner = []
    for coord, name in adjacent:
        if in_bounds(coord) and coord in checked:
            if name == "top":
                corners["top_right"] += 1
                corners["top_left"] += 1
            elif name == "bottom":
                corners["bottom_right"] += 1
                corners["bottom_left"] += 1
            elif name == "right":
                corners["top_right"] += 1
                corners["bottom_right"] += 1
            elif name == "left":
                corners["top_left"] += 1
                corners["bottom_left"] += 1
            else:
                corners[name] += 1
                sole_corner.append(name)
    count = 0
    for key, val in corners.items():
        if val == 0:
            count += 1
        elif val == 3:
            count -= 1
        elif val == 1 or val == 2:
            if key in sole_corner:
                count += 1
            else:
                count -= 1

    return count


def bfs(farm: list[list[str]], coords: tuple[int, int]):
    char = farm[coords[0]][coords[1]]

    queue: list[tuple[int, int]] = [coords]
    checked: set[tuple[int, int]] = set([coords])
    area, corners = 1, 4

    while len(queue) > 0:
        for idx, (row, col) in enumerate(queue):
            for coord, _ in get_sides((row, col)):
                if (
                    in_bounds(coord)
                    and coord not in checked
                    and get_char(coord, farm) == char
                ):
                    queue.append(coord)
                    checked.add(coord)
                    farm[coord[0]][coord[1]] = "."
                    area += 1
                    corners += inc_corners_by(coord, checked)
                    # for i in farm:
                    #     print("".join(i))
                    # print(corners)
                    # print("\n")

            queue.pop(idx)

    # for i, j in checked:
    #     farm[i][j] = "."
    return area * corners


total_price = 0
for idx_row, row in enumerate(farm):
    for idx_col, col in enumerate(row):
        if col != ".":
            total_price += bfs(farm, (idx_row, idx_col))

print(total_price)
