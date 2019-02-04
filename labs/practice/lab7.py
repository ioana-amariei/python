# 1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie
# (din intervalul [a, b] , unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul
# (in minute, cu doua zecimale). Programul va rula la infinit.
import random
import time
import os, hashlib


def print_elapsed_running_time(a, b):
    start_time = time.time()

    while True:
        seconds = random.randint(a, b)
        time.sleep(seconds)
        running_time = time.time() - start_time
        print("%.2f" % running_time)


# print_elapsed_running_time(1, 10)

#   Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare.
#   Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt.

def find_duplicate_files(path):
    def hash_file(path, block_size=65536):
        my_file = open(path, 'rb')
        hasher = hashlib.md5()
        buf = my_file.read(block_size)

        while len(buf) > 0:
            hasher.update(buf)
            buf = my_file.read(block_size)
        my_file.close()

        return hasher.hexdigest()

    start_time = time.time()
    duplicates = {}

    for (root, directories, files) in os.walk(path):
        for filename in files:
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                file_hash = hash_file(file_path)
                if file_hash in duplicates:
                    f = open('duplicates.txt', 'a')
                    f.write(file_path)
                    f.write('\n')
                    f.close()
                    duplicates[file_hash].append(file_path)
                else:
                    duplicates[file_hash] = [file_path]

    running_time = time.time() - start_time
    print("%.2f" % running_time)
    return duplicates


# find_duplicate_files('C:\\facultate\\an3\\sem1\\python\\python')


#   Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date
#   despre toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele informatii:
#   nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul
#   (in format human-readable) si calea absoluta catre fisier.

def files_info_to_json(path):
    def hash(hash_type, path, block_size=65536):
        my_file = open(path, 'rb')
        hasher = 0
        if hash_type is 'md5':
            hasher = hashlib.md5()
        elif hash_type is 'sha256':
            hasher = hashlib.sha256()
        else:
            return
        buf = my_file.read(block_size)

        while len(buf) > 0:
            hasher.update(buf)
            buf = my_file.read(block_size)
        my_file.close()

        return hasher.hexdigest()

    elements = os.listdir(path)

    for element in elements:
        element_path = os.path.join(path, element)
        creation_time = os.path.getmtime(element_path)
        human_readable_time = time.localtime(creation_time)

        f = open('info.json', 'a')
        if os.path.isfile(element_path):
            f.write('{\n\t')
            f.write('\"file_name\":\"' + element + '\",\n')
            f.write('\"file_md5\":\"' + hash('md5', element_path) + '\",\n')
            f.write('\"file_sha256\":\"' + hash('sha256', element_path) + '\",\n')
            f.write('\"file_size\":\"' + str(os.path.getsize(element_path)) + '\",\n')
            f.write('\"creation_time\":\"' + str(human_readable_time) + '\",\n')
            f.write('\"absolute_path\":\"' + element_path + '\"\n')
            f.write('},\n')
        f.close()


# files_info_to_json('C:\\facultate\\an3\\sem1\\python\\python\\labs')

# 7. Sa se simuleze extragerea 6/49.


def loto():
    numbers = list(range(1, 50))
    extracted = []

    for i in range(1, 7):
        random_number = random.randint(0, len(numbers) - 1)
        number = numbers.pop(random_number)
        extracted.append(number)

    return extracted


print(loto())