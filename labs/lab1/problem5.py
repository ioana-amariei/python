# Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)


def contains_special_characters(string):
    result = [c for c in string if c in '\r\t\n\a\b\f\v']
    return len(result) > 0


print(contains_special_characters("abcvdsh\nbvdj\r"))
print(contains_special_characters("abcv"))