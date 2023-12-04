with open('input.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        _, data = line.split(': ')
        win, mine = data.split('|')
        win = {*map(int, win.split())}
        card_score = 0
        for num in map(int, mine.split()):
            if num in win:
                card_score = 1 if not card_score else card_score * 2
        total += card_score
    print(total)
