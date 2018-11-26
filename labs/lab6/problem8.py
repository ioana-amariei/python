# Write a function that recursively scrolls a directory and displays those files whose name
# 	matches a regular expression given as a parameter or contains a string that matches the same expression.
# 	Files that satisfy both conditions will be prefixed with ">>"
import os
import re


def fully_matches_regex(file_name, pattern):
    if re.match(pattern + "$", file_name) is not None:
        return True
    return False


def matches_regex(file_name, pattern):
    if re.search(pattern, file_name) is not None:
        return True
    return False


def get_files_that_match_pattern(path, pattern):
    for (root, directories, files) in os.walk(path):
        for file_name in files:
            if os.path.isfile(file_name):
                if fully_matches_regex(file_name, pattern) and matches_regex(file_name, pattern):
                    print(">>" + file_name)
                elif fully_matches_regex(file_name, pattern) or matches_regex(file_name, pattern):
                    print(file_name)


get_files_that_match_pattern("C:\\facultate\\an3\\sem1\\python\\python\\labs", "problem5.p")
