def read_bytes():
    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.strip().split(",")
            yield int(x), int(y)


def reachable(memory):

    def filter_nodes(node: tuple[int, int]):
        x, y = node

        if x < 0 or x >= MEMORY_LENGTH or y < 0 or y >= MEMORY_LENGTH:
            return False

        return memory[y][x] != "#"

    queue = [(0, 0)]
    visited = []
    while len(queue) > 0:
        x, y = queue.pop(0)
        top = (x, y - 1)
        bottom = (x, y + 1)
        left = (x - 1, y)
        right = (x + 1, y)
        for adjacent in filter(filter_nodes, [top, bottom, left, right]):
            if adjacent not in visited:
                if adjacent == (MEMORY_LENGTH - 1, MEMORY_LENGTH - 1):
                    return True
                visited.append(adjacent)
                queue.append(adjacent)

    return False


def create_memory(n: int):
    memory = [["." for i in range(MEMORY_LENGTH)] for i in range(MEMORY_LENGTH)]

    for i in range(n):
        x, y = bytes[i]
        memory[y][x] = "#"

    return memory


MEMORY_LENGTH = 71
BYTES_TO_READ = 1024
bytes = list(read_bytes())
low = BYTES_TO_READ
high = len(bytes) - 1

while low < high:
    mid = (high + low) // 2
    memory1 = create_memory(mid)
    memory2 = create_memory(mid - 1)

    if not reachable(memory1) and reachable(memory2):
        print(bytes[mid - 1])
        break
    elif reachable(memory1) and reachable(memory2):
        low = mid + 1
    else:
        high = mid
