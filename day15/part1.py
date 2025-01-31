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


def move_boxes(pos: tuple[int, int], dir: str, map: list[list[str]]):

    x, y = pos

    if dir == "^":
        while map[y][x] == "O":
            y -= 1
    elif dir == "v":
        while map[y][x] == "O":
            y += 1
    elif dir == ">":
        while map[y][x] == "O":
            x += 1
    else:
        while map[y][x] == "O":
            x -= 1

    if map[y][x] == ".":
        map[y][x] = "O"
        return True
    return False


with open(INPUT_FILE, "r") as file:
    text = file.read().strip()

map, movements = text.split("\n\n")
map = [list(x) for x in map.split("\n")]
movements = "".join(movements.split("\n"))

robot_pos: tuple[int, int] = find_robot_pos(map)

for mov in movements:
    x, y = move_robot(robot_pos, mov)

    if map[y][x] == "#":
        continue

    if map[y][x] == "O":
        if not move_boxes((x, y), mov, map):
            continue

    map[robot_pos[1]][robot_pos[0]] = "."
    robot_pos = (x, y)
    map[y][x] = "@"

sum = 0
for i, row in enumerate(map):
    for j, char in enumerate(row):
        if char == "O":
            sum += 100 * i + j

print(sum)
