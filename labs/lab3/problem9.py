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


def create_set_operations_dictionary(*sets):
    dictionary = dict()
    length = len(sets)
    sets = list(sets)

    for i in range(0, length):
        current_set = sets[i]
        for j in range(1, length):
            next_set = sets[j]

            intersection = current_set.intersection(next_set)
            union = current_set.union(next_set)
            diff1 = current_set.difference(next_set)
            diff2 = next_set.difference(current_set)

            print(intersection)
            print(union)
            print(diff1)
            print(diff2)

            dictionary.update({current_set + " & " + next_set, intersection})
            print(dictionary)
            dictionary.update({current_set + " | " + next_set, union})
            dictionary.update({current_set + " - " + next_set, diff1})
            dictionary.update({current_set + " & " + next_set, diff2})

    return dictionary


print(create_set_operations_dictionary({1, 2, 3}, {1, 4, 5}, {3, 4}))
