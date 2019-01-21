# 3. Scrieti o functie care primeste ca parametru un nume de fisier.
# 	Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar,
# 	sub forma cheie [tab] valoare.


import os


def write_info_to(file_path):
    try:
        f = open(file_path, 'w+')
        for elem in os.environ:
            f.write(elem + '\t' + os.getenv(elem) + '\n')
            print(elem + '\t' + os.getenv(elem) + '\n')
        f.close()
    except Exception as e:
        print(str(e))


write_info_to('os_environment_info.txt')
