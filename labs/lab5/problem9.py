# 9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem:
#
#     versiunea de python folosita.
#           Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ===" iar daca se foloseste
#           Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
#     numele user-ului care a executat scriptul,
#     path-ul complet al scriptului.
#     path-ul directorului in care se afla scriptul,
#     tipul sistemului de operare,
#     numarul de core-uri,
#     directoarele din PATH-ul procesului cate unul pe linie

import sys
import os

if "major=2" in str(sys.version_info):
    print(sys.version_info + ("=== Python 2 ===",))
elif "major=3" in str(sys.version_info):
    print(sys.version_info + ("Running under Py3",))
print("Username: ")
print("Absolute script path: " + os.path.realpath(__file__))
print("Absolute directory path: " + os.path.dirname(os.path.abspath(__file__)))

if os.name == "nt":
    print("Operating system type: Windows")
elif os.name == "posix":
    print("Operating system type: Mac or Solaris")

print("Number of CPUs: " + str(os.cpu_count()))

print("Current process path directories: ")
path = '.'
for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current):
        print(current)
