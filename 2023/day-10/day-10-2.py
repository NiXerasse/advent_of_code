d = {
    'F': {
        (0, -1): (1, 0),
        (-1, 0): (0, 1)
    },
    '7': {
        (1, 0): (0, 1),
        (0, -1): (-1, 0)
    },
    'J': {
        (0, 1): (-1, 0),
        (1, 0): (0, -1)
    },
    'L': {
        (0, 1): (1, 0),
        (-1, 0): (0, -1)
    },
    '-': {
        (1, 0): (1, 0),
        (-1, 0): (-1, 0)
    },
    '|': {
        (0, 1): (0, 1),
        (0, -1): (0, -1)
    }
}

m = {}
sx = sy = 0
max_x, max_y = 0, 0
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            m[2 * x, 2 * y] = c
            m[2 * x + 1, 2 * y] = '-' if c in 'SFL-' else '.'
            m[2 * x, 2 * y + 1] = '|' if c in 'SF7|' else '.'
            m[2 * x + 1, 2 * y + 1] = '.'
            if c == 'S':
                sx, sy = 2 * x, 2 * y
    max_x, max_y = 2 * x + 1, 2 * y + 1

def check(x, y, dx, dy):
    borders = {(x - dx, y - dy)}
    count = 1
    while (x, y) in m and m[x, y] != 'S' and m[x, y] in d and (dx, dy) in d[m[x, y]]:
        borders.add((x, y))
        dx, dy = d[m[x, y]][dx, dy]
        x, y = x + dx, y + dy
        count += 1
    return (x, y) in m and m[x, y] == 'S' and borders

def is_inside(x, y, borders):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny, bc = x, y, 0
        while (nx, ny) in m:
            bc += (nx, ny) in borders
            nx, ny = nx + dx, ny + dy
        if bc % 2 == 0:
            return False
    return True

def fill(x, y):
    s = [(x, y)]
    while s:
        x, y = s.pop()
        m[x, y] = '*'
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy 
            if (nx, ny) in m and m[nx, ny] == '.':
                s.append((nx, ny))

for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    borders = check(sx + dx, sy + dy, dx, dy)
    if borders:
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) not in borders:
                    m[x, y] = '.'
        for dx, dy in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
            if is_inside(sx + dx, sy + dy, borders):
                fill(sx + dx, sy + dy)
                print(sum(m[x, y] == '*' for x in range(0, max_x + 1, 2) for y in range(0, max_y + 1, 2)))
                break
        break
