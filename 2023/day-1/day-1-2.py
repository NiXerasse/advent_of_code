d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five':'5', 'six': '6',
     'seven': '7', 'eight': '8', 'nine': '9'}
with open('input.txt', 'r') as f:
    s = 0
    while line := f.readline().strip():
        n = [
            line[i] if line[i].isdigit()
            else min([d[num] for num in d if line[i:i+len(num)] == num], default='')
            for i in range(len(line))
        ]
        *n, = filter(None, n)
        s += int(n[0] + n[-1])
    print(s)
