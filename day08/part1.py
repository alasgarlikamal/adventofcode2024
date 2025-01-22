INPUT_FILE = "input.txt"

map: list[str] = []
with open(INPUT_FILE, "r") as file:
    for line in file:
        map.append(line.strip())

map.reverse()

HEIGHT = len(map)
WIDTH = len(map[0])

visited_antennas: set[str] = set()
unique_antinodes: set[tuple[int, int]] = set()


def find_occurences(antenna: str) -> list[tuple[int, int]]:
    occurences: list[tuple[int, int]] = []
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col == antenna:
                occurences.append((x, y))
    return occurences


def calculate_collinearity(points: list[tuple[int, int]]) -> set[tuple[int, int]]:

    antinodes: set[tuple[int, int]] = set()
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            point1 = (2 * x1 - x2, 2 * y1 - y2)
            point2 = (2 * x2 - x1, 2 * y2 - y1)

            if in_bounds(point1):
                antinodes.add(point1)

            if in_bounds(point2):
                antinodes.add(point2)

    return antinodes


def in_bounds(antinode: tuple[int, int]) -> bool:
    x, y = antinode
    if not (0 <= x < WIDTH):
        return False
    if not (0 <= y < HEIGHT):
        return False
    return True


for row in map:
    for char in row:
        if char == ".":
            continue
        if char in visited_antennas:
            continue
        occurences = find_occurences(char)
        antinodes = calculate_collinearity(occurences)
        unique_antinodes |= antinodes
        visited_antennas.add(char)

print("Total unique antinode locations:", len(unique_antinodes))
