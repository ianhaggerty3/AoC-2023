import sys
from operator import add

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

pipe_map = [[symbol_dict[symbol] for j, symbol in enumerate(line)] for i, line in enumerate(raw_lines)]

start = (0, 0)
for i, line in enumerate(raw_lines):
    result = line.find('S')
    if result != -1:
        start = (result, i)
        break


moves_tracker = []
for starting_direction in {'N', 'S', 'E', 'W'}:
    # if you start by moving north, you entered the first pipe from the south
    current_direction = reverse_direction_dict[starting_direction]
    current_pos = add_tuple(start, direction_dict[starting_direction])
    moves = 1
    print(current_pos)
    while current_pos != start:
        if current_direction not in pipe_map[current_pos[1]][current_pos[0]]:
            print(f'invalid starting direction {starting_direction}')
            break

        
        exit_direction = pipe_map[current_pos[1]][current_pos[0]][current_direction]
        current_pos = add_tuple(current_pos, direction_dict[exit_direction])
        current_direction = reverse_direction_dict[exit_direction]
        moves += 1
    
    moves_tracker.append(moves)
    
print(max(moves_tracker) // 2)