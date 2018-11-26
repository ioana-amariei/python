# Write a function that receives as a parameter a string of text characters and a list of regular expressions and
# returns a list of strings that match on at least one regular expression given as a parameter.
import re


def match_at_least_one_regex(s, patterns):
    for pattern in patterns:
        if re.search(pattern, s) is not None:
            return True

    return False


def strings_that_matches_at_least_one_patterns(list_of_strings, patterns):
    return [s for s in list_of_strings if match_at_least_one_regex(s, patterns)]


print(strings_that_matches_at_least_one_patterns(["I", "payed", "150 dollars for 1 night", "at the museum"],
                                                 ["(\d+)"]))
