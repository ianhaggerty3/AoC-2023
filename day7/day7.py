import sys
from functools import cmp_to_key

with open(sys.argv[1], 'r') as fid:
    raw_lines = [line.strip() for line in fid.readlines()]

points = {str(k): k for k in range(2, 10)}
points['T'] = 10
points['J'] = 11
points['Q'] = 12
points['K'] = 13
points['A'] = 14

def is_five(hand):
    return len(set(hand)) == 1

def is_four(hand):
    hand_set = set(hand)
    length = len(hand_set)
    example = hand_set.pop()
    count = hand.count(example)
    return length == 2 and (count == 1 or count == 4)

def is_full_house(hand):
    hand_set = set(hand)
    length = len(hand_set)
    example = hand_set.pop()
    count = hand.count(example)
    return length == 2 and (count == 2 or count == 3)

def is_three(hand):
    return len(set(hand)) == 3 and max(map(lambda char: hand.count(char), set(hand))) == 3

def is_two_pair(hand):
    return len(set(hand)) == 3 and not is_three(hand)

def is_pair(hand):
    return len(set(hand)) == 4

def is_high_card(hand):
    return len(set(hand)) == 5

identifiers = [is_five, is_four, is_full_house, is_three, is_two_pair, is_pair, is_high_card]

def compare_hands(hand1, hand2):
    for identifier in identifiers:
        results = [identifier(hand1[0]), identifier(hand2[0])]
        if sum(results) == 2:
            break
        elif sum(results) == 1:
            if results[0] is True:
                return 1
            else:
                return -1
    
    for char1, char2 in zip(hand1[0], hand2[0]):
        if points[char1] != points[char2]:
            return points[char1] - points[char2]
    
    print('houston, we have a problem')

hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in raw_lines]

hand_rankings = sorted(hands, key=cmp_to_key(compare_hands))
print(hand_rankings)

print(sum(map(lambda item: (item[0] + 1) * item[1][1], enumerate(hand_rankings))))
