INPUT_FILE = "input.txt"


disk_map = ""
with open(INPUT_FILE, "r") as file:
    disk_map = file.readline().strip()

disk: list[str] = []
id = 0
for idx, num in enumerate(disk_map):
    if idx % 2 == 0:  # File
        disk.extend([str(id)] * int(num))
        id += 1
    else:  # Empty space
        disk.extend(["."] * int(num))


def find_free_space(disk: list[str], length: int, last_idx: int) -> int | None:
    curr = 0
    while curr < last_idx:
        while disk[curr] != ".":
            curr += 1

        found_length = 0
        while disk[curr] == "." and curr < last_idx:
            curr += 1
            found_length += 1
            if found_length == length:
                return curr - found_length
    return None


curr = len(disk) - 1
while curr >= 0:
    length = 0
    current_num = disk[curr]
    while disk[curr] == current_num:
        curr -= 1
        length += 1

    num_len = len(disk[curr + 1])

    if free_space_index := find_free_space(disk, length, curr + 1):
        for i in range(length):
            disk[free_space_index + i] = disk[curr + 1]

        for i in range(length):
            disk[curr + 1 + i] = "."

    while disk[curr] == "." or disk[curr] == current_num:
        curr -= 1

sum = 0

for idx, num in enumerate(disk):
    if num.isnumeric():
        sum += idx * int(num)

print(sum)
