TARGET = "XMAS"


def read_data(file_path):
    with open(file_path) as f:
        data = f.readlines()
    return data


def part_1(data):
    rows, cols = len(data), len(data[0].strip())
    result = 0
    for row in range(rows):
        result += data[row].strip().count(TARGET)
        result += data[row][::-1].strip().count(TARGET)

    for col in range(cols):
        col_data = "".join([data[row][col] for row in range(rows)])
        result += col_data.count(TARGET)
        result += col_data[::-1].count(TARGET)

    # 检查从左上到右下的斜线
    for d in range(-(rows - 1), cols):
        chars = []
        for i in range(rows):
            for j in range(cols):
                if i - j == d:
                    chars.append(data[i][j])
        line_str = "".join(chars)
        result += line_str.count(TARGET)
        result += line_str[::-1].count(TARGET)

    # 检查从右上到左下的斜线
    for d in range(1, cols + rows - 1):
        chars = []
        for i in range(rows):
            for j in range(cols):
                if i + j == d:
                    chars.append(data[i][j])
        line_str = "".join(chars)
        result += line_str.count(TARGET)
        result += line_str[::-1].count(TARGET)
    return result


def is_match(data, row, col):
    if row < 1 or col < 1 or row >= len(data) or col >= len(data[0].strip()):
        return False
    if data[row][col] != "A":
        return False
    line_1 = "".join([data[row - 1][col - 1], data[row][col], data[row + 1][col + 1]])
    line_2 = "".join([data[row - 1][col + 1], data[row][col], data[row + 1][col - 1]])
    if (line_1 == line_2 or line_1 == line_2[::-1]) and line_1 in ["MAS", "SAM"]:
        return True
    return False


def part_2(data):
    rows, cols = len(data), len(data[0].strip())
    result = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if is_match(data, row, col):
                result += 1

    return result


data = read_data("input")
print(part_1(data))
print(part_2(data))
