import sys
from itertools import cycle, islice
from functools import reduce
from math import gcd
import math
from operator import mul


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

def get_cycle_info(original_node):
    offset_map = {}
    steps = 0
    current = original_node
    for instruction in cycle(instructions):
        current = get_next(current, instruction)
        steps += 1
        key = (current, steps % len(instructions))
        if key in offset_map:
            return key[0], offset_map[key], steps - offset_map[key]
        offset_map[key] = steps

cycle_info = [get_cycle_info(node) for node in currents]
lengths = [item[2] for item in cycle_info]
print(lengths)
overall_cycle = reduce(mul, lengths) // reduce(gcd, lengths)

def get_end_states(key, start, length):
    current = key

    ret = set()

    choices = islice(cycle(instructions), start, None)
    for instruction, i in zip(choices, range(start, start + length)):
        if current.endswith('Z'):
            ret.add(i)
        current = get_next(current, instruction)
    
    return ret

final_sets = [get_end_states(item[0], item[1], item[2]) for item in cycle_info]

def expand_set(final_set, length, count):
    ret = set()
    for number in final_set:
        for i in range(count):
            ret.add(number + i * length)
    
    return ret

print(overall_cycle)

expanded_final_sets = [expand_set(item[0], item[1], overall_cycle // item[1]) for item in zip(final_sets, lengths)]

print(expanded_final_sets)

valid_final_combos = reduce(lambda a, b: a.intersection(b), expanded_final_sets)
print(min(valid_final_combos))