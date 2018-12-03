# compute is_prime time
import timeit

primes = [8191, 131071, 524287]
repeat = 1
number = 10


def is_prime_time():
    setup_code = '''from problem2 import is_prime'''
    test_code = '''is_prime(524287)'''

    times = timeit.repeat(setup=setup_code,
                          stmt=test_code,
                          repeat=repeat,
                          number=number)

    print('is_prime time: {}' . format(min(times)))


def is_prime_optimized_time():
    setup_code = '''from problem2 import is_prime_optimized'''
    test_code = '''is_prime_optimized(524287)'''

    times = timeit.repeat(setup=setup_code,
                          stmt=test_code,
                          repeat=repeat,
                          number=number)

    print('is_prime_optimized time: {}'.format(min(times)))


is_prime_time()
is_prime_optimized_time()



