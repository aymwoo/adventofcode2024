import re


def read_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data


def part_1(data):
    result = 0
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, data)
    for match in matches:
        result += int(match[0]) * int(match[1])

    return result


def part_2(data):
    pattern_clear = r"don\'t\(\).*?do\(\)"
    new_data = re.sub(pattern_clear, "don't()do()", data, flags=re.DOTALL)
    # 处理don't()到行尾的内容
    pattern_clear = r"don\'t\(\)(?:(?!do\(\)).)*$"
    new_data = re.sub(pattern_clear, "don't()do()", new_data, flags=re.DOTALL)

    return part_1(new_data)


# file_path = "sample"
file_path = "input"
data = read_data(file_path)

print(part_1(data))
print(part_2(data))
