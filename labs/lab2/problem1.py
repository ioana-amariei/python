# Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fibonacci_list = [0, 1]
    for index in range(2, n):
        fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])

    return fibonacci_list


print("Invalid input: ", fibonacci(-1))
print("First fibonacci number: ", fibonacci(1))
print("First " + str(2) + " fibonacci numbers: ", fibonacci(2))
print("First " + str(10) + " fibonacci numbers: ", fibonacci(10))
