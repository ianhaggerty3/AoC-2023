import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

num_list = []
symbol_list = []
size = len(lines[0])
for i, line in enumerate(lines):
    first_indexes = [j for j in range(size) if line[j].isdigit() and (j == 0 or not line[j - 1].isdigit())]
    last_indexes = [j for j in range(size) if line[j].isdigit() and (j == (size - 1) or not line[j + 1].isdigit())]
    symbols = [j for j in range(size) if line[j] != '.' and not line[j].isdigit()]
    symbol_list += list(map(lambda item: (i, item), symbols))
    num_list += list(map(lambda item: (i, item[0], item[1], int(line[item[0]:(item[1] + 1)])), zip(first_indexes, last_indexes)))

print(num_list)
print(symbol_list)

total = 0
for num in num_list:
    if any(map(lambda point: abs(point[0] - num[0]) <= 1 and point[1] in range(num[1] - 1, num[2] + 2), symbol_list)):
        total += num[3]

print(total)
