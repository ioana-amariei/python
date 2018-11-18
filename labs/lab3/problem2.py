# 2. Scrieti o functie care primeste ca parametru un sir de caractere si returneaza un dictionar
#  in care cheile sunt caracterele din componenta sirului de caractere
#  iar valorile sunt reprezentate de numarul de aparitii ale caracterului respectiv in textul dat.
# 	Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul:
# 	{'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.


def create_dictionary(string):
    # result = dict()
    #
    # for char in string:
    #     result.update({char: string.count(char)})
    #
    # return result

    return {c: string.count(c) for c in string}


print(create_dictionary("Ana are mere."))
