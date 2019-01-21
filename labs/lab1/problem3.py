# Write a function that returns the number of words in a string.
# Words are separated by spaces, punctuation marks (, ;, ? ! . )


def is_delimiter(char):
    return char in ',;?!.'


def number_of_words_from(string):
    for character in string:
        if is_delimiter(character):
            string = string.replace(character, ' ')

    words = string.split(' ')
    return len(words)


print("number of words: ", number_of_words_from("bdc!dijfvn.kfke"))
print("number of words: ", number_of_words_from("bdc dijfvn,,kfke"))