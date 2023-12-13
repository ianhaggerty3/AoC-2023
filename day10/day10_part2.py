import sys
from operator import add
from functools import reduce

symbol_dict = {
    '|': {'N': 'S', 'S': 'N'},
    '-': {'E': 'W', 'W': 'E'},
    'L': {'N': 'E', 'E': 'N'},
    'J': {'N': 'W', 'W': 'N'},
    '7': {'W': 'S', 'S': 'W'},
    'F': {'E': 'S', 'S': 'E'},
    'S': {},
    '.': {}
}

inside_edge_dict = {
    '|': {'E': 'E', 'W': 'W'},
    '-': {'N': 'N', 'S': 'S'},
    # wrong
    'L': {'E': 'N', 'N': 'E', 'W': 'S', 'S': 'W'},
    'J': {'W': 'N', 'N': 'W', 'E': 'S', 'S': 'E'},
    '7': {'W': 'S', 'S': 'W', 'E': 'N', 'N': 'E'},
    'F': {'E': 'S', 'S': 'E', 'W': 'N', 'N': 'W'},
    'S': {},
    '.': {}
}

direction_dict = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
}

reverse_direction_dict = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W',
}

add_tuple = lambda a, b: tuple(map(add, a, b))

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

start = (0, 0)
for i, line in enumerate(raw_lines):
    result = line.find('S')
    if result != -1:
        start = (result, i)
        break

raw_lines[start[1]] = raw_lines[start[1]].replace('S', 'L')
pipe_map = [[symbol_dict[symbol] for symbol in line] for i, line in enumerate(raw_lines)]
inside_edge_map = [[inside_edge_dict[symbol] for j, symbol in enumerate(line)] for i, line in enumerate(raw_lines)]
all_tiles = reduce(lambda a, b: a.union(b), [{(j, i) for j, symbol in enumerate(line)} for i, line in enumerate(raw_lines)])


perpendicular_directions = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

def get_circular_path(starting_direction):
    ret_path = {}
    perpendicular_direction = perpendicular_directions[starting_direction]
    # if you start by moving north, you entered the first pipe from the south
    current_direction = reverse_direction_dict[starting_direction]
    current_pos = add_tuple(start, direction_dict[starting_direction])

    # print(current_pos)
    while current_pos not in ret_path:
        if current_direction not in pipe_map[current_pos[1]][current_pos[0]]:
            return None

        exit_direction = pipe_map[current_pos[1]][current_pos[0]][current_direction]
        perpendicular_direction = inside_edge_map[current_pos[1]][current_pos[0]][perpendicular_direction]
        # at bends, there are two inner edge directions
        ret_path[current_pos] = set([perpendicular_direction, inside_edge_map[current_pos[1]][current_pos[0]][perpendicular_direction]])
        if current_pos == start:
            break
        current_pos = add_tuple(current_pos, direction_dict[exit_direction])
        current_direction = reverse_direction_dict[exit_direction]
        
    # L
    # perpendicular_direction = inside_edge_dict['L'][perpendicular_direction]
    # ret_path[start] = set([perpendicular_direction, inside_edge_dict['L'][perpendicular_direction]])
    return ret_path

def check_valid_inner_assumption(path):
    for coords, directions in path.items():
        if raw_lines[coords[1]][coords[0]] == '|' and 'W' in directions:
            starting_coords = coords
            break
    
    diff = (-1, 0)
    current_coords = starting_coords
    while current_coords[0] > 0:
        current_coords = add_tuple(diff, current_coords)
        if current_coords in path:
            if 'E' in path[current_coords]:
                return True
            else:
                return False
    
    return False


for starting_direction in {'N', 'S', 'E', 'W'}:
    path = get_circular_path(starting_direction)
    if path is None:
        continue
    
    if not check_valid_inner_assumption(path):
        perpendicular_directions = {v: k for k, v in perpendicular_directions.items()}
        path = get_circular_path(starting_direction)
        print(check_valid_inner_assumption(path))

    print(starting_direction)
    break

# print(start)
# print(path[0])
# print(path[-1])

diff = (-1, 0)
total = 0
for tile in all_tiles:
    if tile in path:
        continue
    current_coords = tile
    while current_coords[0] > 0:
        current_coords = add_tuple(diff, current_coords)
        if current_coords in path:
            if 'E' in path[current_coords]:
                total += 1
            break

print(total)


# print(max(moves_tracker) // 2)