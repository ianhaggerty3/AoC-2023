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

matches_sequence = list(map(lambda pair: sum(map(lambda num: num in pair[0], pair[1])), zip(winning_numbers, player_numbers)))

print(matches_sequence)

size = len(matches_sequence)
card_match_map = {}

for i, matches in reversed(list(enumerate(matches_sequence))):
    card_total = 1
    for j in range(1, matches + 1):
        card_total += card_match_map.get(i + j, 0)
    
    card_match_map[i] = card_total

print(sum(card_match_map.values()))
