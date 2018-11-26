# Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
# 	Censorship means replacing characters from odd positions with *.
import re
from problem1 import extract_words

def censor(text):
    # words = re.sub("[^\w]", " ",  text).split()
    words = extract_words(text)
    censored = []
    for word in words:
        censoredWordCharList = list(word)
        if re.match("^[aeiou].*[aeiou]$", word, flags=re.IGNORECASE):
            for i in range(0, len(word)):
                if i % 2 != 0:
                    censoredWordCharList[i] = '*'

        censoredWord = "".join(censoredWordCharList)
        censored.append(censoredWord)

    return ' '.join(censored)


print(censor("Ana is an effective online reader"))