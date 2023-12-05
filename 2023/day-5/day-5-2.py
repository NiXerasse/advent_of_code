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
            dst, src, d = map(int, line.split())
            maps[from_][1].append((src, dst, d))


def map_ranges(ranges, maps):
    ret_ranges = []
    for ra, rb in ranges:
        dst_ranges = []
        for src, dst, d in maps:
            sa, sb = src, src + d - 1
            if sa <= rb and sb >= ra:
                da, db = max(sa, ra), min(sb, rb)
                dst_ranges.append((da, db, dst + da - src, dst + db - src))
        if dst_ranges:
            dst_ranges.sort()
            for sa, sb, da, db in dst_ranges:
                if ra < sa:
                    ret_ranges.append((ra, sa - 1))
                ret_ranges.append((da, db))
                ra = sb + 1
            if rb > sb:
                ret_ranges.append((sb + 1, rb))
        else:
            ret_ranges.append((ra, rb))
    return ret_ranges


ranges = [(seed, seed + count - 1) for seed, count in zip(seeds[0::2], seeds[1::2])]
cur = 'seed'
while cur != 'location':
    cur, m = maps[cur]
    ranges = map_ranges(ranges, m)

print(sorted(ranges)[0][0])
