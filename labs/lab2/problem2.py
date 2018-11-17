# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.


def is_prime(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, p):
        if p % i == 0:
            return False
    return True


def get_primes(my_list):
    return [p for p in my_list if is_prime(p)]


print(get_primes([i for i in range(1, 100)]))