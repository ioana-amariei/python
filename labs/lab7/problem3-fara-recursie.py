#   Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare.
#   Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt.
import os
import hashlib
import time


def hash_file(path, block_size=65536):
    my_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = my_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = my_file.read(block_size)
    my_file.close()

    return hasher.hexdigest()


def append_path_to_file(path, filename):
    try:
        f = open(filename, "a+")
        f.write(path)
        f.write('\n')
    except IOError:
        print("Error: can\'t find file or write data")
    else:
        f.close()


def get_files(directory):
    files = []
    items = os.listdir(directory)
    for item in items:
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files.append(item)

    return files


def find_duplicates(directory):
    start_time = time.time()
    duplicates = {}
    files = get_files(directory)
    for file in files:
        path = os.path.join(directory, file)
        file_hash = hash_file(path)
        if file_hash in duplicates:
            append_path_to_file(path, "output.txt")
            duplicates[file_hash].append(path)
        else:
            duplicates[file_hash] = [path]
    running_time = time.time() - start_time
    print("%.2f" % running_time)

    return duplicates


find_duplicates("C:\\facultate\\an3\\sem1\\python\\python\\labs")