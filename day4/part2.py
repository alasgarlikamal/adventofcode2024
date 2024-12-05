from typing import List

INPUT_FILE = "input.txt"

puzzle: List[str] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        puzzle.append(line.strip())

DIMENSION = len(puzzle[0])


def count_words(string: str, last_coord: tuple[int, int]):
    i, j = last_coord
    if i <= j:
        triangle = "top"
    else:
        triangle = "bottom"
    curr = 0
    count = 0
    while curr <= len(string) - 3:
        word = string[curr : curr + 3]
        if word == "MAS" or word == "SAM":
            if triangle == "top":
                i_A = curr + 1
                j_A = curr + 1 + (j - i)
            else:
                j_A = curr + 1
                i_A = curr + 1 + (i - j)
            cross = puzzle[i_A - 1][j_A + 1] + "A" + puzzle[i_A + 1][j_A - 1]
            if cross == "MAS" or cross == "SAM":
                count += 1
                curr += 1
            else:
                curr += 1
        else:
            curr += 1
    return count


def search_left_diagonal(puzzle: List[str]):
    count = 0
    # Finding for top triangle
    for row_idx in range(DIMENSION - 2):
        i = 0
        j = row_idx
        diagonal = ""
        while i < DIMENSION and j < DIMENSION:
            diagonal += puzzle[i][j]
            i += 1
            j += 1
        count += count_words(diagonal, (i, j))

    # Finding for bottom triangle
    for row_idx in range(1, DIMENSION - 2):
        i = row_idx
        j = 0
        diagonal = ""
        while i < DIMENSION and j < DIMENSION:
            diagonal += puzzle[i][j]
            i += 1
            j += 1
        count += count_words(diagonal, (i, j))

    return count


print("Count:", search_left_diagonal(puzzle))
