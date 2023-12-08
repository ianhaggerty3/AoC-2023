import sys
from itertools import cycle

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

instructions = lines[0]

node_map = {}
for entry in lines[2::]:
    exec(f'node_map{entry}')

currents = [node for node in node_map.keys() if node.endswith('A')]

def get_next(node, instruction):
    if instruction == 'L':
        return node_map[node][0]
    else:
        return node_map[node][1]

def get_cycle_length(original_node):
    offset_map = {}
    steps = 0
    current = original_node
    for instruction in cycle(instructions):
        current = get_next(current, instruction)
        steps += 1
        key = (current, steps % len(instructions))
        if key in offset_map:
            return steps - offset_map[key]
        offset_map[key] = steps

print([get_cycle_length(node) for node in currents])

# steps = 0
# for instruction in cycle(instructions):
#     for i in range(len(currents)):
#         currents[i] = get_next(currents[i], instruction)

#     steps += 1

#     if all(map(lambda node: node.endswith('Z'), currents)):
#         break

print('still cooking')