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


# print(problema5('171'))
# print(problema5('16427'))
# print(problema5('55'))


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.


def primes(numbers):
    def is_prime(nr):
        if nr < 2:
            return False
        if nr is 2:
            return True
        if nr % 2 is 0:
            return False
        for i in range(3, nr):
            if nr % i is 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]


# print(primes([1, 3, 4, 5, 6, 7, 8, 9, 11, 13, 2]))

# # 4. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza:
# # 	(a intersectat cu b, a reunit cu b, a - b, b - a)


def set_operations(a, b):
    a = set(a)
    b = set(b)

    intersection = a.intersection(b)
    reunion = a.union(b)
    diff1 = a.difference(b)
    diff2 = b.difference(a)

    return intersection, reunion, diff1, diff2


# print(set_operations([1, 2, 3, 4], [3, 5, 6, 7, 1]))


# 6. Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
# 	Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
# 	Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3]
# 	 1 se afla in lista 1 si 4,
#    2 se afla in lista 1 si 2,
#    3 se afla in listele 1 si 2,
#    4 se afla in listele 2 si 3


def get_list_with_exact_count_elements(x, *lists):
    flatten_list = []

    for l in lists:
        flatten_list += l

    return [elem for elem in set(flatten_list) if flatten_list.count(elem) is x]


# print(get_list_with_exact_count_elements(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

# 7. Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1,
#  un numar variabil de siruri de caractere
# 	si un flag boolean setat default pe True.
# 	Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele care au codul ASCII divizibil cu x
# 	in caz ca flag-ul este setat pe True, in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x.
# 	Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]).
# 	Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere
# 	primite ca input.


def generate_by_condition(x=1, flag=True, *strings):
    generated_lists = []

    for string in strings:
        if flag:
            generated_lists.append([c for c in string if ord(c) % x == 0])
        else:
            generated_lists.append([c for c in string if ord(c) % x != 0])

    return generated_lists


# print(generate_by_condition(2, False, "test", "hello", "lab002"))

# 8. Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel:
# 	primul tuplu sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
# 	Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].
# 	Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente,
# 	elementele lipsa vor fi inlocuite cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple.


def get_tuples(*lists):
    result = []

    index = 0
    while index < len(lists):
        each_tuple = tuple()
        for list in lists:
            each_tuple += (list[index],)
        result.append(each_tuple)
        index += 1

    return result


# print(get_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))


# 9. Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui
# 	de-al 2-lea element din tuplă. Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


def get_sorted_from(list_of_tuples):
    def take_third_character_from_second_tuple(current_tuple):
        return current_tuple[1][2]

    list_of_tuples.sort(key=take_third_character_from_second_tuple)

    return list_of_tuples


# print(get_sorted_from([('abc', 'bcd'), ('abc', 'zza')]))


