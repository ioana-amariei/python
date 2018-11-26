# Verify using a regular expression whether a string is a valid CNP.
import re


def is_valid_cnp(input_string):
    pattern = "^[1-8][0-9]{10}(0[1-9]|[1-4][0-9]|[5][0-2])$"
    if re.match(pattern, input_string) is not None:
        return True
    return False


print(is_valid_cnp("2890224336522"))
print(is_valid_cnp("1899999999930"))
print(is_valid_cnp("9890214336527"))
print(is_valid_cnp("9890214336555"))
