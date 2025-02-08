INPUT_FILE = "input.txt"


def find_robot_pos(map):
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "@":
                return x, y
    return 0, 0


def move_robot(pos: tuple[int, int], dir: str):
    x, y = pos
    if dir == ">":
        return (x + 1, y)
    elif dir == "<":
        return (x - 1, y)
    elif dir == "^":
        return (x, y - 1)
    else:
        return (x, y + 1)


def move_vertically(pos: tuple[int, int], dir: str, map: list[list[str]]):
    x, y = pos
    inc = -1 if dir == "^" else 1

    queue: list[tuple[int, int]] = [
        pos
    ]  # List of Coordinates of Box with its complement

    temp: list[tuple[int, int]] = []
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        to_move = map[y + inc][x]
        to_move_complement = map[y + inc][x + 1]
        if to_move == "#" or to_move_complement == "#":
            return False
        if (x, y) not in temp:
            temp.append((x, y))

        box = to_move + to_move_complement
        if box == "[]":
            queue.append(((x, y + inc)))
        elif box == "][":
            queue.append(((x - 1, y + inc)))
            queue.append(((x + 1, y + inc)))
        elif box == "].":
            queue.append((x - 1, y + inc))
        elif box == ".[":
            queue.append(((x + 1, y + inc)))

    # Updating Map
    temp = sorted(temp, key=lambda x: x[1])
    temp = temp if dir == "^" else list(reversed(temp))
    for x, y in temp:  # Move the items in temp:
        map[y + inc][x] = map[y][x]
        map[y + inc][x + 1] = map[y][x + 1]
        map[y][x] = "."
        map[y][x + 1] = "."

    return True


def move_horizontally(pos: tuple[int, int], dir: str, map: list[list[str]]):
    x, y = pos
    if dir == ">":
        while map[y][x] == "[" and map[y][x + 1] == "]":
            x += 2
    else:
        while map[y][x] == "]" and map[y][x - 1] == "[":
            x -= 2

    if map[y][x] == ".":
        if dir == ">":
            for i in range(x, pos[0], -1):
                map[y][i] = map[y][i - 1]
        else:
            for i in range(x, pos[0]):
                map[y][i] = map[y][i + 1]

        map[pos[1]][pos[0]] = "."
        return True

    return False


def move_boxes(pos: tuple[int, int], dir: str, map: list[list[str]]):
    x, y = pos
    char = map[y][x]

    if dir == "^" or dir == "v":
        return move_vertically((x if char == "[" else x - 1, y), dir, map)
    else:
        return move_horizontally(pos, dir, map)


with open(INPUT_FILE, "r") as file:
    text = file.read().strip()

old_map, movements = text.split("\n\n")
old_map = [list(x) for x in old_map.split("\n")]
movements = "".join(movements.split("\n"))

map: list[list[str]] = []

# Doubling map
for row in old_map:
    extension = []
    for char in row:
        if char == ".":
            extension.append(".")
            extension.append(".")
        elif char == "#":
            extension.append("#")
            extension.append("#")
        elif char == "O":
            extension.append("[")
            extension.append("]")
        else:
            extension.append("@")
            extension.append(".")
    map.append(extension)

robot_pos: tuple[int, int] = find_robot_pos(map)

for mov in movements:
    x, y = move_robot(robot_pos, mov)
    char = map[y][x]

    if char == "#":
        continue

    if char in ["]", "["]:
        if not move_boxes((x, y), mov, map):
            continue

    map[robot_pos[1]][robot_pos[0]] = "."
    robot_pos = (x, y)
    map[y][x] = "@"

sum = 0
for i, row in enumerate(map):
    for j, char in enumerate(row):
        if char == "[":
            sum += 100 * i + j

print(sum)
