def get_max_reflection(p):
    P = len(p)
    for i in range(1, P):
        d = min(i, P - i)
        if all(p[i + di] == p[i - 1 - di] for di in range(d)):
            return i


with open('input.txt') as f:
    data = f.read().split('\n\n')
    total = 0
    for part in data:
        part = part.strip().split('\n')
        h = get_max_reflection(part)
        total += 100 * h if h else get_max_reflection([*zip(*part)])
    print(total)
