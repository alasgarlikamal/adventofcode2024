INPUT_FILE = "input.txt"


disk_map = ""
with open(INPUT_FILE, "r") as file:
    disk_map = file.readline().strip()

output: list[str] = []
id = 0
for idx, num in enumerate(disk_map):
    if idx % 2 == 0:  # File
        output.extend([str(id)] * int(num))
        id += 1
    else:  # Empty space
        output.extend(["."] * int(num))

r, l = 0, len(output) - 1

while r < l:
    while output[r] != ".":
        r += 1
    if output[l] == ".":
        while output[l] == ".":
            l -= 1
    else:
        output[r] = output[l]
        output[l] = "."

sum = 0
for idx, num in enumerate(output):
    if num == ".":
        break
    sum += idx * int(num)

print("File system checksum:", sum)
