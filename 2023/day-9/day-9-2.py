data = []
with open('input.txt') as f:
    for line in f.readlines():
        data.append([*map(int, line.split())])

total = 0
for row in data:
    sign = 1
    while (*filter(None, row),):
        total += row[0] * sign
        row = [b - a for a, b in zip(row, row[1:])]
        sign = -sign
print(total)
