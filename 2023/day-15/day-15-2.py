from collections import defaultdict


def _hash(w):
    h = 0
    for c in w:
        h = (h + ord(c)) * 17 % 256
    return h


with open('input.txt') as f:
    box = [[] for _ in range(256)]
    lens = defaultdict(lambda: None)
    for step in f.readline().strip().split(','):
        if '-' in step:
            lens_name = step[:-1]
            box_no, lens_idx = _hash(lens_name), lens[lens_name]
            if lens_idx is not None:
                box[box_no][lens_idx], lens[lens_name] = 0, None
        else:
            lens_name, f_length = step.split('=')
            box_no, lens_idx = _hash(lens_name), lens[lens_name]
            if lens_idx is not None:
                box[box_no][lens_idx] = int(f_length)
            else:
                box[box_no].append(int(f_length))
                lens[lens_name] = len(box[box_no]) - 1
    total = sum(
        box_no * lens_idx * f_length
        for box_no, lenses in enumerate(box, start=1)
        for lens_idx, f_length in enumerate(filter(None, lenses), start=1)
    )
    print(total)
