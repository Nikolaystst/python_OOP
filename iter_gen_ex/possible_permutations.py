from itertools import permutations


def possible_permutations(lst):
    n = permutations(lst)
    for x in n:
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]
