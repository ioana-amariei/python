# 9. Sa se scrie o functie care primeste un numar variabil de seturi
#   si returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua:
#   reuniune, intersectie, a-b, b-a.
# 	Cheia va avea urmatoarea forma:
#           "a op b", unde a si b sunt doua seturi,
#           iar op este operatorul aplicat: |, &, -.
# 	Ex: {1,2}, {2, 3} =>
#
# 			{
#
# 				"{1, 2} | {2, 3}": 3,
#
# 				"{1, 2} & {2, 3}": 1,
#
# 				"{1, 2} - {2, 3}": 1,
#
# 				...
#
# 			}
from pprint import PrettyPrinter


def create_set_operations_dictionary(*sets):
    dictionary = dict()
    length = len(sets)
    sets = list(sets)

    for i in range(0, length):
        a = sets[i]
        for j in range(i + 1, length):
            b = sets[j]

            intersection = a.intersection(b)
            union = a.union(b)
            diff1 = a.difference(b)
            diff2 = b.difference(a)

            dictionary.update({str(a) + " & " + str(b): intersection})
            dictionary.update({str(a) + " | " + str(b): union})
            dictionary.update({str(a) + " - " + str(b): diff1})
            dictionary.update({str(b) + " - " + str(a): diff2})

    return dictionary


pp = PrettyPrinter(indent=4)
pp.pprint(create_set_operations_dictionary({1, 2, 3}, {1, 4, 5}, {3, 4}))
