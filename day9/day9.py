import sys

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

lines = [list(map(int, line.split(' '))) for line in raw_lines]

print(lines)

def get_diff(history):
    return [j - i for i, j in zip(history[0::], history[1::])]

total = 0
for line in lines:
    diffs = [line]
    current_diff = line
    while any(map(lambda item: item != 0, current_diff)):
        current_diff = get_diff(current_diff)
        diffs.append(current_diff)
    
    print(diffs)
    predicted = 0
    for diff in reversed(diffs[:-1]):
        predicted = diff[-1] + predicted

    total += predicted

print(total)
