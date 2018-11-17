from pathlib import Path

if __name__ == "__main__":
    # https://docs.python.org/2/tutorial/modules.html
    # if __name__ => __main__ (for execution),
    # if __name__ => __file-name__ (import)
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print("Help")


def problema2():
    product = 1
    for n in range(1, 11):
        product *= n

    return product


def problema3(n):
    initial = str(n)
    reversed = initial[::-1]
    return initial == reversed

    # if n < 0:
    #     return False
    # if 0 <= n < 10:
    #     return True
    #
    # x = []
    # while n > 0:
    #     x.append(n % 10)
    #     n = int(n / 10)
    #
    # return x == list(reversed(x))


def problema4(m):
    # palindroms = []
    # for i in range (0, m):
    #     if problema3(i):
    #         palindroms.append(i)
    #
    # return palindroms

    return [x for x in range(0, m) if problema3(x)]


def problema5(my_list):
    return [x for x in set(my_list) if x % 7 == 0]


def get_python_paths(folder):
    return [str(x.absolute()) for x in Path(folder).glob("*.py") if x.is_file()]


def write_path(cale, fisier):
    f = open(fisier, "a+")
    f.write(cale + '\n')
    f.close()


def problema6(folder, fisier):
    for cale in get_python_paths(folder):
        write_path(cale, fisier)


def get_dir_paths(director, depth):
    dirs = [str(x.absolute()) for x in Path(director).iterdir() if x.is_dir()]
    if depth <= 1:
        return dirs
    else:
        result = []
        for dir in dirs:
            result += get_dir_paths(dir, depth - 1)
        return result


def problem7(director, depth):
    return [a for a in get_dir_paths(director, depth) if len(get_python_paths(a)) > 0]


print(problema2())
print(problema3(123))
print(problema3(121))
print(problema4(100))
print(problema5([2, 3, 4, 7, 14, 21]))
problema6(".", "problema6.txt")
print(problem7("C:\\facultate\\an3\\sem1", 2))
