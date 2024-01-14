import sys
from copy import copy
from operator import add

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]


direction_map = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

slope_map = {
    '>': 'E',
    '<': 'W',
    '^': 'N',
    'v': 'S',
}

add_tuple = lambda a, b: tuple(map(add, a, b))

start = [(i, 0) for i in range(len(lines[0])) if lines[0][i] == '.'][0]
print(start)

results = []

def traverse_path(start, visited):
    current = start
    current_token = lines[start[1]][start[0]]

    while current_token != None:
        if current_token in slope_map.keys():
            coord = add_tuple(current, direction_map[slope_map[current_token]])
            options = [coord] if coord not in visited else []
        else:
            options = []
            for option in direction_map.values():
                coord = add_tuple(current, option)
                token = lines[coord[1]][coord[0]]
                if token != '#' and coord not in visited:
                    options.append(coord)

        visited.add(current)
        for option in options[1::]:
            traverse_path(option, copy(visited))
        
        last = current
        current = options[0] if len(options) > 0 else None
        current_token = lines[current[1]][current[0]] if current is not None else None
        
    if last[1] == len(lines) - 2:
        results.append(len(visited))

traverse_path(add_tuple(start, direction_map['S']), set([start]))

print(max(results) - 1)