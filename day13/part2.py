def solve(equation1: tuple[int, int, int], equation2: tuple[int, int, int]):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
    y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

    return x, y


def parse_values(text: str, start_idx: int):
    x = ""
    while text[start_idx] != ",":
        x += text[start_idx]
        start_idx += 1
    while not text[start_idx].isnumeric():
        start_idx += 1

    return int(x), int(text[start_idx:])


INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as file:
    text = file.read()

tokens = 0
for machine in text.split("\n\n"):
    buttonA, buttonB, prize = machine.strip().split("\n")
    a1, a2 = parse_values(buttonA, 12)
    b1, b2 = parse_values(buttonB, 12)
    c1, c2 = parse_values(prize, 9)
    pushA, pushB = solve((a1, b1, c1 + 10000000000000), (a2, b2, c2 + 10000000000000))

    if pushA.is_integer() and pushB.is_integer():
        tokens += 3 * pushA
        tokens += pushB

print(int(tokens))
