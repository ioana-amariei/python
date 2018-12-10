#   Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date
#   despre toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele informatii:
#   nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul
#   (in format human-readable) si calea absoluta catre fisier.
import os
import hashlib


def md5_hash(path, block_size=65536):
    my_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = my_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = my_file.read(block_size)
    my_file.close()

    return hasher.hexdigest()


def sha256_hash(path, block_size=65536):
    my_file = open(path, 'rb')
    hasher = hashlib.sha256()
    buf = my_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = my_file.read(block_size)
    my_file.close()

    return hasher.hexdigest()


def get_files(directory):
    files = []
    items = os.listdir(directory)
    for item in items:
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files.append(item)

    return files


def files_info_to_json(directory):
    f = open("info.json", "a+")
    f.write("{\n")
    f.write("\"files\":[\n")

    files = get_files(directory)
    for file in files:
        path = os.path.join(directory, file)
        file_name = file
        md5 = md5_hash(path)
        sha256 = sha256_hash(path)
        file_size = os.path.getsize(path)
        creation_time = os.path.getmtime(path)

        f.write("{\n")
        f.write("\"fileName\":" + "\"" + file_name + "\",\n")
        f.write("\"md5\":" + "\"" + str(md5) + "\",\n")
        f.write("\"sha256\":" + "\"" + str(sha256) + "\",\n")
        f.write("\"fileSize\":" + "\"" + str(file_size) + "\",\n")
        f.write("\"creationTime\":" + "\"" + str(creation_time) + "\",\n")
        f.write("\"absolutePath\":" + "\"" + path + "\",\n")
        f.write("},\n")

    f.write("]\n}")


files_info_to_json("C:\\facultate\\an3\\sem1\\python\\python\\labs")
