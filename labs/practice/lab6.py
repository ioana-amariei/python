 # Write a function that extracts the words from a given text as a parameter.
# 	A word is defined as a sequence of alpha-numeric characters.
import re, os


def extract_words(text):
    # pattern = re.compile('\w+\')
    # words = re.findall(pattern, text)

    # return words

    return re.split("[^\w]+", text)


# print(extract_words("Today I'm shopping for 2 notebooks and 10 kilos of onions"))


# Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.

def get_substrings_that_matches(regex, text, x):
    # pattern = re.compile(regex)
    # matches = re.findall(pattern, text)
    # return [m for m in matches if len(m) is x]
    return [word for word in re.findall(regex, text) if len(word) is x]


# print(get_substrings_that_matches('(\w+)', "I am a computer science student", 7))


# Write a function that receives as a parameter a string of text characters and a list of regular expressions and
# returns a list of strings that match on at least one regular expression given as a parameter.


def strings_that_matches_at_least_one_patterns(list_of_strings, patterns):
    def match_at_least_one_regex(s, patterns):
        for pattern in patterns:
            if re.search(pattern, s) is not None:
                return True

        return False

    return [s for s in list_of_strings if match_at_least_one_regex(s, patterns)]


# print(strings_that_matches_at_least_one_patterns(["I", "payed", "150 dollars for 1 night", "at the museum"],
#                                                  ["(\d+)"]))


# Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
# 	Censorship means replacing characters from odd positions with *.

def censure_words(text):
    words = extract_words(text)
    censored = []

    for word in words:
        pattern = '^[aeiou].*[aeiou]$'
        if re.match(pattern, word, flags=re.IGNORECASE):
            word = word.replace(word[0], '*')
            word = word.replace(word[len(word) - 1], '*')
            censored.append(word)

    return censored


# print(censure_words('Ana are mere dulci, are apatie'))

# Write a function that recursively scrolls a directory and displays those files whose name
# 	matches a regular expression given as a parameter or contains a string that matches the same expression.
# 	Files that satisfy both conditions will be prefixed with ">>"

def get_files_that_match_pattern(regex):
    def fully_matches_regex(file_name, pattern):
        if re.match(pattern + "$", file_name) is not None:
            return True
        return False

    def matches_regex(file_name, pattern):
        if re.search(pattern, file_name) is not None:
            return True
        return False

    path = 'C:\\facultate\\an3\\sem1\\python\\python\\labs'

    for (root, directories, files) in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                if fully_matches_regex(filename, regex) and matches_regex(filename, regex):
                    print('>>' + filename)
                elif fully_matches_regex(filename, regex) or matches_regex(filename, regex):
                    print(filename)


print(get_files_that_match_pattern('problem5.py'))



