# Find The largest common divisor of multiple numbers.
# Define a function with variable number of parameters to resolve this.


def largest_common_divisor(*args):
    if (len(args)) == 0:
        return None

    a = args[0]
    for b in args[1:]:
        while b != 0:
            r = a % b
            a = b
            b = r
    return a


print("cmmdc(12, 16): ", largest_common_divisor(12, 16))
print("cmmdc(): ", largest_common_divisor())
print("cmmdc(25, 7): ", largest_common_divisor(25, 7))
