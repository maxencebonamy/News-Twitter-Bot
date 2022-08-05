import random


def getDifferentRandoms(n_min, n_max, length):
    assert n_max - n_min + 1 >= length

    result = []
    n = 0

    while len(result) < length:
        n = random.randint(n_min, n_max)
        if n not in result:
            result.append(n)

    return result