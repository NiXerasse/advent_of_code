with open('input.txt', 'r') as f:
    s = 0
    while line := f.readline().strip():
        n = [c for c in line if c.isdigit()]
        s += int(n[0] + n[-1])
    print(s)
