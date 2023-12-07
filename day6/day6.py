import sys

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

raw_times = raw_lines[0].split(':')[1].strip()
raw_distances = raw_lines[1].split(':')[1].strip()

times = list(map(int, [time for time in raw_times.split(' ') if len(time) != 0]))
distances = list(map(int, [distance for distance in raw_distances.split(' ') if len(distance) != 0]))

options = 1
for time, distance in zip(times, distances):
    total = 0
    for i in range(time + 1):
        if i * (time - i) > distance:
            total += 1
    options *= total


print(options)