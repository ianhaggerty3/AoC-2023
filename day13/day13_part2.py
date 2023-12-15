import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

def lichenstein_diff(line1, line2):
    diff = 0
    for a, b in zip(line1, line2):
        diff += 1 if a != b else 0
    
    return diff

blocks = []
current_block = []
for line in lines:
    if len(line) == 0:
        blocks.append(current_block)
        current_block = []
        continue
    current_block.append(line)

def detect_horizontal_reflection(block):
    for possible in range(1, len(block)):
        count = min(possible, len(block) - possible)

        top = block[possible-count:possible]
        bottom = reversed(block[possible:possible+count])
        total_diff = 0
        for line1, line2 in zip(top, bottom):
            total_diff += lichenstein_diff(line1, line2)
        
        if total_diff == 1:
            return possible
        
    
    return 0

swapped_blocks = [[''.join([line[i] for line in block]) for i in range(len(block[0]))] for block in blocks]

total = 0
for i, block in enumerate(blocks):
    total += 100 * detect_horizontal_reflection(block)
for i, block in enumerate(swapped_blocks):
    total += detect_horizontal_reflection(block)

print(total)