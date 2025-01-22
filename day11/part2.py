INPUT_FILE = "input.txt"


with open(INPUT_FILE, "r") as file:
    nums = {int(x): 1 for x in file.read().split()}


def blink(num: int) -> list[int]:

    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        num1 = str(num)[: (len(str(num)) // 2)]
        num2 = str(num)[(len(str(num)) // 2) :]
        return [int(num1), int(num2)]

    return [num * 2024]


def update_nums(nums: dict[int, int]):
    new_nums = {}
    for num in nums.keys():
        stones = blink(num)
        for stone in stones:
            if new_nums.get(stone) is None:
                new_nums[stone] = 0
            new_nums[stone] += nums[num]

    return new_nums


for _ in range(75):
    nums = update_nums(nums)


print(sum(nums.values()))
