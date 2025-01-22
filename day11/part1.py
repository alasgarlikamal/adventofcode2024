INPUT_FILE = "input.txt"


with open(INPUT_FILE, "r") as file:
    nums = [int(x) for x in file.read().split()]


def blink(num: int) -> list[int]:

    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        num1 = str(num)[: (len(str(num)) // 2)]
        num2 = str(num)[(len(str(num)) // 2) :]
        return [int(num1), int(num2)]

    return [num * 2024]


for _ in range(25):
    new_nums = []
    for num in nums:
        new_nums.extend(blink(num))

    nums = new_nums


print(len(nums))
