import math


with open('input.txt', 'r') as f:
    _, times = f.readline().split(':')
    _, dists = f.readline().split(':')
    count = math.prod(
        sum(
            (_time - t) * t > dist
            for t in range(_time)
        )
        for _time, dist in zip(map(int, times.split()), map(int, dists.split()))
    )
    print(count)
