from itertools import groupby


def converter(n):
    print(max([len(list(g)) for k, g in groupby(bin(n))]))
    # return bin(n)[2:]


converter(13)