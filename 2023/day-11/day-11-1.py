with open('input.txt') as f:
    space = []
    for line in f.readlines():
        space.append(line.strip())   
    w, h = len(space[0]), len(space)
    C = []
    DX = set()
    for x in range(w):
        if all(space[y][x] == '.' for y in range(h)):
            DX.add(x)
    dy = 0
    for y in range(h):
        if all(c == '.' for c in space[y]):
            dy += 1
        else:
            dx = 0
            for x in range(w):
                if x in DX:
                    dx += 1
                elif space[y][x] != '.':
                    C.append((x+dx, y + dy))
    
    total_dist = sum(
        abs(C[i][0] - C[j][0]) + abs(C[i][1] - C[j][1]) for i in range(len(C)) for j in range(i + 1, len(C))
    )
    print(total_dist)
