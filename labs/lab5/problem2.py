# 2. Scrieti un script care primeste ca parametru de la linia de comanda un path
# si afiseaza primii 4096 bytes daca path-ul duce la un fisier,
# intrarile din acesta daca path-ul reprezinta un director
# si un mesaj de eroare daca path-ul nu este unul valid.


import sys
import os

if len(sys.argv) < 2 or len(sys.argv) > 2:
    raise TypeError

path = sys.argv[1]
if os.path.isdir(path):
    try:
        print(os.listdir(path))
    except IOError:
        print("Folder not found or path is incorrect")
elif os.path.isfile(path):
    try:
        f = open(path)
        print(f.read(4096))
        f.close()
    except IOError:
        print("File not found or path is incorrect")
