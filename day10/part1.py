INPUT_FILE = "input.txt"

topographic_map: list[list[int]] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        line = line.strip()
        nums = list(map(int, list(line)))
        topographic_map.append(nums)

MAX_HEIGHT = len(topographic_map)
MAX_WIDTH = len(topographic_map[0])
trailheads: list[tuple[int, int]] = []

for row_idx in range(MAX_HEIGHT):
    for col_idx in range(MAX_WIDTH):
        if topographic_map[row_idx][col_idx] == 0:
            trailheads.append((row_idx, col_idx))


def find_trail(coord: tuple[int, int], found: set[tuple[int, int]]):

    row_idx, col_idx = coord
    current_num = topographic_map[row_idx][col_idx]
    if current_num == 9:
        if coord not in found:
            found.add(coord)
            return 1
        return 0

    count = 0
    # Traverse UP
    if row_idx > 0 and topographic_map[row_idx - 1][col_idx] == current_num + 1:
        count += find_trail((row_idx - 1, col_idx), found)

    # Traverse DOWN
    if (
        row_idx < MAX_HEIGHT - 1
        and topographic_map[row_idx + 1][col_idx] == current_num + 1
    ):
        count += find_trail((row_idx + 1, col_idx), found)

    # Traverse LEFT
    if col_idx > 0 and topographic_map[row_idx][col_idx - 1] == current_num + 1:
        count += find_trail((row_idx, col_idx - 1), found)

    # Traverse RIGHT
    if (
        col_idx < MAX_WIDTH - 1
        and topographic_map[row_idx][col_idx + 1] == current_num + 1
    ):
        count += find_trail((row_idx, col_idx + 1), found)

    return count


sum = 0
for trailhead in trailheads:
    sum += find_trail(trailhead, set())

print(sum)
