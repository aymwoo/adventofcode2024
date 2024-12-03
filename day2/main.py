def read_data(file_path: str):
    with open(file_path, "r") as file:
        return [list(map(int, line.strip().split())) for line in file]


file_path = "input"


def diff(a, b):
    return a - b


def is_safe(l_row):
    cond1 = all(
        abs(diff(l_row[i], l_row[i + 1])) in [1, 2, 3] for i in range(len(l_row) - 1)
    )
    cond2 = all(l_row[i] < l_row[i + 1] for i in range(len(l_row) - 1)) or all(
        l_row[i] > l_row[i + 1] for i in range(len(l_row) - 1)
    )
    return cond1 and cond2


def part_1():
    data = read_data(file_path)
    safe_report = 0
    for l_row in data:
        # 自己写的方法尽量减少不必要的计算
        # is_increasing = True if l_row[0] < l_row[1] else False
        # for i in range(0, len(l_row) - 1):
        #     if (l_row[i] < l_row[i + 1]) != is_increasing:
        #         break
        #     diff = abs(l_row[i] - l_row[i + 1])
        #     if not (1 <= diff <= 3):
        #         break
        # else:
        #     safe_report += 1

        # 暴力解法
        if is_safe(l_row):
            safe_report += 1
    return safe_report


def part_2():
    data = read_data(file_path)
    safe_report = 0
    for row in data:
        if is_safe(row):
            safe_report += 1
        else:
            if any(is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))):
                safe_report += 1
    return safe_report


# file_path = "sample"
print(part_1())
print(part_2())
