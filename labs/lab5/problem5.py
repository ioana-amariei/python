# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand
#   un path catre un director de pe sistem
#   si un nume de fisier.
#
# Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca parametru,
#   utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si
#   tipul acestuia (FILE, DIRECTORY, UNKNOWN),
# 	separate de |. Fiecare path va fi scris pe cate o linie.

import os
import sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
    raise TypeError

path = sys.argv[1]
file_to_write = sys.argv[2]

for (root, directories, files) in os.walk("."):
    for fileName in files:
        full_fileName = os.path.join(root, fileName)
        try:
            f = open(file_to_write, "a+")
            if os.path.isdir(fileName):
                f.write(full_fileName + " | " + "DIRECTORY\n")
            elif os.path.isfile(fileName):
                f.write(full_fileName + " | " + "FILE\n")
            else:
                f.write(full_fileName + " | " + "UNKNOWN\n")
            f.close()
        except Exception as e:
            print(str(e))
