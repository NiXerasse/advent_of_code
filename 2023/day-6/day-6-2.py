with open('input.txt', 'r') as f:
    _, times = f.readline().split(':')
    _, dists = f.readline().split(':')
    r_time = int(times.replace(' ', ''))
    r_dist = int(dists.replace(' ', ''))
    count = sum(
        (r_time - t) * t > r_dist
        for t in range(r_time)
    )
    print(count)
