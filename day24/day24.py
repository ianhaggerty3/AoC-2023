import sys
from itertools import combinations

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

start, stop = list(map(int, lines[0].strip().split(' ')))

def calculate_intersection(p1, p2, v1, v2):
    lhs = p1[1] - p2[1] + (v1[1] * (p2[0] - p1[0])) / v1[0]
    divisor = (v2[1] - (v1[1] * v2[0] / v1[0]))

    if divisor == 0:
        return None, None

    t2 = lhs / divisor

    if t2 < 0:
        return None, None
    
    t1 = (p2[0] - p1[0] + v2[0] * t2) / v1[0]

    if t1 < 0:
        return None, None

    x = p2[0] + v2[0] * t2
    y = p2[1] + v2[1] * t2

    return x, y

def in_range(x):
    return x >= start and x <= stop

# todo: fix heuristic to determine if particle collides with test area at all
def determine_intersects(p, v):
    t1 = (start - p[0]) / v[0]
    y1 = p[1] + v[1] * t1


    t2 = (stop - p[0]) / v[0]
    y2 = p[1] + v[1] * t2

    if t1 < 0 and t2 < 0:
        return False
    
    if t1 < 0:
        return not (p[1] < start and y2 < start or p[1] > stop and y2 > stop)

    if t2 < 0:
        return not (p[1] < start and y1 < start or p[1] > stop and y1 > stop)
    
    return not (y1 < start and y2 < start or y1 > stop and y2 > stop)

positions = []
velocities = []
for line in lines[1::]:
    raw_position, raw_velocity = line.split('@')
    position = list(map(int, raw_position.strip().split(', ')))
    velocity = list(map(int, raw_velocity.strip().split(', ')))
    positions.append(position)
    velocities.append(velocity)

valid_indices = list(filter(lambda i: determine_intersects(positions[i], velocities[i]), range(len(positions))))

total = 0
for s1, s2 in combinations(valid_indices, 2):
    p1 = positions[s1]
    p2 = positions[s2]
    v1 = velocities[s1]
    v2 = velocities[s2]

    x, y = calculate_intersection(p1, p2, v1, v2)

    if x is not None and y is not None and in_range(x) and in_range(y):
        total += 1

print(total)