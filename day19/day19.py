import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

workflows = {}

def get_rule(rule):
    parts = rule.split(':')
    if len(parts) == 2:
        condition = rule.split(':')[0]
        target = rule.split(':')[1]
        if condition[1] == '<':
            callback = lambda part: part[condition[0]] < int(condition[2:])
        else:
            callback = lambda part: part[condition[0]] > int(condition[2:])
    else:
        callback = lambda part: True
        target = parts[0]

    return (callback, target)

part_start = 0
for i, line in enumerate(lines):
    if len(line) == 0:
        part_start = i + 1
        break
    name = line.split("{")[0]
    rules = line.split("{")[1][:-1]
    print(rules)

    workflow = [get_rule(rule) for rule in rules.split(',')]
    workflows[name] = workflow

parts = []
for line in lines[part_start:]:
    fields = line[1:-1]
    part = {}
    for field in fields.split(','):
        key = field.split('=')[0]
        value = int(field.split('=')[1])
        part[key] = value

    parts.append(part)

total = 0
for part in parts:
    current = 'in'
    while True:
        workflow = workflows[current]
        i = 0
        while workflow[i][0](part) is False:
            i += 1
        
        current = workflow[i][1]
        if current == 'R':
            break
        elif current == 'A':
            total += sum(part.values())
            break

print(total)