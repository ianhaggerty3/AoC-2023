import sys
from functools import reduce
from operator import mul
from copy import deepcopy

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

workflows = {}

def get_new_ranges(ranges, current_target, new_target, operator, property, comparison):
    relevant_value = ranges[property]
    first_new_ranges = deepcopy(ranges)
    second_new_ranges = deepcopy(ranges)
    if operator == '<':
        first_new_ranges[property] = range(relevant_value.start, min(comparison, relevant_value.stop))
        second_new_ranges[property] = range(max(relevant_value.start, comparison), relevant_value.stop)
        return [(first_new_ranges, new_target), (second_new_ranges, current_target)]
    else:
        first_new_ranges[property] = range(relevant_value.start, min(comparison + 1, relevant_value.stop))
        second_new_ranges[property] = range(max(relevant_value.start, comparison + 1), relevant_value.stop)
        return [(first_new_ranges, current_target), (second_new_ranges, new_target)]

def get_rule(rule):
    parts = rule.split(':')
    if len(parts) == 2:
        condition = rule.split(':')[0]
        new_target = rule.split(':')[1]
        callback = lambda ranges, target: get_new_ranges(ranges, target, new_target, condition[1], condition[0], int(condition[2:]))
    else:
        callback = lambda ranges, target: [(ranges, parts[0])]

    return callback

for i, line in enumerate(lines):
    if len(line) == 0:
        break
    name = line.split("{")[0]
    rules = line.split("{")[1][:-1]

    workflow = [get_rule(rule) for rule in rules.split(',')]
    workflows[name] = workflow

full_ranges = {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)}
def get_all_parts(current, ranges):
    if current == 'R':
        return 0
    if current == 'A':
        return reduce(mul, map(len, ranges.values()))

    workflow = workflows[current]
    total = 0
    for rule in workflow:
        for new_ranges, new_target in rule(ranges, current):
            if new_target != current and all(map(lambda span: len(span) != 0, new_ranges)):
                total += get_all_parts(new_target, new_ranges)
            elif new_target == current:
                ranges = new_ranges

    return total

total = get_all_parts("in", full_ranges)
print(total)