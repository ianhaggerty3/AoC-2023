import sys
from operator import itemgetter
import time

t0 = time.time()

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

def get_score(hand):
    return sum([15 ** (5 - i) * points[hand[i]] for i in range(len(hand))])

def get_comp_tuple(hand):
    improved_hand = improve_hand(hand[0])
    return (5 - len(set(improved_hand)), get_max_occurrence(improved_hand), get_score(hand[0]))

hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in raw_lines]
hand_rankings = sorted(hands, key=get_comp_tuple)

print(sum(map(lambda item: (item[0] + 1) * item[1][1], enumerate(hand_rankings))))

t1 = time.time()
print(t1 - t0)