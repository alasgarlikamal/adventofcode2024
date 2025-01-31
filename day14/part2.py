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


def get_new_pos(robot: dict[str, tuple[int, int]], seconds: int):
    return (
        (robot["pos"][0] + seconds * robot["vel"][0]) % WIDTH,
        (robot["pos"][1] + seconds * robot["vel"][1]) % HEIGHT,
    )


robots: list[dict[str, tuple[int, int]]] = []
with open(INPUT_FILE, "r") as file:
    for line in file:
        line = line.strip()
        p, v = line.split()
        robots.append({"pos": parse_values(p), "vel": parse_values(v)})


def find_easter_egg():
    for i in range(10000):
        positions: dict[tuple[int, int], int] = {}
        for robot in robots:
            new_pos = get_new_pos(robot, i)
            if new_pos not in positions:
                positions[new_pos] = 0
            positions[new_pos] += 1

        for x, y in positions:
            found = True
            for j in range(13):
                if (x + j + 1, y) not in positions:
                    found = False
                    break
            if found:
                map = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
                for (x, y), val in positions.items():
                    map[y][x] = str(val)
                for line in map:
                    print("".join(line))
                print("FOUND AFTER:", i, "SECONDS")
                return i


find_easter_egg()
