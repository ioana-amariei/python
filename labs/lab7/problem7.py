# 7. Sa se simuleze extragerea 6/49.
from random import randint


def extract_6_49():
    numbers = list(range(1, 50))
    extracted = []

    for i in range(1, 7):
        n = numbers.pop(randint(0, len(numbers) - 1))
        extracted.append(n)

    return extracted


print(extract_6_49())
