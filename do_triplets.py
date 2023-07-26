def get_triplets(l):
    list_length = len(l)
    for i in range(list_length):
        triplet = l[i]
        for m in range(1, 3):
            t_idx = i + m
            if t_idx >= list_length:
                break
            triplet += l[t_idx]
        yield triplet

a = [
    'line 1\n',
    'line 2\n',
    'line 3\n',
    'line 4\n',
    'line 5\n',
    'line 6\n',
    'line 7\n',
    'line 8\n',
    'line 9\n',
    'line 10\n'
]


if __name__ == '__main__':
    triplets = get_triplets(a)
    for triplet in triplets:
        print('-----------------')
        print(triplet)
        print('-----------------')