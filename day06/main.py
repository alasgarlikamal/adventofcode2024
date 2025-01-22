from map import Map
from guard import Guard
from position import Position
import json


INPUT_FILE = "input.txt"

rows: list[list[str]] = []
with open(INPUT_FILE, "r") as file:
    for line in file:
        rows.append(list(line.strip()))

rows.reverse()
map_dump = json.dumps(rows)


def part1():
    map_ = Map(json.loads(map_dump))
    guard = Guard(map_.starting_position)

    while map_.in_bounds(position := Position.turn(guard.position, guard.direction)):
        guard.go_to(position)
        x, y = position
        if map_.rows[y][x] == "#":
            guard.go_back()
            guard.rotate_right()

    points = set(map(lambda x: x[0], guard.path))
    return points, guard


def check_loop(map: Map):
    guard = Guard(map.starting_position)
    while map.in_bounds(position := Position.turn(guard.position, guard.direction)):
        x, y = position
        visit = ((x, y), guard.direction)

        if visit in guard.path:
            return True

        guard.go_to(position)
        if map.rows[y][x] == "#":
            guard.go_back()
            guard.rotate_right()

    return False


def part2(guard: Guard):
    points = list(guard.path)[1:]
    loops: set[tuple[int, int]] = set()

    for idx, ((x, y), direction) in enumerate(points):
        map = Map(json.loads(map_dump))
        map.rows[y][x] = "#"

        if check_loop(map):
            loops.add((x, y))
        print("\033[H\033[J", end="")
        print(f"Found {len(loops)} loops out of {idx+1} possibilites")

    return len(loops)


if __name__ == "__main__":
    points, guard = part1()
    loop_count = part2(guard)

    print("Total distinct points visited:", len(points))
    print("Total possible loops: ", loop_count)
