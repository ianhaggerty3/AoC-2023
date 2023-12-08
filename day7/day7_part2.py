import sys
from functools import cmp_to_key
from operator import itemgetter

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

points = {str(k): k for k in range(2, 10)}
points['T'] = 10
points['J'] = 1
points['Q'] = 12
points['K'] = 13
points['A'] = 14

def improve_hand(hand: str):
    j_count = hand.count('J')
    raw_hand = hand.replace('J', '')
    if len(raw_hand) == 0:
        return 'AAAAA'
    best_wild_card = max(map(lambda char: (hand.count(char), char), set(raw_hand)), key=itemgetter(0))
    return raw_hand + j_count * best_wild_card[1]

def get_max_occurrence(hand):
    return max(map(lambda char: hand.count(char), set(hand)))

def compare_hands(hand1, hand2):
    hand1_set = set(improve_hand(hand1[0]))
    hand2_set = set(improve_hand(hand2[0]))

    if len(hand1_set) != len(hand2_set):
        return len(hand2_set) - len(hand1_set)
    elif get_max_occurrence(improve_hand(hand1[0])) != get_max_occurrence(improve_hand(hand2[0])):
        return get_max_occurrence(improve_hand(hand1[0])) - get_max_occurrence(improve_hand(hand2[0]))
    
    # score = [15 ** (5 - i) * hand[i] for i in range(len(hand))]

    for char1, char2 in zip(hand1[0], hand2[0]):
        if points[char1] != points[char2]:
            return points[char1] - points[char2]
    
    print('houston, we have a problem')

hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in raw_lines]

hand_rankings = sorted(hands, key=cmp_to_key(compare_hands))
print(hand_rankings)

print(sum(map(lambda item: (item[0] + 1) * item[1][1], enumerate(hand_rankings))))
