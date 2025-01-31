INPUT_FILE = "input.txt"
SECONDS = 100
HEIGHT = 103
WIDTH = 101


def parse_values(txt: str):
    idx = 2
    x = ""
    while txt[idx] != ",":
        x += txt[idx]
        idx += 1

    return int(x), int(txt[idx + 1 :])


def get_quadrant(pos: tuple[int, int]):
    x, y = pos

    if x > WIDTH // 2 and y < HEIGHT // 2:
        return "I"
    elif x < WIDTH // 2 and y < HEIGHT // 2:
        return "II"
    elif x < WIDTH // 2 and y > HEIGHT // 2:
        return "III"
    elif x > WIDTH // 2 and y > HEIGHT // 2:
        return "IV"

    return None


robots: list[dict[str, tuple[int, int]]] = []
with open(INPUT_FILE, "r") as file:
    for line in file:
        line = line.strip()
        p, v = line.split()
        robots.append({"pos": parse_values(p), "vel": parse_values(v)})

positions: dict[tuple[int, int], int] = {}

for robot in robots:
    new_pos = (
        (robot["pos"][0] + SECONDS * robot["vel"][0]) % WIDTH,
        (robot["pos"][1] + SECONDS * robot["vel"][1]) % HEIGHT,
    )

    if new_pos not in positions:
        positions[new_pos] = 0
    positions[new_pos] += 1

quadrants = {"I": 0, "II": 0, "III": 0, "IV": 0}

for pos, count in positions.items():
    if quadrant := get_quadrant(pos):
        quadrants[quadrant] += count

sum = 1

for val in quadrants.values():
    sum *= val

print(sum)
