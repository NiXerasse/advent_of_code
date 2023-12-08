with open('input.txt', 'r') as f:
    route = f.readline().strip()
    f.readline()
    m = {}
    for line in f.readlines():
        _from, dst = line.strip()[:-1].split(' = (')
        dst = dst.split(', ')
        m[_from] = dst

steps_count = 0
cur_point = 'AAA'
while cur_point != 'ZZZ':
    step = route[steps_count % len(route)]
    cur_point = m[cur_point][step == 'R']
    steps_count += 1
print(steps_count)
