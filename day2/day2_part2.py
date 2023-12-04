import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

total_power = 0
for i, line in enumerate(lines):
    line = line.split(':')[1]

    groups = line.split(';')
    failed = False
    max_dict = {}
    for group in groups:
        count_dict = {}
        draws = group.split(',')
        for draw in draws:
            draw = draw.strip()
            parts = draw.split(' ')
            key = parts[1]
            value = int(parts[0])

            max_dict[key] = max(max_dict.get(key, 0), value)

    power = 1
    for k, v in max_dict.items():
        power *= v

    total_power += power

print(total_power)
