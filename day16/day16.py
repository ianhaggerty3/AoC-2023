import sys
from operator import add

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

direction_map = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

mirror_map = {
    '/': {
        'N': 'E',
        'E': 'N',
        'S': 'W',
        'W': 'S'
    },
    '\\': {
      'N': 'W',
      'W': 'N',
      'S': 'E',
      'E': 'S',
    }
}

splitter_map = {
    '-': {'N': {'E', 'W'}, 'S': {'E', 'W'}},
    '|': {'E': {'N', 'S'}, 'W': {'N', 'S'}}
}

start = (-1, 0)
direction = 'E'

energized_tiles = set()
add_tuple = lambda a, b: tuple(map(add, a, b))

def simulate_beam(start, direction, energized_tiles, cave):
    current = start
    while True:
        current = add_tuple(current, direction_map[direction])
        if current[0] < 0 or current[0] >= len(cave[0]) or current[1] < 0 or current[1] >= len(cave):
            return

        if (current, direction) in energized_tiles:
            return
        energized_tiles.add((current, direction))
        tile = cave[current[1]][current[0]]
        if tile in mirror_map:
            direction = mirror_map[tile][direction]
        elif tile in splitter_map:
            if direction in splitter_map[tile]:
                [simulate_beam(current, new_direction, energized_tiles, cave) for new_direction in splitter_map[tile][direction]]
                return

simulate_beam(start, direction, energized_tiles, lines)

unique_energized_tiles = {tile[0] for tile in energized_tiles}

# for j in range(len(lines)):
#     cave_string = ['#' if (i, j) in unique_energized_tiles else '.' for i in range(len(lines[0]))]
#     print(''.join(cave_string))

print(len(unique_energized_tiles))
# print(min(map(lambda x: x[0], unique_energized_tiles)))
# print(max(map(lambda x: x[0], unique_energized_tiles)))
# print(min(map(lambda x: x[1], unique_energized_tiles)))
# print(max(map(lambda x: x[1], unique_energized_tiles)))