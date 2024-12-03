from typing import List, Tuple


def read_input(file_path: str) -> Tuple[List[int], List[int]]:
    column_left = []
    column_right = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split()
            column_left.append(int(values[0]))
            column_right.append(int(values[1]))
    return column_left, column_right


def part_1():
    list_left, list_right = read_input("input")
    list_left_sorted = sorted(list_left)
    list_right_sorted = sorted(list_right)
    distance = 0
    for i in range(len(list_left)):
        distance += abs(list_left_sorted[i] - list_right_sorted[i])
    return distance


def part_2():
    list_left, list_right = read_input("input")
    result = 0
    for n in list_left:
        result += n * list_right.count(n)
    return result


print(part_1())
print(part_2())
