from collections import defaultdict

with open('input.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        game, log = line.split(': ')
        _, game_id = game.split()
        count = defaultdict(int)
        for round in log.split('; '):
            for turn in round.split(', '):
                cnt, color = turn.split()
                count[color] = max(count[color], int(cnt))
        if count['red'] <= 12 and count['green'] <= 13 and count['blue'] <= 14:
            total += int(game_id)
    print(total)
