import sys

def reverse_dict(dict):
    return {v: k for k, v in dict.items()}

def merge_lookups(map1, map2):
    new_map = {}
    # need to incorporate dest into algorithm and transform indices
    for span1, dest in map1.items():
        diff = dest - span1.start
        overlap = filter(lambda span2: (span2[0].start < span1.stop and span2[0].stop > span1.start), map2.items())
        rangelist = sum(map(lambda span: [span.start, span.stop - 1], overlap))
        if rangelist[0] <= span1.start:
            rangelist[0] = span1.start
        else:
            rangelist.insert(0, span1.start)
        
        if rangelist[-1] >= (span1.stop - 1):
            rangelist[-1] = (span1.stop - 1)
        else:
            rangelist.append(span1.stop - 1)

        for i, j in zip(rangelist[0::], rangelist[1::]):
            new_map[range(i, j + 1)] = 0 # need to preserve original dest :/
test = range(3)


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

initial_seed_ranges = list(map(int, raw_lines[0].split(':')[1].strip().split(' ')))

initial_seeds = []
for start, length in zip(initial_seed_ranges[0::2], initial_seed_ranges[1::2]):
    initial_seeds.append(range(start, start + length))

print(initial_seeds)

map_lines = raw_lines[2::]

# lookup_list = []
# while len(map_lines) != 0:
#     current_lookup = {}
#     current_line = map_lines.pop(0)
#     while len(current_line) != 0:
#         if ':' in current_line:
#             current_line = map_lines.pop(0)
#             continue
#         parts = list(map(int, current_line.split(' ')))
#         current_lookup[range(parts[1], parts[1] + parts[2])] = parts[0]
#         current_line = map_lines.pop(0)

#     lookup_list.append(current_lookup)

# seed_locations = list(map(lambda seed: get_seed_location(seed, lookup_list), initial_seeds))
# print(seed_locations)
# print(f'min location = {min(seed_locations)}')
