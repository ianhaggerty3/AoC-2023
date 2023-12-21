import sys

def scrunch_maps(map1, map2):
    new_map = {}
    for span1, dest1 in map1.items():
        diff = dest1 - span1.start

        # TODO: Handle blank sections
        span_map = {}
        for span2, dest2 in map2.items():
            if span1.start + diff >= span2.stop or span1.stop + diff <= span2.start:
                continue
            new_start = max(span1.start + diff, span2.start)
            new_stop = min(span1.stop + diff, span2.stop)

            span_map[range(new_start, new_stop)] = dest2 + (new_start - span2.start)
        

        points = list(map(lambda item: item[0], span_map.keys())) + list(map(lambda item: item[0], span_map.keys()))
        points.insert(0, span1.start + diff)
        points.append(span1.stop + diff)
        points = sorted(points)
        for p1, p2 in zip(points[:], points[1:]):
            if p1 != p2:
                new_map[range(p1, p2)] = span_map.get(range(p1, p2), p1)
    
    return new_map

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

print(min(lookup_list[0].values()))
