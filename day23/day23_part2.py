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

add_tuple = lambda a, b: tuple(map(add, a, b))

start = [(i, 0) for i in range(len(lines[0])) if lines[0][i] == '.'][0]
end = [(i, len(lines) - 2) for i in range(len(lines[0])) if lines[0][i] == '.'][0]


def get_around(node):
    ret = []

    for option in direction_map.values():
        next_node = add_tuple(node, option)

        if lines[next_node[1]][next_node[0]] != '#':
            ret.append(next_node)

    return ret

visited = set()
boundary = set([start])
junction_map = {}


# reduce map to only junctions
while len(boundary) != 0:
    start = boundary.pop()
    visited.add(start)
    for option in direction_map.values():
        found_end = False
        last = start
        current = add_tuple(start, option)
        current_token = lines[current[1]][current[0]]

        if current_token == '#' or current in visited:
            continue

        count = 1
        while not found_end:
            next_options = get_around(current)

            if len(next_options) == 1 and current == end:
                found_end = True
                continue

            if len(next_options) >= 3:
                found_end = True
                continue
            
            if len(next_options) == 2:
                next_node = [next_option for next_option in next_options if next_option != last][0]
                last = current
                current = next_node
                count += 1
        
        junction_map[start] = junction_map.get(start, []) + [(current, count)]
        if current not in visited:
            boundary.add(current)
        

print(junction_map)

