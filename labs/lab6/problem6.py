# Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
# 	Censorship means replacing characters from odd positions with *.
import re
from problem1 import extract_words

def censor(text):
    words = extract_words(text)
    censored = []

    for word in words:
        pattern = '^[aeiou].*[aeiou]$'
        if re.match(pattern, word, flags=re.IGNORECASE):
            word = word.replace(word[0], '*')
            word = word.replace(word[len(word) - 1], '*')
            censored.append(word)

    return censored


print(censor("Ana is an effective online reader"))