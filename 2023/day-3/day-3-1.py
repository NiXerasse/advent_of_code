import itertools

with open('input.txt', 'r') as f:
    *r, = map(lambda s: s.strip() + '.', f.readlines())
    total = 0
    for y in range(len(r)):
        xs = None
        for x in range(len(r[0])):
            if r[y][x].isdigit():
                if xs is None:
                    xs = x
            elif xs is not None:
                if any(
                        any(
                            not r[y + dy][xn + dx].isdigit()
                            for dx, dy in itertools.product((-1, 0, 1), (-1, 0, 1))
                            if (dx, dy) != (0, 0) and
                               0 <= xn + dx < len(r[0]) and
                               0 <= y + dy < len(r) and
                               r[y + dy][xn + dx] != '.'
                        )
                        for xn in range(xs, x)
                    ):
                    total += int(''.join(r[y][xs:x]))
                xs = None
    print(total)
