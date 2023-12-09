data = []
with open('input.txt') as f:
    for line in f.readlines():
        data.append([*map(int, line.split())])

total = 0
for row in data:
    while (*filter(None, row),):
        total += row[-1]
        row = [b - a for a, b in zip(row, row[1:])]
print(total)
