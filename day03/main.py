INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as f:
    text = f.read()

curr = 0
sum = 0
enabled = True

while curr < len(text) - 4:

    while text[curr : curr + 4] != "mul(":
        if text[curr : curr + 4] == "do()":
            enabled = True

        if curr <= len(text) - 7 and text[curr : curr + 7] == "don't()":
            enabled = False
        curr += 1

    curr = curr + 4
    iter = 0

    while (
        iter < 7 and text[curr] != ")" and (text[curr].isdigit() or text[curr] == ",")
    ):
        curr += 1
        iter += 1

    if text[curr] == ")" and enabled:
        nums = list(map(int, text[curr - iter : curr].split(",")))
        if len(nums) == 2:
            num1, num2 = nums
            sum += num1 * num2

print("Sum:", sum)
