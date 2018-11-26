import os
import sys


def problema1(n):
    return sum([x for x in range(0, n + 1)])


def problema2(a, b, n):
    sir = []
    # contor = 0
    # while contor < n:
    #     element = sir[n - 2] + 3 * sir[n - 1]
    #     sir.append(element)
    #     contor += 1

    return sir


# print(problema2(1, 3, 4))


def problema3(n, m):
    list = [(x - 2) + 3 * (x - 1) for x in range(3, 100000)]

    return list[0], list[1]


# print(problema3(2, 3))


def problema4():
    size = 0
    if len(sys.argv) > 2:
        folder = sys.argv[1]
        if os.path.isdir(folder):
            files = os.listdir(folder)
            for file in files:
                if ".jpg" in file:
                    size += file.count(file)

    return size


# print(problema4())


def problema5(characters):
    oglinda = characters[::-1]
    to_ten = int(characters, 3)
    return int(oglinda) == to_ten


def problema6(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, "r+")
        list = os.listdir(my_path)
        f.close()
        return list[::22]
    elif os.path.isdir(my_path):
        result = ()
        list = os.listdir(my_path)
        for e in list:
            if os.path.isdir(e):
                result += (my_path, e)

        return result


def problema7(*lists):
    return " "

