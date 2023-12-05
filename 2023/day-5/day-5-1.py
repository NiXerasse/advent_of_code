with open('input.txt', 'r') as f:
    _, seeds = f.readline().split(': ')
    *seeds, = map(int, seeds.split())
    maps = {}
    new_mapping, from_, to_ = False, '', ''
    for line in f.readlines():
        if not line.strip():
            new_mapping = True
        elif new_mapping:
            from_, _, to_ = line.split('-')
            to_, _ = to_.split()
            maps[from_] = (to_, [])
            new_mapping = False
        else:
            dest, src, d = map(int, line.split())
            maps[from_][1].append((dest, src, d))

min_loc = None
for seed in seeds:
    cur, num = 'seed', seed
    while cur != 'location':
        cur, m = maps[cur]
        for dst, src, d in m:
            if src <= num < src + d:
                num = dst + num - src
                break
    min_loc = num if min_loc is None else min(min_loc, num)

print(min_loc)
