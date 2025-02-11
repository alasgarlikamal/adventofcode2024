INPUT_FILE = "input.txt"


def get_char(maze, char) -> tuple[int, int]:
    for row_idx, row in enumerate(maze):
        for col_idx, col in enumerate(row):
            if col == char:
                return (col_idx, row_idx)

    return (0, 0)


def get_nodes(maze):
    for row_idx, row in enumerate(maze):
        for char_idx, char in enumerate(row):
            if char != "#":
                node = (char_idx, row_idx)

                top = (char_idx, row_idx - 1)
                bottom = (char_idx, row_idx + 1)
                left = (char_idx - 1, row_idx)
                right = (char_idx + 1, row_idx)

                adjacent = list(
                    filter(
                        lambda n: maze[n[1]][n[0]] != "#",
                        [top, bottom, left, right],
                    )
                )
                yield (node, adjacent)


def get_direction(node1: tuple[int, int], node2: tuple[int, int]):
    x1, y1 = node1
    x2, y2 = node2

    if y1 - y2 == 1:
        return "TOP"
    elif y1 - y2 == -1:
        return "BOTTOM"
    elif x1 - x2 == 1:
        return "LEFT"
    else:
        return "RIGHT"


def djikstra(
    nodes: dict[tuple[int, int], list[tuple[int, int]]],
    start: tuple[int, int],
    end: tuple[int, int],
):
    def next(unvisited, distances) -> tuple[int, int]:
        min = unvisited[0]
        for i in unvisited:
            if distances[i] < distances[min]:
                min = i
        return min

    unvisited = [x for x in nodes.keys()]
    distances: dict[tuple[int, int], tuple[float, None | str]] = {
        node: (float("inf"), None) for node in unvisited
    }
    distances[start] = (0, "RIGHT")

    while len(unvisited) > 0:
        curr = next(unvisited, distances)
        distance, curr_direction = distances[curr]
        for node in nodes[curr]:
            direction = get_direction(curr, node)
            edge = 1 if direction == curr_direction else 1001
            distances[node] = (min(distance + edge, distances[node][0]), direction)

        unvisited.remove(curr)
    return distances[end]


maze: list[list[str]] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        maze.append(list(line.strip()))

start = get_char(maze, "S")
end = get_char(maze, "E")
nodes = dict(get_nodes(maze))
score, _ = djikstra(nodes, start, end)
print(score)
