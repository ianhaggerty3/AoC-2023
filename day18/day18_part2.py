import sys
from operator import add
from random import randrange
from functools import reduce

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

direction_map = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

direction_decoder = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

add_tuple = lambda a, b: tuple(map(add, a, b))
mul_tuple = lambda a, b: tuple(map(lambda x: x * b, a))

start = (0, 0)
current = start
directions = []
magnitudes = []
# for instruction in lines:
#     _direction, _magnitude, color = instruction.split(' ')
#     direction = direction_decoder[color[-2]]
#     magnitude = int(f'0x{color[2:-2]}', 0)
#     directions.append(direction)
#     magnitudes.append(magnitude)

for instruction in lines:
    direction, magnitude, color = instruction.split(' ')
    # direction = direction_decoder[color[-2]]
    # magnitude = int(f'0x{color[2:-2]}', 0)
    directions.append(direction)
    magnitudes.append(int(magnitude))

outline = []
current = start
for direction, magnitude in zip(directions, magnitudes):
    current = add_tuple(current, mul_tuple(direction_map[direction], magnitude))
    
    outline.append(current)

vertical_lines = []
for v1, v2 in zip(outline, outline[1:]):
    if v1[0] == v2[0]:
        vertical_lines.append((v1[0], range(min(v1[1], v2[1]), max(v1[1], v2[1]) + 1)))

def is_in_polygon(p):
    lines_to_left = filter(lambda line: line[0] <= p[0] and p[1] in line[1], vertical_lines)
    return len(list(lines_to_left)) % 2 == 1

# take rectangles out of the irregular polygon
total_area = 0
while len(outline) > 4:
    index = randrange(len(outline))
    v1, v2, v3 = outline[index], outline[(index + 1) % len(outline)], outline[(index + 2) % len(outline)]

    # project new vertex
    if v1[0] == v2[0]:
        new_x = v3[0]
        new_y = v1[1]
    else:
        new_x = v1[0]
        new_y = v3[1]

    v4 = (new_x, new_y)


    if not is_in_polygon(v4):
        continue

    print(v1, v2, v3, v4)
    current_vertices = {v1, v2, v3, v4}

    x_range = range(min(v1[0], v3[0]) + 1, max(v1[0], v3[0]))
    y_range = range(min(v1[1], v3[1]) + 1, max(v1[1], v3[1]))

    if any(map(lambda point: point not in current_vertices and point[0] in x_range and point[1] in y_range, outline)):
        continue

    total_area += (len(x_range)) * (len(y_range))
    outline.remove(v2)
    outline.remove(v3)
    # conditionally do this?
    outline.insert(index + 1, v4)
    
print(total_area)
print(outline)

# through data exploration, learned that there were no squeezes
