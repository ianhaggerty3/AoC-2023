import sys
from collections import deque
from copy import copy

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

def get_combinations(sequence, strips):
    if len(strips) == 0:
        if sequence.find('#') == -1:
            return 1
        else:
            return 0

    if sum(strips) + len(strips) - 1 > len(sequence):
        return 0

    relevant_strip = strips[0]
    total = 0

    window = deque(['.'] * relevant_strip)
    # loop for patterns in the middle of the sequence
    for i, token in enumerate(sequence):
        if (token == '.' or token == '?') and not any(map(lambda item: item == '.', window)):
            total += get_combinations(sequence[(i + 1)::], strips[1::])

        if window[-1] == '#':
            break
        window.rotate(1)
        window[0] = token

    # loop (lol) for patterns at the end of the sequence
    window = deque(['.'] * relevant_strip)
    for i, token in enumerate(sequence):
        if window[-1] == '#':
            break
        window.rotate(1)
        window[0] = token
        if (i == len(sequence) - 1) and not any(map(lambda item: item == '.', window)):
            if len(strips) == 1:
                total += 1
            # total += get_combinations(sequence[(i + 1)::], strips[1::])

    return total



total = 0
# for line in [raw_lines[5]]:
for line in raw_lines:
    folded_sequence, raw_strips = line.split(' ')
    folded_strips = list(map(int, raw_strips.split(',')))
    sequence = '?'.join([folded_sequence] * 5)
    strips = folded_strips * 5
    total += get_combinations(sequence, strips)

print(total)