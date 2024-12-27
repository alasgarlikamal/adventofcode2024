from itertools import product

INPUT_FILE = "input.txt"
entries: list[tuple[int, list[int]]] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        num, nums = line.strip().split(": ")
        target = int(num)
        nums = list(map(int, nums.split()))
        entries.append((target, nums))


def get_combinations(length: int):
    yield from product(*(["*+|"] * length))


def check_calibration(entry: tuple[int, list[int]]) -> bool:
    target, nums = entry

    for combination in get_combinations(len(nums) - 1):
        operands = "".join(combination)
        curr = nums[0]
        for idx, op in enumerate(operands):
            if op == "+":
                curr += nums[idx + 1]
            if op == "*":
                curr *= nums[idx + 1]
            if op == "|":
                curr = int(str(curr) + str(nums[idx + 1]))

        if curr == target:
            return True

    return False


result = 0
for entry in entries:
    if check_calibration(entry):
        result += entry[0]

print(result)
