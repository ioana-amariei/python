# Given a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float).
# Evaluate the polynomial for the given value.


def is_numerical(character):
    return character in '0123456789'


def is_operator(character):
    return character in '-+/%^'


def is_unknown_value(character):
    return character == 'x'


def polinom_solution(string, number, number_type):
    operators = []
    values = []

    for character in string:
        if is_numerical(character):
            values.append(number_type(character))
        if is_operator(character):
            operators.append(character)
        if is_unknown_value(character):
            operators.append('*')
            values.append(number)

    print(values)
    print(operators)

    if len(operators) > len(values):
        print("Invalid equation.")
        return None

    result = values[0]

    for index in range(0, len(operators)):
        if operators[index] == '+':
            result += values[index + 1]
        elif operators[index] == '-':
            result -= values[index + 1]
        elif operators[index] == '*':
            result *= values[index + 1]
        elif operators[index] == '/':
            result /= values[index + 1]
        elif operators[index] == '^':
            result ^= values[index + 1]
        elif operators[index] == '%':
            result %= values[index + 1]

    return result


def compute_polynomial_for_float_value(string, number):
    return 0


def compute_polynomial(string, number):
    if len(string) < 2:
        return None

    if isinstance(number, int):
        return polinom_solution(string, number, int)

    if isinstance(number, float):
        return polinom_solution(string, number, float)


print("The result of '3x ^ 3 + 5x ^ 2 - 2x - 5' equation where x = 3 is: ",
      compute_polynomial("3x ^ 3 + 5x ^ 2 - 2x - 5", 3))

# print("The result of '3x ^ 3 + 5x ^ 2 - 2x - 5' equation where x = 3.5 is: ",
#       compute_polynomial("3x ^ 3 + 5x ^ 2 - 2x - 5", 3.5))
