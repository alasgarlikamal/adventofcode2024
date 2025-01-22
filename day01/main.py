from typing import List

INPUT_FILE = "input.txt"

list1: List[int] = []
list2: List[int] = []


def insert_ascending(list: List[int], value):
    for idx, num in enumerate(list):
        if num > value:
            list.insert(idx, value)
            return

    list.append(value)


with open(INPUT_FILE, "r") as file:
    for line in file:
        nums = line.split("   ")
        insert_ascending(list1, int(nums[0]))
        insert_ascending(list2, int(nums[1]))

total_distance = 0

for num1, num2 in zip(list1, list2):
    total_distance += abs(num1 - num2)

print("Total distance:", total_distance)

similarity_score = 0

idx = 0
for num1 in list1:
    count = 0
    for i in range(idx, len(list2)):
        if list2[i] > num1:
            idx = i
            break
        if list2[i] == num1:
            count += 1
    similarity_score += count * num1

print("Similarity score:", similarity_score)
