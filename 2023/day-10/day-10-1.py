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
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            m[x, y] = c
            if c == 'S':
                sx, sy = x, y

def check(x, y, dx, dy):
    count = 1
    while (x, y) in m and m[x, y] != 'S' and m[x, y] in d and (dx, dy) in d[m[x, y]]:
        dx, dy = d[m[x, y]][dx, dy]
        x, y = x + dx, y + dy
        count += 1
    return count * ((x, y) in m and m[x, y] == 'S')

print(max(check(sx + dx, sy + dy, dx, dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]) // 2)
