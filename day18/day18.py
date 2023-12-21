import sys
from operator import add

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

direction_map = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

add_tuple = lambda a, b: tuple(map(add, a, b))
mul_tuple = lambda a, b: tuple(map(lambda x: x * b, a))

start = (0, 0)
current = start
outline = set()
for instruction in lines:
    direction, magnitude, _color = instruction.split(' ')
    for i in range(int(magnitude)):
        current = add_tuple(current, direction_map[direction])
        outline.add(current)

min_x = min(map(lambda item: item[0], outline))
max_x = max(map(lambda item: item[0], outline))
min_y = min(map(lambda item: item[1], outline))
max_y = max(map(lambda item: item[1], outline))

min_x_items = {item for item in outline if item[0] == min_x}

for item in min_x_items:
    inside_point = add_tuple(item, (1, 0))
    if inside_point not in outline:
        break


options = {inside_point}
inside = set()

while len(options) != 0:
    option = options.pop()
    for direction in direction_map.values():
        neighbor = add_tuple(option, direction)
        if neighbor not in inside and neighbor not in outline:
            options.add(neighbor)
    
    inside.add(option)

# through data exploration, learned that there were no squeezes

# for y in range(min_y, max_y + 1):
#     trench_string = ''.join(['#' if (x, y) in outline else '.' for x in range(min_x, max_x + 1)])
#     print(trench_string)

# print()
# inside = set()
# for i in range(min_x, max_x + 1):
#     for j in range(min_y, max_y + 1):
#         current = (i, j)
#         diff = (-1, 0)
#         count = 0

#         last_was_trench = False

#         while current[0] >= min_x:
#             if current in outline and last_was_trench is False:
#                 count += 1
#                 last_was_trench = True
#             elif current not in outline:
#                 last_was_trench = False
#             current = add_tuple(current, diff)
        
#         if count % 2 == 1:
#             inside.add((i, j))

full = outline | inside

# for y in range(min_y, max_y + 1):
#     trench_string = ''.join(['#' if (x, y) in full else '.' for x in range(min_x, max_x + 1)])
#     print(trench_string)

print(len(outline | inside))
