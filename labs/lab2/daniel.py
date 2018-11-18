def sum_first(n):
    return sum([x for x in range(0, n + 1)])


def number_of_occurrences(my_list):
    return [(n, len(str(n))) for n in my_list]


def elements_that_occur_in_all(list_of_lists):
    result = set(list_of_lists[0])
    for l in list_of_lists:
        result = result.intersection(set(l))

    return list(result)


def sum_squared(n):
    return sum([x * x for x in range(0, n + 1)])


def sum_digits(x):
    s = 0
    while x > 0:
        s += (x % 10)
        x = int(x / 10)

    return s


def magic(x):
    if x < 10:
        return x
    else:
        return magic(sum_digits(x))


def magic_firsts(n):
    return [magic(x) for x in range(0, n + 1)]


print(sum_first(10))
print(number_of_occurrences([1, 10, 20]))
print(elements_that_occur_in_all([[1, 2], [1, 5, 3, 2], [5, 2, 1]]))
print(sum_squared(4))
print(magic_firsts(111))