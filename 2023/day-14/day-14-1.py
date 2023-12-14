with open('input.txt') as f:
    b = [[*r,] for r in f.read().split('\n')]
    B = len(b)
    p = [-1] * len(b[0])
    total = 0
    for y, r in enumerate(b):
        for x, c in enumerate(r):
            if c == '#':
                p[x] = y
            elif c == 'O':
                p[x] += 1
                total += B - p[x] - 1
    print(total)
