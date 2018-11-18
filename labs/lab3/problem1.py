# 1. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza un tuplu de seturi care sa contina:
# 	(a intersectat cu b, a reunit cu b, a - b, b - a)


def set_operations(a, b):
    a = set(a)
    b = set(b)

    intersection = list(a.intersection(b))
    union = list(a.union(b))
    diff1 = list(a.difference(b))
    diff2 = list(b.difference(a))

    return intersection, union, diff1, diff2


print(set_operations([1, 2, 3, 4, 5], [4, 1, 7, 8, 9]))

