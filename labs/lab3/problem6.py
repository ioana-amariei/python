# 6. Fie un dictionar global
# 				{
#
# 					"+": lambda a, b: a + b,
#
# 					"*": lambda a, b: a * b,
#
# 					"/": lambda a, b: a / b,
#
# 					"%": lambda a, b: a % b
#
# 				}
# 	Sa se construiasca o functie apply_operator(operator, a, b) care va aplica peste a si b regula specificata de
#   dictionarul global.
# 	Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara modificarea functiei.


global_dictionary = {"+": lambda a, b: a + b, "*": lambda a, b: a * b, "/": lambda a, b: a / b, "%": lambda a, b: a % b,
                     "**": lambda a, b: a ** b}


def apply_operator(operator, a, b):
    operation = global_dictionary[operator]
    return operation(a, b)


print(apply_operator("+", 1, 2))
print(apply_operator("*", 5, 2))
print(apply_operator("**", 5, 2))
