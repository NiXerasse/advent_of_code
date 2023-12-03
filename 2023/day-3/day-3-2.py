import itertools

with open('input.txt', 'r') as f:
    *r, = map(str.strip, f.readlines())
    total = 0
    for y in range(len(r)):
        for x in range(len(r[0])):
            if r[y][x] == '*':
                n = set()
                for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1)):
                    if (dx, dy) != (0, 0) and 0 <= (nx := x + dx) < len(r[0]) and 0 <= (ny := y + dy) < len(r) and r[ny][nx].isdigit():
                        s = r[ny][nx]
                        d = nx - 1
                        while d >= 0 and r[ny][d].isdigit(): s = r[ny][d] + s; d -= 1
                        d = nx + 1
                        while d < len(r[0]) and r[ny][d].isdigit(): s += r[ny][d]; d += 1
                        n.add(s)
                if len(n) == 2:
                    n1, n2 = n
                    total += int(n1) * int(n2)
    print(total)
