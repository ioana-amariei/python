# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem,
#   parcurge recursiv structura de fisiere si directoare pe care acesta le contine
#   si afiseaza in consola toate path-urile pe care le-a parcurs.
# 	NU aveti voie sa folositi os.walk.


import os

def browse_recursively(path):
    try:
        print(path)
        if os.path.isdir(path):
            files_and_dirs = os.listdir(path)
            for elem in files_and_dirs:
                browse_recursively(os.path.join(path, elem))
    except IOError:
        print("Invalid path")


browse_recursively("C:\\facultate\\an3\\sem1\\python\\python")
