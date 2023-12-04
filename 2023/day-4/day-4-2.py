from functools import cache

cards = [0]
with open('input.txt', 'r') as f:
    for line in f.readlines():
        _, data = line.split(': ')
        win, mine = data.split('|')
        win = {*map(int, win.split())}
        cards.append(sum(num in win for num in map(int, mine.split())))


@cache
def get_win_count(n):
    win_count = cards[n]
    return win_count + sum(get_win_count(n + w) for w in range(1, win_count + 1))


total = len(cards) - 1
total += sum(get_win_count(i) for i in range(1, len(cards)))
print(total)
