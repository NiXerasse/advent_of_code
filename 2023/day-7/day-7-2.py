from collections import Counter

with open('input.txt', 'r') as f:
    hands = []
    for line in f.readlines():
        hands.append(line.split())


def get_strength(hand):
    cc = Counter(hand)
    j = cc['J']
    c = [cc[x] for x in cc if x != 'J']
    m = max(c, default=0) + j
    if m == 5:
        return 7
    elif m == 4:
        return 6
    elif 3 in c and 2 in c or c.count(2) == 2 and j:
        return 5
    elif m == 3:
        return 4
    elif c.count(2) == 2:
        return 3
    elif m == 2:
        return 2
    return 1


cmp_hand = lambda h: \
    (get_strength(h[0]), h[0].replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', '0').replace('T', 'A'))

print(sum(int(bid) * (rank + 1) for rank, [_, bid] in enumerate(sorted(hands, key=cmp_hand))))
