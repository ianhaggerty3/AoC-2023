import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

steps = lines[0].split(',')

total = 0
for step in steps:
    current_val = 0
    for token in step:
        current_val += ord(token)
        current_val *= 17
        current_val %= 256
    
    total += current_val

print(total)

    
