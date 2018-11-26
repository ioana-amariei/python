# Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.
import re


def long_length_substrings(regex, text, x):
    return [word for word in re.findall(regex, text) if len(word) == x]


print(long_length_substrings("(\w+)", "I am a computer science student", 7))
