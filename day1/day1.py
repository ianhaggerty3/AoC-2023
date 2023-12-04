import sys

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

print(raw_lines)

num_lines = list(map(lambda line: list(filter(lambda character: character.isdigit(), line)), raw_lines))
print(num_lines)

nums_to_add = map(lambda line: int(line[0] + line[-1]), num_lines)
print(sum(nums_to_add))
