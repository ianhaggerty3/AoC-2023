import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

columns = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]

total_load = 0
for column in columns:
    h = len(column)
    for i, token in enumerate(column):
        if token == '#':
            h = len(column) - (i + 1)
        elif token == 'O':
            total_load += h
            h -= 1

print(total_load)