from functools import reduce
from operator import add
import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

width = len(lines[0])
height = len(lines)
print(width, height)
rocks = reduce(lambda a, b: a | b, [{(x, y) for x, token in enumerate(line) if token == '#'} for y, line in enumerate(lines)])

for y, line in enumerate(lines):
    x = line.find('S')
    if x != -1:
        break

start = (x, y)

directions = {
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
}
add_tuple = lambda a, b: tuple(map(add, a, b))

seen = set()

def is_final(state):
    return state[1] == 64

options = {(start, 0)}

def check_original(steps):
    total = 0
    for x in range(width):
        for y in range(height):
            if ((x, y), steps) in seen:
                total += 1
    
    return total

while len(options) != 0:
    current_node, steps = options.pop()
    seen.add((current_node, steps))
    if is_final((current_node, steps)):
        continue

    for direction in directions:
        next_node = add_tuple(current_node, direction)
        if (next_node, steps + 1) in seen or (next_node[0] % width, next_node[1] % height) in rocks:
            continue
        
        options.add((next_node, steps + 1))



print(check_original(191))
print(check_original(192))
print(check_original(193))


print(len(list(filter(lambda item: is_final(item), seen))))
