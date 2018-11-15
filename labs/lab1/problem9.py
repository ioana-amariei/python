# Write a function that returns the largest prime number from a string given as a parameter
# or -1 if the character string contains no prime number.
# Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271


def contains_numbers(string):
    for character in string:
        if character in '0123456789':
            return True

    return False


def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for index in range(3, number):
        if number % index == 0:
            return False

    return True


def is_number(character):
    return character in '0123456789'


def get_index(string):
    for index in range(0, len(string)):
        if is_number(string[index]):
            return index

    return -1


def largest_prime_number(string):
    if len(string) == 0:
        return -1

    if not contains_numbers(string):
        return -1

    first_figure_index = get_index(string)
    largest_prime = -1
    number = 0

    for index in range(first_figure_index, len(string)):
        while is_number(string[index]):
            number = number * 10 + int(string[index])
            index += 1
        if is_largest_prime(largest_prime, number):
            largest_prime = number
        number = reset(number)

    return largest_prime


def reset(number):
    number = 0
    return number


def is_largest_prime(largest_prime, number):
    return is_prime(number) and number > largest_prime


print("Largest prime number in 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda' is: ",
      largest_prime_number('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))
print("Largest prime number in 'abcds' is: ", largest_prime_number('abcds'))
