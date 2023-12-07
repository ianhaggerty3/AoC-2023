import sys
from math import floor, ceil, sqrt

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

time = int(raw_lines[0].split(':')[1].replace(" ", ""))
distance = int(raw_lines[1].split(':')[1].replace(" ", ""))

# V1
# total = 0
# for i in range(time + 1):
#     if i * (time - i) > distance:
#         total += 1

# V2
# first = 0
# while first * (time - first) < distance:
#     first += 1

# V3
# last = time
# while last * (time - last) < distance:
#     last -= 1

# quadratics FTW :)
first = ceil((time - sqrt(time ** 2 - 4 * distance)) / 2)
last = floor((time + sqrt(time ** 2 - 4 * distance)) / 2)

print(last - first  + 1)