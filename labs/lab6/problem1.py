# Write a function that extracts the words from a given text as a parameter.
# 	A word is defined as a sequence of alpha-numeric characters.
import re


def extract_words(text):
    # pattern = re.compile('\w+\')
    # words = re.findall(pattern, text)

    # return words

    return re.split("[^a-z'A-Z0-9]+", text)


print(extract_words("Today I'm shopping for 2 notebooks and 10 kilos of onions"))

