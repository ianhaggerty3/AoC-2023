import sys

max_vals = {
        'red': 12,
        'green': 13,
        'blue': 14
}

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

total = 0
for i, line in enumerate(lines):
    line = line.split(':')[1]

    groups = line.split(';')
    failed = False
    for group in groups:
        count_dict = {}
        draws = group.split(',')
        for draw in draws:
            draw = draw.strip()
            parts = draw.split(' ')
            key = parts[1]
            value = int(parts[0])

            count_dict[key] = count_dict.get(key, 0) + value

        if any(map(lambda pair: pair[1] < count_dict.get(pair[0], 0),
            max_vals.items())):
            failed = True
    if not failed:
        total += (i + 1)

print(total)
