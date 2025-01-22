INPUT_FILE = "input.txt"

protocols: dict[int, list[int]] = {}
updates: list[list[int]] = []


def add_ascending(arr: list[int], value: int):
    curr = 0
    while curr < len(arr) and value > arr[curr]:
        curr += 1
    arr.insert(curr, value)


with open(INPUT_FILE, "r") as file:

    flag = "protocols"
    for line in file:
        line = line.strip()
        if line == "":
            flag = "updates"
            continue

        if flag == "protocols":
            line = list(map(int, line.split("|")))
            if match := protocols.get(line[0]):
                add_ascending(match, line[1])
            else:
                protocols[line[0]] = [line[1]]
            continue

        if flag == "updates":
            updates.append(list(map(int, line.split(","))))


def binary_search(haystack: list[int], needle: int) -> bool:
    low = 0
    high = len(haystack)

    while high > low:
        mid = (low + high) // 2
        if haystack[mid] < needle:
            low = mid + 1
        elif haystack[mid] > needle:
            high = mid
        elif haystack[mid] == needle:
            return True

    return False


def sort_update(update: list[int], idx1: int, idx2: int):
    sorted = False
    while not sorted:
        (followed, idx1, idx2) = rules_followed(update)
        update[idx1], update[idx2] = update[idx2], update[idx1]
        sorted = followed


def rules_followed(update: list[int]) -> tuple[bool, int, int]:
    for idx1, value in enumerate(update):
        if haystack := protocols.get(value):
            needles = update[:idx1]
            for idx2, needle in enumerate(needles):
                if binary_search(haystack, needle):
                    return (False, idx1, idx2)

    return (True, 0, 0)


correct_sum = 0
incorrect_sum = 0
for update in updates:

    (followed, idx1, idx2) = rules_followed(update)

    if not followed:
        sort_update(update, idx1, idx2)
        incorrect_sum += update[len(update) // 2]
    else:
        correct_sum += update[len(update) // 2]


print("Correctly-ordered updates sum:", correct_sum)
print("Incorrectly-ordered updates sum:", incorrect_sum)
