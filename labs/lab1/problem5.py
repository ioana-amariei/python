# Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)


def is_special(character):
    return character in ['\r', '\t', '\n', '\a', '\b', '\f', '\v']


def contains_special_characters(string):
    for character in string:
        if is_special(character):
            return True

    return False


print("Are special characters in 'abcvdsh\nbvdj\r'", contains_special_characters("abcvdsh\nbvdj\r"))
print("Are special characters in 'abcv'", contains_special_characters("abcv"))