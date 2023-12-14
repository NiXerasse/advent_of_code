CYCLE_START = 80
CYCLE_LEN = 38
with open('input.txt') as f:
    b = [[*r,] for r in f.read().split('\n')]
    totals = [0] * (CYCLE_START + CYCLE_LEN)
    for cn in range(CYCLE_START + CYCLE_LEN):
        for _ in range(4):
            p = [-1] * len(b[0])
            for y, r in enumerate(b):
                for x, c in enumerate(r):
                    if c == '#':
                        p[x] = y
                    elif c == 'O':
                        p[x] += 1
                        b[y][x] = '.'
                        b[p[x]][x] = 'O'
            b = [[*r,][::-1] for r in zip(*b)]

        total = sum(len(b) - y for y, r in enumerate(b) for x, c in enumerate(r) if c == 'O')
        totals[cn] = total

    cn = 1_000_000_000 - 1
    print(totals[(cn - CYCLE_START) % CYCLE_LEN + CYCLE_START])
