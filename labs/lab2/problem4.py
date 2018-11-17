# 4. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza:
# 	(a intersectat cu b, a reunit cu b, a - b, b - a)


def set_operations(a, b):
    a = set(a)
    b = set(b)

    intersection = list(a.intersection(b))
    union = list(a.union(b))
    dif1 = list(a.difference(b))
    diff2 = list(b.difference(a))

    return intersection, union, dif1, diff2


print(set_operations([1, 2, 3, 4], [3, 5, 6, 7, 1]))
