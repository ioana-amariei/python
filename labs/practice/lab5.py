# 1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:
# 	a) a-b
# 	b) a+b
# 	c) a/b
# 	d) a*b

# import sys

#
# if len(sys.argv) < 3:
#     print('Must insert <a> <b>')
#     raise Exception
#
# a = int(sys.argv[1])
# b = int(sys.argv[2])

# print(a - b)
# print(a + b)
# print(a / b)
# print(a * b)


# 2. Scrieti un script care primeste ca parametru de la linia de comanda un path
# si afiseaza primii 4096 bytes daca path-ul duce la un fisier,
# intrarile din acesta daca path-ul reprezinta un director
# si un mesaj de eroare daca path-ul nu este unul valid.


# import sys
# import os
#
# if len(sys.argv) < 2:
#     raise Exception
#
# path = sys.argv[1]
#
# if os.path.isdir(path):
#     try:
#         print(os.listdir(path))
#     except IOError:
#         print("Invalid path")
# elif os.path.isfile(path):
#     try:
#         f = open(path)
#         print(f.read(4096))
#         f.close()
#     except IOError:
#         print("Invalid path")


import os

# 3. Scrieti o functie care primeste ca parametru un nume de fisier.
# 	Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar,
# 	sub forma cheie [tab] valoare.


# def write_info_to(file_path):
#     try:
#         f = open(file_path, 'w+')
#         for elem in os.environ:
#             f.write(elem + '\t' + os.getenv(elem) + '\n')
#             print(elem + '\t' + os.getenv(elem) + '\n')
#         f.close()
#     except Exception as e:
#         print(str(e))


# write_info_to('os_environment_info.txt')

# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem,
#   parcurge recursiv structura de fisiere si directoare pe care acesta le contine
#   si afiseaza in consola toate path-urile pe care le-a parcurs.
# 	NU aveti voie sa folositi os.walk.


# def browse_recursively(path):
#     try:
#         print(path)
#         if os.path.isdir(path):
#             files_and_dirs = os.listdir(path)
#             for elem in files_and_dirs:
#                 browse_recursively(os.path.join(path, elem))
#     except IOError:
#         print("Invalid path")


# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand
#   un path catre un director de pe sistem
#   si un nume de fisier.
#
# Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca parametru,
#   utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si
#   tipul acestuia (FILE, DIRECTORY, UNKNOWN),
# 	separate de |. Fiecare path va fi scris pe cate o linie.

# import sys
# import os
#
# if len(sys.argv) < 3:
#     raise Exception
#
# path = sys.argv[1]
# file_to_write = sys.argv[2]
#
# for (root, directories, files) in os.walk(path):
#     for filename in files:
#         file_path = os.path.join(root, filename)
#         try:
#             f = open(file_to_write, 'a')
#             if os.path.isfile(file_path):
#                 f.write(file_path + ' | FILE\n')
#             else:
#                 f.write(file_path + ' | UNKNOWN\n')
#             f.close()
#         except Exception as e:
#             print(str(e))
#
#     for directory in directories:
#         directory_path = os.path.join(root, directory)
#         try:
#             f = open(file_to_write, 'a')
#             if os.path.isfile(directory_path):
#                 f.write(directory_path + ' | DIRECTORY\n')
#             else:
#                 f.write(directory_path + ' | UNKNOWN\n')
#             f.close()
#         except Exception as e:
#             print(str(e))


# 6. Scrieti un script care primeste 3 parametri de la consola.
# 	Primul va fi un path catre un fisier,
#   al doilea un path catre un director iar
#   al treilea va fi dimensiunea unui buffer.
# 	Scriptul va copia fisierul dat ca parametru in directorul dat ca parametru,
#   utilizand un buffer de marimea celui de-al treilea parametru, in bytes.


import sys
import os

if len(sys.argv) < 4:
    raise IOError

file_path = sys.argv[1]
dir_path = sys.argv[2]
buffer_size = int(sys.argv[3])

if not os.path.isfile(file_path):
    raise TypeError

if not os.path.isdir(dir_path):
    raise TypeError

if buffer_size < 1:
    raise TypeError

try:
    f_read = open(file_path, 'rb')
    file_to_copy_name = os.path.basename(file_path)
    file_copy_path = os.path.join(dir_path, file_to_copy_name)
    f_write = open(file_copy_path, 'wb+')
    data = f_read.read(buffer_size)
    while data:
        f_write.write(data)
        data = f_read.read(buffer_size)
    f_write.close()
    f_read.close()
except Exception as e:
    print(str(e))
