import sys

def parse_num_sequence(sequence):
    nums = list(filter(lambda num: num != '', sequence.split(' ')))
    return list(map(int, nums))

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip().split(':')[1].strip() for line in fid.readlines()]

winning_numbers = list(map(lambda line: parse_num_sequence(line.split('|')[0]), lines))
player_numbers = list(map(lambda line: parse_num_sequence(line.split('|')[1]), lines))

print(winning_numbers)
print(player_numbers)

total_score = 0
for winners, nums in zip(winning_numbers, player_numbers):
    matches = sum(map(lambda num: num in winners, nums))
    card_score = 0 if matches == 0 else 2 ** (matches - 1)
    total_score += card_score

print(total_score)
