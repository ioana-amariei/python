# 3. Write a script that reads a file, line by line, and for every triple (a, b, c - separated by spaces)
#   applies operator c for the operands a and b.
#   The valid operations are : +, *, -,  \, ** .
#
# 	Input Example:
#
# 			3 5 ** => 3 ** 5 =  243
# 			7 2 + => 7 + 2   = 9


def compute_results():
    read_fd = open("operations.txt", "r")
    lines = read_fd.readlines()
    read_fd.close()

    result = None
    for line in lines:
        a, b, c = line.strip().split(" ")
        a, b = int(a), int(b)
        if c == "+":
            result = a + b
        elif c == "-":
            result = a - b
        elif c == "/":
            result = a / b
        elif c == "*":
            result = a * b
        elif c == "**":
            result = a ** b

        print("{} {} {} is {}".format(a, c, b, result))


compute_results()
