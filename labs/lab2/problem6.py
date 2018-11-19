# 6. Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
# 	Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
# 	Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3]
# 	 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.


def elements(x, *lists):
    flatten = []
    for l in lists:
        flatten += l

    return [e for e in set(flatten) if flatten.count(e) == x]


print(elements(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
