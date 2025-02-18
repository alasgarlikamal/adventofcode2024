MEMORY_LENGTH = 71
BYTES_TO_READ = 1024


def read_bytes():
    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.strip().split(",")
            yield int(y), int(x)


def filter_nodes(node: tuple[int, int]):
    x, y = node

    if x < 0 or x >= MEMORY_LENGTH or y < 0 or y >= MEMORY_LENGTH:
        return False

    return memory[y][x] != "#"


def get_nodes(memory):
    for row_idx, row in enumerate(memory):
        for char_idx, char in enumerate(row):
            if char != "#":
                node = (char_idx, row_idx)

                top = (char_idx, row_idx - 1)
                bottom = (char_idx, row_idx + 1)
                left = (char_idx - 1, row_idx)
                right = (char_idx + 1, row_idx)

                adjacent = list(
                    filter(
                        filter_nodes,
                        [top, bottom, left, right],
                    )
                )
                yield (node, adjacent)


def djikstra(
    nodes: dict[tuple[int, int], list[tuple[int, int]]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> float:

    def next(unvisited, distances) -> tuple[int, int]:
        min = unvisited[0]
        for i in unvisited:
            if distances[i] < distances[min]:
                min = i
        return min

    unvisited = [x for x in nodes.keys()]
    distances: dict[tuple[int, int], float] = {node: float("inf") for node in unvisited}
    distances[start] = 0

    while len(unvisited) > 0:
        curr = next(unvisited, distances)
        distance = distances[curr]
        for node in nodes[curr]:
            distances[node] = min(distance + 1, distances[node])

        unvisited.remove(curr)

    return distances[end]


memory = [["." for i in range(MEMORY_LENGTH)] for i in range(MEMORY_LENGTH)]
bytes = list(read_bytes())
for i in range(BYTES_TO_READ):
    x, y = bytes[i]
    memory[y][x] = "#"

start = (0, 0)
end = (MEMORY_LENGTH - 1, MEMORY_LENGTH - 1)
nodes = dict(get_nodes(memory))
score = djikstra(nodes, start, end)
print(score)
