import math


with open('input.txt', 'r') as f:
    instr = f.readline().strip()
    f.readline()
    m = {}
    for line in f.readlines():
        _from, dst = line.strip()[:-1].split(' = (')
        dst = dst.split(', ')
        m[_from] = dst

# During investigation of input data I've found there are cycles of length equal to number of steps to reach
# finish point for each of ghosts. So the result will be LCM(*number of steps to reach finish for each of ghosts)

steps_count = 0
cur_points = [_from for _from in m if _from[-1] == 'A']
cycle_params = [0] * len(cur_points)
while not all(cycle_params):
    step_num = steps_count % len(instr)
    step = instr[step_num]
    for i, cur_point in enumerate(cur_points):
        if not cycle_params[i]:
            if cur_point[-1] == 'Z':
                cycle_params[i] = steps_count
            cur_points[i] = m[cur_point][step == 'R']
    steps_count += 1

print(math.lcm(*cycle_params))
