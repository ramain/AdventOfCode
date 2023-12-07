import numpy as np
import collections
f = open('input', 'r')
#f = open('test', 'r')

def score_hand(hand):
    reduce = len(set(hand))
    if reduce == 1:
        score = 7
    elif reduce == 2:
        duplicate = collections.Counter(hand).most_common(1)[0]
        if duplicate[1] == 4:
            score = 6
        else:
            score = 5
    elif reduce == 3:
        duplicate = collections.Counter(hand).most_common(1)[0]
        if duplicate[1] == 3:
            score = 3
        else:
            score = 2
    elif reduce == 4:
        score = 1
    else:
        score = 0
    return score

def card_digit(card):
    if card == 'T':
        dig = 10
    elif card == 'J':
        dig = 11
    elif card == 'Q':
        dig = 12
    elif card == 'K':
        dig = 13
    elif card == 'A':
        dig = 14
    else:
        dig = int(card)
    return dig

def tiebreak(handgroup):
    nums = []
    for h in handgroup:
        num = 0
        for i in range(5):
            num += card_digit(h[i]) / (15.0)**i
        nums.append(num)
    nums = np.array(nums)
    i_tbreak = np.argsort(np.argsort(nums))
    #i_tbreak = np.argsort(nums)
    return i_tbreak



hands = []
bids = []

for line in f:
    line = line.split()
    hands.append(line[0])
    bids.append(int(line[1]))

scores = []
for hand in hands:
    score = score_hand(hand)
    scores.append(score)

isort = np.argsort(scores)
hands = np.array(hands)[isort]
bids = np.array(bids)[isort]
scores = np.array(scores)[isort]

# tiebreak equal hands
ranking = []
rank_counter = 1
for score in range(8):
    handgroup = hands[scores == score]
    print(handgroup)
    if len(handgroup) == 1:
        ranking.append(rank_counter)
        rank_counter += 1
    elif len(handgroup) > 1:
        i_tbreak = tiebreak(handgroup)
        for i in i_tbreak:
            ranking.append(i+rank_counter)
        rank_counter += len(i_tbreak)
    else:
        continue

winnings = np.sum(np.array(bids) * np.array(ranking))
print(winnings)