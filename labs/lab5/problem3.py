# 3. Scrieti o functie care primeste ca parametru un nume de fisier.
# 	Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar,
# 	sub forma cheie [tab] valoare.


import os


def write_to_file(file_name):
    try:
        f = open(file_name, "w+")
        if os.path.isfile(file_name):
            for e in os.environ:
                f.write(e + "\t" + os.getenv(e) + "\n")
        f.close()
    except Exception as e:
        print(str(e))


write_to_file("environment.txt")
