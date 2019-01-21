# Find The largest common divisor of multiple numbers.
# Define a function with variable number of parameters to resolve this.


def largest_common_divisor(*args):
    if (len(args)) == 0:
        return None

    a = args[0]
    for b in args[1:]:
        while b != 0:
            r = a % b
            a = b
            b = r
    return a


# print("cmmdc(12, 16): ", largest_common_divisor(12, 16))
# print("cmmdc(): ", largest_common_divisor())


# Write a function that calculates how many vowels are in a string.


def number_of_vowels(characters):
    vowels = [c for c in characters if c in 'aeiouAEIOU']
    return len(vowels)


# print(number_of_vowels('ana are mere dulci'))
# print(number_of_vowels('nfg ghf'))


# Write a function that returns the number of words in a string.
# Words are separated by spaces, punctuation marks (, ;, ? ! . )


def is_delimiter(character):
    return character in ' ,;,?!.'


def number_of_words(string):
    for character in string:
        if is_delimiter(character):
            string = string.replace(character, ' ')

    words = string.split(' ')
    return len(words)


# print("number of words: ", number_of_words("bdc!dijfvn.kfke"))
# print("number of words: ", number_of_words("bdc dijfvn,,kfke"))


# Write a function that receives two strings as parameters and returns the number of occurrences
# of the first string in the second.


def number_of_occurrences(first, second):
    return second.count(first)


# print("Number of occurrences of the 'abc' string in 'abcdddabcabc' string is: ",
#       number_of_occurrences("abc", "abcdddabcabc"))


# Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)4


def contains_special_characters(string):
    special_chars = [c for c in string if c in '\r\t\n\a\b\f\v']
    return len(special_chars) > 0


# print(contains_special_characters("abcvdsh\nbvdj\r"))
# print(contains_special_characters("abcv"))


#  Write a function that converts a string of characters written
# in UpperCamelCase into lowercase_with_underscores.


def convert(input_string):
    if input_string[0].isupper():
        input_string = input_string.replace(input_string[0], input_string[0].lower(), 1)

    length = len(input_string)
    for i in range(1, length):
        if input_string[i].isupper():
            input_string = input_string.replace(input_string[i], '_' + input_string[i].lower(), 1)

    return input_string


# print("Converted string: ", convert("CamelCase"))
# print("Converted string: ", convert("camelCase"))
# print("Converted string: ", convert("camelCaseNamingConvention"))


# Given a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float).
# Evaluate the polynomial for the given value.


def compute_polynomial_function(polynomial_string, number):
    values = [int(v) for v in polynomial_string if v in '0123456789']
    operators = [o for o in polynomial_string if o in '+*^-/']

    if len(operators) > len(values):
        print("Invalid equation.")
        return None

    result = values[0]
    length = len(operators)
    for i in range(0, length):
        if operators[i] == '+':
            result += values[i + 1]
        elif operators[i] == '-':
            result -= values[i + 1]
        elif operators[i] == '*':
            result *= values[i + 1]
        elif operators[i] == '/':
            result /= values[i + 1]
        elif operators[i] == '^':
            result ^= values[i + 1]
        elif operators[i] == '%':
            result %= values[i + 1]

    return result


# print("The result of '3x ^ 3 + 5x ^ 2 - 2x - 5' equation where x = 3 is: ",
#       compute_polynomial_function("3x ^ 3 + 5x ^ 2 - 2x - 5", 3))


# Write a function that returns the largest prime number from a string given as a parameter
# or -1 if the character string contains no prime number.
# Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271


def largest_prime_from(string):
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

    numbers = [n for n in string if n in '0123456789']

    if len(numbers) is 0:
        return -1

    length = len(string)
    primes = [-1]
    for i in range(0, length):
        number = 0
        while string[i] in '0123456789':
            number = number * 10 + int(string[i])

        if is_prime(number):
            primes.append(number)

    return max(primes)


# print(largest_prime_from('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))




