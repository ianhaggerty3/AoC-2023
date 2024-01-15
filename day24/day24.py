import sys
from itertools import combinations

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

start, stop = list(map(int, lines[0].strip().split(' ')))

def calculate_intersection(p1, p2, v1, v2):
    lhs = p1[1] - p2[1] + (v1[1] * (p2[0] - p1[0])) / v1[0]
    divisor = (v2[1] - (v1[1] / v1[0]))

    if divisor == 0:
        return None, None

    t2 = lhs / divisor

    x = p2[0] + v2[0] * t2
    y = p2[1] + v2[1] * t2

    return x, y

# todo: fix heuristic to determine if particle collides with test area at all
def determine_intersects(p, v):
    x1, y1 = calculate_intersection(p, [start, 0, 0], v, [0, 1, 0])
    x2, y2 = calculate_intersection(p, [stop, 0, 0], v, [0, 1, 0])

    if x1 is None or x2 is None:
        print(f'returning False for {p}')
        return False
    
    print('made it here')

    # if x1 < start and x2 < start:
    #     return False
    
    # if x1 > stop and x2 > stop:
    #     return False
    
    if y1 < start and y2 < start:
        return False
    
    if y1 > stop and y2 > stop:
        return False

    return True

positions = []
velocities = []
for line in lines[1::]:
    raw_position, raw_velocity = line.split('@')
    position = list(map(int, raw_position.strip().split(', ')))
    velocity = list(map(int, raw_velocity.strip().split(', ')))
    positions.append(position)
    velocities.append(velocity)

valid_indices = filter(lambda i: determine_intersects(positions[i], velocities[i]), range(len(positions)))

total = 0
for s1, s2 in combinations(valid_indices, 2):
    p1 = positions[s1]
    p2 = positions[s2]
    v1 = velocities[s1]
    v2 = velocities[s2]

    x, y = calculate_intersection(p1, p2, v1, v2)

    if x in range(start, stop + 1) and y in range(start, stop + 1):
        total += 1

print(total)