def _hash(w):
    h = 0
    for c in w:
        h = (h + ord(c)) * 17 % 256
    return h


with open('input.txt') as f:
    s = f.readline().strip().split(',')
    print(sum(map(_hash, s)))
