import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

num_list = []
gear_list = []
size = len(lines[0])
for i, line in enumerate(lines):
    first_indexes = [j for j in range(size) if line[j].isdigit() and (j == 0 or not line[j - 1].isdigit())]
    last_indexes = [j for j in range(size) if line[j].isdigit() and (j == (size - 1) or not line[j + 1].isdigit())]
    gears = [j for j in range(size) if line[j] == '*']
    gear_list += list(map(lambda item: (i, item), gears))
    num_list += list(map(lambda item: (i, item[0], item[1], int(line[item[0]:(item[1] + 1)])), zip(first_indexes, last_indexes)))

print(num_list)
print(gear_list)

total = 0
for gear in gear_list:
    in_range_list = list(filter(lambda num: abs(gear[0] - num[0]) <= 1 and gear[1] in range(num[1] - 1, num[2] + 2), num_list))
    if len(in_range_list) == 2:
        total += (in_range_list[0][3] * in_range_list[1][3])

print(total)
