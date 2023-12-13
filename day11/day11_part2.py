import sys
from functools import reduce
from itertools import combinations

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

width = len(raw_lines[0])
height = len(raw_lines)

galaxies = reduce(lambda a, b: a.union(b), [{(j, i) for j, symbol in enumerate(line) if symbol == '#'} for i, line in enumerate(raw_lines)])
no_warp_cols = {i[0] for i in galaxies}
no_warp_rows = {i[1] for i in galaxies}

total = 0
for a, b in combinations(galaxies, 2):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    x_min = min(b[0], a[0])
    y_min = min(b[1], a[1])
    x_range = range(x_min, x_min + x_diff)
    y_range = range(y_min, y_min + y_diff)
    x_dist = x_diff + (999999 * len({i for i in x_range if i not in no_warp_cols}))
    y_dist = y_diff + (999999 * len({i for i in y_range if i not in no_warp_rows}))
    total += x_dist + y_dist

print(total)
