#   Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date
#   despre toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele informatii:
#   nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul
#   (in format human-readable) si calea absoluta catre fisier.
import time
import os, hashlib


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


files_info_to_json('C:\\facultate\\an3\\sem1\\python\\python\\labs')
