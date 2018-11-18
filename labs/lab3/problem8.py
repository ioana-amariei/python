# 8. Sa se scrie o functie care primeste ca parametru un set
#  si returneaza un tuplu (a, b),
#       a reprezentand numarul de elemente unice din set iar
#       b reprezentand numarul de elemente duplicate din set.


def get_tuple(input_set):
    uniques = [e for e in input_set if input_set.count(e) < 2]
    duplicates = list(set([e for e in input_set if input_set.count(e) > 1]))
    return uniques, duplicates


print(get_tuple([1, 2, 3, 4, 1, 2, 5, 4, 6, 7]))
