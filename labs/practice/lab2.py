import os

# Write a function to return a list of the first n numbers in the Fibonacci string.
#  F{n}=F{n-1}+F{n-2}


def first_n_numbers_in_fibonacci(n):
    if n < 1:
        return []
    if n is 1:
        return [0]
    if n is 2:
        return [0, 1]

    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    return fibonacci


#
# print("Invalid input: ", first_n_numbers_in_fibonacci(-1))
# print("First fibonacci number: ", first_n_numbers_in_fibonacci(1))
# print("First " + str(2) + " fibonacci numbers: ", first_n_numbers_in_fibonacci(2))
# print("First " + str(10) + " fibonacci numbers: ", first_n_numbers_in_fibonacci(10))

# Sa se scrie o func?ie cu numele problema2 ce prime?te ca parametri trei numere, a, b ?i n
# si returneaza al n-lea element din sirul construit pe baza formulei:
# f(n) = 2 * f(n - 2) + f(n - 1). Consideram f(1) = a si f(2) = b

def problema2(a, b, n):
    sir = [a, b]

    for i in range(2, n):
        sir.append(2 * sir[i - 2] + sir[i - 1])

    return sir[n - 1]


# print(problema2(1, 2, 3))


# Sa se scrie o func?ie cu numele problema4 ce returneaza o lista cu dimensiunile unice ale
# fi?ierelor din directorul dat ca argument la linia de comanda (nerecursiv).
# Lista trebuie sa fie sortata crescator.

def problema4(directory_path):
    set_of_sizes = set()
    elements = os.listdir(directory_path)

    for element in elements:
        full_path = os.path.join(directory_path, element)
        if os.path.isfile(full_path):
            element_size = os.path.getsize(full_path)
            print((element, element_size))
            set_of_sizes.add(element_size)

    list_of_sizes = list(set_of_sizes)
    list_of_sizes.sort()

    return list_of_sizes


# print(problema4('C:\\facultate\\an3\\sem1\\python\\python\\labs'))


# ?Sa se scrie o func?ie cu numele problema5 ce prime?te un parametru, n (?ir de caractere)
# reprezent?nd un numar ?n baza 8.
# Func?ia returneaza True daca reprezentarea acestui numar ?n baza 10 este un palindrom ?i False ?n caz contrar.
# Hint: int(...)


def problema5(n):
    def is_palindrom(n):
        n = str(n)
        left = 0
        right = len(n) - 1

        while left < right:
            if n[left] is not n[right]:
                return False
            left += 1
            right -= 1
        return True

    n = int(n, 8)
    print(n)
    return is_palindrom(n)


print(problema5('171'))
print(problema5('16427'))
print(problema5('55'))
