import sys
from itertools import cycle, islice
from math import gcd

def get_next(node, instruction):
    if instruction == 'L':
        return node_map[node][0]
    else:
        return node_map[node][1]

def get_cycle_info(original_node):
    offset_map = {}
    steps = 0
    current = original_node
    offset_map[(current, 0)] = 0
    for instruction in cycle(instructions):
        current = get_next(current, instruction)
        steps += 1
        key = (current, steps % len(instructions))
        if key in offset_map:
            print(key[0], offset_map[key], steps - offset_map[key])
            return key[0], offset_map[key], steps - offset_map[key]
        offset_map[key] = steps

def get_end_states(key, start, length):
    current = key

    ret = set()

    choices = islice(cycle(instructions), start, None)
    for instruction, i in zip(choices, range(start, start + length)):
        if current.endswith('Z'):
            ret.add(i)
        current = get_next(current, instruction)
    
    return ret

def combine_cycles(a, b):
    c1, l1 = a
    c2, l2 = b
    total_cycle = gcd(l1, l2)
    all_a = {c1 + l1 * i for i in range(l2 // total_cycle)}
    all_b = {c2 + l2 * i for i in range(l1 // total_cycle)}
    intersection = all_a.intersection(all_b).pop()

    return (intersection, (l1 * l2) // total_cycle)

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

instructions = lines[0]

node_map = {}
for entry in lines[2::]:
    exec(f'node_map{entry}')

currents = [node for node in node_map.keys() if node.endswith('A')]

cycle_info = [get_cycle_info(node) for node in currents]
final_sets = [get_end_states(item[0], item[1], item[2]) for item in cycle_info]
offset_and_length = [(info[2], info[2]) for info in cycle_info]

while len(offset_and_length) > 1:
    a = offset_and_length.pop(0)
    b = offset_and_length.pop(0)
    offset_and_length.append(combine_cycles(a, b))

print(offset_and_length.pop())

