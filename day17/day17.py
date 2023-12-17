import sys
from operator import add
from queue import PriorityQueue

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

city = [[int(token) for token in line] for line in lines]

start = (0, 0)
end = (len(lines[0]) - 1, len(lines) - 1)

turn_map = {
    'N': {'N', 'E', 'W'},
    'E': {'N', 'E', 'S'},
    'S': {'S', 'E', 'W'},
    'W': {'N', 'S', 'W'},
    '': {'N', 'S', 'E', 'W'}
}

direction_map = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}


add_tuple = lambda a, b: tuple(map(add, a, b))

def check_pos(pos, city):
    return pos[0] >= 0 and pos[0] < len(city[0]) and pos[1] >= 0 and pos[1] < len(city)
            

def get_next(state):
    ret = []
    for direction in turn_map[state[1][:1]]:
        if direction == state[1][:1]:
            if len(state[1]) == 3:
                continue
            new_pos = add_tuple(state[0], direction_map[direction])
            if check_pos(new_pos, city):
                ret.append((new_pos, state[1] + direction))
        else:
            new_pos = add_tuple(state[0], direction_map[direction])
            if check_pos(new_pos, city):
                ret.append((new_pos, direction))
    
    return ret

options = PriorityQueue()

options.put((0, (start, '')))

seen = set()

while options:
    dist, current = options.get()
    if current in seen:
        continue
    seen.add(current)
    if current[0] == end:
        print(dist)
        break
    for neighbor in get_next(current):
        cost = city[neighbor[0][1]][neighbor[0][0]]
        options.put((dist + cost, neighbor))
        
print('we made it to the end')