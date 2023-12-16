from collections import defaultdict
from itertools import chain


_map = {}
max_x, max_y = 0, 0
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        max_y = max(y, max_y)
        for x, char in enumerate(line.strip()):
            max_x = max(x, max_x)
            _map[x, y] = char

visited = defaultdict(lambda: set())
border_out = set()
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
        if (x, y) not in _map:
            border_out.add((x - dx, y - dy))

max_energy = 0
for x, y, dx, dy in [(0, 0, 1, 0), (0, 0, 0, 1), (max_x, 0, 0, 1), (max_x, 0, -1, 0), 
                     (max_x, max_y, -1, 0), (max_x, max_y, 0, -1), (0, max_y, 0, -1), (0, max_y, 1, 0)]:
    border_out.add((x, y))
    visited.clear()
    max_energy = max(max_energy, sum(len(v) > 0 for v in visited.values()))
    
for x, y in chain([(x, y) for y in [0, max_y] for x in range(1, max_x)],
                  [(x, y) for x in [0, max_x] for y in range(1, max_y)]):
    if (x, y) not in border_out:
        border_out.add((x, y))
        visited.clear()
        push_beam(x, y, 1 if x == 0 else -1 if x == max_x else 0, 1 if y == 0 else -1 if y == max_y else 0)
        max_energy = max(max_energy, sum(len(v) > 0 for v in visited.values()))

print(max_energy)
