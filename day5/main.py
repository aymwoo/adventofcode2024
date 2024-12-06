from icecream import ic

ic.disable()


def read_rules(file_path):
    rules = {}
    data = []
    is_rule = True
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            print(line)
            if line == "":
                is_rule = False
                continue
            if is_rule:
                parts = line.split("|")
                page_1 = int(parts[0])
                page_2 = int(parts[1])

                rules[page_1] = rules.get(page_1, []) + [page_2]
                ic(page_1, page_2)
                ic(rules[page_1])
            else:
                data.append([int(x) for x in line.split(",")])
    return rules, data


def is_correct(page, index, row):
    for p in row[index + 1 :]:
        if page in rules.get(p, []):
            return False
    else:
        return True


def fix(page, index, row, rules):
    before = row[:index]
    after = row[index + 1 :]
    for n in after:
        if page in rules.get(n, []):
            before.append(n)
            after.remove(n)
            break

    return before + [page] + after


def fix_row(row, rules):
    while True:
        for index, page in enumerate(row):
            if not is_correct(page, index, row):
                row = fix(page, index, row, rules)
                break
        else:
            break
    return row


def part_1(rules, data):
    ic(rules)
    ic(data)
    result = 0
    for row in data:
        for index, page in enumerate(row):
            if not is_correct(page, index, row):
                break
        else:
            result += row[len(row) // 2]

    return result


def part_2(rules, data):
    result = 0
    is_fixed = False
    for row in data:
        ic(row)
        for index, page in enumerate(row):
            if not is_correct(page, index, row):
                row = fix_row(row, rules)
                is_fixed = True
        if is_fixed:
            result += row[len(row) // 2]
            ic(row)
            is_fixed = False

    return result


rules, data = read_rules("input")
print(part_1(rules, data))
print(part_2(rules, data))
