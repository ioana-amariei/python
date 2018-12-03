# 1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie
# (din intervalul [a, b] , unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul
# (in minute, cu doua zecimale). Programul va rula la infinit.
from random import randint
import time


def print_elapsed_running_time(a, b):
    start_time = time.time()

    while True:
        x = randint(a, b)
        time.sleep(x)
        running_time = time.time() - start_time
        print("%.2f" % running_time)


print_elapsed_running_time(2, 5)
