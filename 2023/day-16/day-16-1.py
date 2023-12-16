from collections import defaultdict


_map = {}
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            _map[x, y] = char

visited = defaultdict(lambda: set())

def push_beam(x, y, dx, dy):
    while (x, y) in _map and (dx, dy) not in visited[x, y]:
        visited[x, y].add((dx, dy))
        if _map[x, y] == "\\":
            dx, dy = dy, dx
        elif _map[x, y] == '/':
            dx, dy = -dy, -dx
        elif dy == 0 and _map[x, y] == '|':
            push_beam(x, y - 1, 0, -1)
            push_beam(x, y + 1, 0, 1)
            return
        elif dx == 0 and _map[x, y] == '-':
            push_beam(x + 1, y, 1, 0)
            push_beam(x - 1, y, -1, 0)
            return
        x, y = x + dx, y + dy

push_beam(0, 0, 1, 0)
print(sum(len(v) > 0 for v in visited.values()))
