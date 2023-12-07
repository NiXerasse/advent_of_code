from collections import Counter

with open('input.txt', 'r') as f:
    hands = []
    for line in f.readlines():
        hands.append(line.split())


def get_strength(hand):
    *c, = Counter(hand).values()
    if 5 in c:
        return 7
    elif 4 in c:
        return 6
    elif 3 in c and 2 in c:
        return 5
    elif 3 in c:
        return 4
    elif c.count(2) == 2:
        return 3
    elif 2 in c:
        return 2
    return 1


cmp_hand = lambda h: \
    (get_strength(h[0]), h[0].replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A'))

print(sum(int(bid) * (rank + 1) for rank, [_, bid] in enumerate(sorted(hands, key=cmp_hand))))
