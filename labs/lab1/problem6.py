#  Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.


def convert(initial_string):
    if initial_string[0].isupper():
        initial_string = replace_with_lowercase(initial_string)

    length = len(initial_string)
    for index in range(1, length):
        if initial_string[index].isupper():
            initial_string = replace_with_underscore_and_lowercase(index, initial_string)

    return initial_string


def replace_with_lowercase(string):
    return string.replace(string[0], string[0].lower(), 1)


def replace_with_underscore_and_lowercase(index, string):
    return string.replace(string[index], '_' + string[index].lower())


print("Converted string: ", convert("CamelCase"))
print("Converted string: ", convert("camelCase"))
print("Converted string: ", convert("camelCaseNamingConvention"))
