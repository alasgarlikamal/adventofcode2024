from typing import List

INPUT_FILE = "input.txt"

puzzle: List[str] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        puzzle.append(line.strip())

DIMENSION = len(puzzle[0])


def count_words(string: str):
    curr = 0
    count = 0
    while curr <= len(string) - 4:
        word = string[curr : curr + 4]
        if word == "XMAS" or word == "SAMX":
            count += 1
            curr += 3
        else:
            curr += 1
    return count


def search_horizontal(puzzle: List[str]):
    count = 0

    for row in puzzle:
        count += count_words(row)

    return count


def search_vertical(puzzle: List[str]):
    count = 0

    for i in range(DIMENSION):
        col = ""
        for row in puzzle:
            col += row[i]
        count += count_words(col)

    return count


def search_left_diagonal(puzzle: List[str]):
    count = 0
    # Finding for top triangle
    for row_idx in range(DIMENSION):
        i = 0
        j = row_idx
        diagonal = ""
        while i < DIMENSION and j < DIMENSION:
            diagonal += puzzle[i][j]
            i += 1
            j += 1
        count += count_words(diagonal)

    # Finding for bottom triangle
    for row_idx in range(1, DIMENSION):
        i = row_idx
        j = 0
        diagonal = ""
        while i < DIMENSION and j < DIMENSION:
            diagonal += puzzle[i][j]
            i += 1
            j += 1
        count += count_words(diagonal)

    return count


def search_right_diagonal(puzzle: List[str]):
    count = 0
    # Finding for top triangle
    for row_idx in range(DIMENSION - 1, -1, -1):
        i = 0
        j = row_idx
        diagonal = ""
        while i < DIMENSION and j >= 0:
            diagonal += puzzle[i][j]
            i += 1
            j -= 1
        count += count_words(diagonal)

    # Finding for bottom triangle
    for row_idx in range(1, DIMENSION):
        i = row_idx
        j = DIMENSION - 1
        diagonal = ""
        while i < DIMENSION and j >= 0:
            diagonal += puzzle[i][j]
            i += 1
            j -= 1
        count += count_words(diagonal)

    return count


count = (
    search_horizontal(puzzle)
    + search_vertical(puzzle)
    + search_left_diagonal(puzzle)
    + search_right_diagonal(puzzle)
)

print("Count: ", count)
