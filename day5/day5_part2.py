import sys
from operator import itemgetter

def reverse_dict(dict):
    return {v: k for k, v in dict.items()}

def scrunch_maps(map1, map2):
    new_map = {}
    # need to incorporate dest into algorithm and transform indices
    for span1, dest in map1.items():
        diff = dest - span1.start
        overlap = filter(lambda span2: (span2[0].start < (span1.stop + diff) and span2[0].stop > (span1.start + diff)), map2.items())
        # print(span1)
        # print(list(overlap))
        # if there are duplicates, the one with the highest dest will be preferred due to the sorting
        # no, this won't work, because dest does not normalize to zero and even if it did, there could be negative numbers
        # print(sum(map(lambda span: [(span[0].start, span[1]), (span[0].stop - 1, span[0].stop - 1)], overlap), start=[]))
        rangelist = sorted(sum(map(lambda span: [(span[0].start, span[1]), (span[0].stop - 1, span[0].stop - 1)], overlap), start=[]))
        
        # ugly 
        # could always do the inserts, but would need to define a clamp function
        # to really clean this up
        if rangelist[0][0] <= span1.start:
            rangelist[0] = (span1.start, rangelist[0][1])
        else:
            rangelist.insert(0, (span1.start, span1.start))
        
        if rangelist[-1][0] >= (span1.stop - 1):
            rangelist[-1] = (span1.stop - 1, rangelist[-1][1])
        else:
            rangelist.append((span1.stop - 1, span1.stop - 1))

        for i, j in zip(rangelist[0::], rangelist[1::]):
            if i[0] != j[0]:
                new_map[range(i[0], j[0] + 1)] = i[1]
    
    print('new map')
    print(new_map)
    return new_map

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

initial_seeds = {}
for start, length in zip(initial_seed_ranges[0::2], initial_seed_ranges[1::2]):
    initial_seeds[range(start, start + length)] = start

map_lines = raw_lines[2::]
lookup_list = [initial_seeds]
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

while len(lookup_list) > 1:
    map_to_scrunch = lookup_list.pop(1)
    lookup_list[0] = scrunch_maps(lookup_list[0], map_to_scrunch)

print(min(map(lambda entry: entry.start, lookup_list[0].keys())))

# seed_locations = list(map(lambda seed: get_seed_location(seed, lookup_list), initial_seeds))
# print(seed_locations)
# print(f'min location = {min(seed_locations)}')
