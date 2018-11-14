# Write a function that receives a char_len integer and a variable number of strings (strings) and
# check that each two neighboring strings follow the following rule: the second string starts with
# the last char_len characters of the first string (like the word game pheasant).


def get_last_characters_from(string, char_len):
    if len(string) == char_len:
        return string

    return string[-char_len:]


def get_first_characters_from(string, char_len):
    return string[0:char_len]


def is_valid_next_word(char_len, *strings):
    if char_len == 0 or len(strings) == 0:
        return False

    if len(strings) == 0 and char_len > 0:
        return False

    for string in strings:
        if len(string) < char_len:
            return False

    previous_element = get_last_characters_from(strings[0], char_len)
    next_element = get_first_characters_from(strings[1], char_len)

    if previous_element != next_element:
        return False

    size = len(strings)
    for index in range(2, size):

        previous_element = get_last_characters_from(strings[index - 1], char_len)
        next_element = get_first_characters_from(strings[index], char_len)

        if previous_element != next_element:
            return False

    return True


print("Valid list of strings: 'elefant, antena, enache' with length 3: ", is_valid_next_word(3, "elefant", "antena", "enache"))
print("Valid list of strings: 'alalal, alal, ala' with length 4: ", is_valid_next_word(4, "alalal", "alal", "ala"))
print("Valid list of strings: 'eat, attach, chorus, usa' with length 2: ", is_valid_next_word(2, "eat", "attach", "chorus", "usa"))
print("Valid list of strings: 'elefant, antena, enache' with length 0: ", is_valid_next_word(0, "elefant", "antena", "enache"))
print("Valid with no strings and length 0: ", is_valid_next_word(5))
