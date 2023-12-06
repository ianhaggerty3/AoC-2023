import sys

def reverse_dict(dict):
    return {v: k for k, v in dict.items()}

def get_seed_location(seed, lookup_list):
    current_i = seed
    for lookup in lookup_list:
        new_i = None
        for span, dest in lookup.items():
            if current_i in span:
                new_i = dest + (current_i - span.start)
                break
        
        if new_i is None:
            new_i = current_i
        
        current_i = new_i

    return current_i

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

initial_seeds = list(map(int, raw_lines[0].split(':')[1].strip().split(' ')))

map_lines = raw_lines[2::]

lookup_list = []
while len(map_lines) != 0:
    current_lookup = {}
    current_line = map_lines.pop(0)
    while len(current_line) != 0:
        if ':' in current_line:
            current_line = map_lines.pop(0)
            continue
        parts = list(map(int, current_line.split(' ')))
        current_lookup[range(parts[1], parts[1] + parts[2])] = parts[0]
        current_line = map_lines.pop(0)

    lookup_list.append(current_lookup)

seed_locations = list(map(lambda seed: get_seed_location(seed, lookup_list), initial_seeds))
print(seed_locations)
print(f'min location = {min(seed_locations)}')
