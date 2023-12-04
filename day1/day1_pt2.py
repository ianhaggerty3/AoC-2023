import sys

num_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
}

rev_map = {k[::-1]: v for k, v in num_map.items()}

def replace_inline_digits(line):
    i = 0
    while i < len(line):
        for key, value in num_map.items():
            if line[i::].startswith(key):
                line = line.replace(key, str(value), 1)
                break
        i += 1


    #best_pos = 10000000000000000000
    #best_key = None
    #for key, value in num_map.items():
    #    pos = line.find(key)
    #    if pos != -1 and pos < best_pos:
    #        best_pos = pos
    #        best_key = key
#
#    if best_key is not None:
#        line = line.replace(best_key, str(num_map[best_key]), 1)

#    best_pos = 10000000000000000000
#    best_key = None
#    rev_line = line[::-1]
#    for key, value in rev_map.items():
#        pos = rev_line.find(key)
#        if pos != -1 and pos < best_pos:
#            best_pos = pos
#            best_key = key
#
#    if best_key is not None:
#        rev_line = rev_line.replace(best_key, str(rev_map[best_key]), 1)

    return line


with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

print(raw_lines)

digified_lines = list(map(lambda line: replace_inline_digits(line), raw_lines))
num_lines = list(map(lambda line: list(filter(lambda character: character.isdigit(), line)),
    digified_lines))
print(num_lines)


nums_to_add = map(lambda line: int(line[0] + line[-1]), num_lines)
print(sum(nums_to_add))
