import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

steps = lines[0].split(',')

boxes = [[] for i in range(256)]
# I don't think lenses are a limited resource, so I don't need this
# lenses = [True for i in range(1, 10)]

total = 0
for step in steps:
    has_equals = '=' in step
    label = step.split('=')[0] if has_equals else step.split('-')[0]
    current_val = 0
    for token in label:
        current_val += ord(token)
        current_val *= 17
        current_val %= 256
    
    relevant_box = boxes[current_val]
    if not has_equals:
        matching_item = [(i, item) for i, item in enumerate(relevant_box) if item[0] == label]
        if len(matching_item) == 1:
            relevant_box.pop(matching_item[0][0])
    else:
        focal_length = int(step.split('=')[1])
        
        if len(list(filter(lambda item: item[0] == label, relevant_box))) == 0:
            relevant_box.append((label, focal_length))
        else:
            matching_item = [(i, item) for i, item in enumerate(relevant_box) if item[0] == label]
            relevant_box.pop(matching_item[0][0])
            relevant_box.insert(matching_item[0][0], (label, focal_length))


total_power = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        current = (i + 1) * (j + 1) * (lens[1])
        print(f'got power of {current} for box {i} {box}')
        total_power += current

print(total_power)