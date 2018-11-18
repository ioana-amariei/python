# 1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
# 	a) a-b
# 	b) a+b
# 	c) a/b
# 	d) a*b


import sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
    raise TypeError

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a - b)
print(a + b)
print(a * b)

try:
    result = int(a / b)
    print(result)
except (Exception, ArithmeticError, TypeError) as e:
    print(str(e))
