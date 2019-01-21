# 2. Scrieti o functie care primeste ca parametru un sir de caractere si returneaza un dictionar
#  in care cheile sunt caracterele din componenta sirului de caractere
#  iar valorile sunt reprezentate de numarul de aparitii ale caracterului respectiv in textul dat.
# 	Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul:
# 	{'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.


def create_dictionary_from(string):
    return {c: string.count(c) for c in string}


# print(create_dictionary_from('Ana are mere.'))

# 6. Fie un dictionar global
# 				{
# 					"+": lambda a, b: a + b,
# 					"*": lambda a, b: a * b,
# 					"/": lambda a, b: a / b,
# 					"%": lambda a, b: a % b
# 				}
# 	Sa se construiasca o functie apply_operator(operator, a, b) care va aplica peste a si b regula specificata de
#   dictionarul global.
# 	Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara modificarea functiei.


global_dictionary = {"+": lambda a, b: a + b,
                     "*": lambda a, b: a * b,
                     "/": lambda a, b: a / b,
                     "%": lambda a, b: a % b,
                     "**": lambda a, b: a ** b
                     }


def apply_operator(operator, a, b):
    operation = global_dictionary[operator]
    return operation(a, b)


# print(apply_operator("+", 1, 2))
# print(apply_operator("*", 5, 2))
# print(apply_operator("**", 5, 2))

# 8. Sa se scrie o functie care primeste ca parametru un set
#  si returneaza un tuplu (a, b),
#       a reprezentand numarul de elemente unice din set iar
#       b reprezentand numarul de elemente duplicate din set.


def get_tuple_with_duplicates_and_uniques_from(input_list):
    uniques = set(input_list)
    duplicates = [e for e in input_list if input_list.count(e) > 1]

    return len(uniques), len(duplicates)


# print(get_tuple_with_duplicates_and_uniques_from([1, 2, 3, 4, 1, 2, 3, 2, 5, 6, 7, 8]))

# 9. Sa se scrie o functie care primeste un numar variabil de seturi
#   si returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua:
#   reuniune, intersectie, a-b, b-a.
# 	Cheia va avea urmatoarea forma:
#           "a op b", unde a si b sunt doua seturi,
#           iar op este operatorul aplicat: |, &, -.
# 	Ex: {1,2}, {2, 3} =>
# 			{
# 				"{1, 2} | {2, 3}": 3,
# 				"{1, 2} & {2, 3}": 1,
# 				"{1, 2} - {2, 3}": 1,
# 				...
# 			}


def create_operations_dictionary_from(* sets):
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


print(create_operations_dictionary_from({1, 2, 3}, {1, 4, 5}, {3, 4}))

