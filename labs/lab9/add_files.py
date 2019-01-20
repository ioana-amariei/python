# Primul program add_files.py va primi ca parametru o locatie in care se afla fisiere.
# Pentru fiecare fisier din aceasta locatie se vor adauga:
#       In tabelul locatie: id_locatie, locatie ( cale director )
#       In tabelul files: id_file, id_locatie
#       In tabelul file_info: id_file, nume_fisier, size_fisier, creation_time, md5_pe_continut_fisier


import argparse
import sqlite3
import os
import sys
import hashlib

parser = argparse.ArgumentParser(description='Process file path.')
parser.add_argument('path', type=str, help='path')
args = parser.parse_args()

PATH = sys.argv[1]


def create_location_table(location_info):
    connection = sqlite3.connect(':memory:')

    connection.execute("CREATE TABLE location(location_id, location)")
    connection.executemany("INSERT INTO location(location_id, location) VALUES (?, ?)", location_info)

    print('LOCATION TABLE\n')
    cursor = connection.cursor()
    for row in cursor.execute("SELECT location_id, location FROM location"):
        print(row)

    connection.commit()
    connection.close()


def create_files_table(files_info):
    connection = sqlite3.connect(':memory:')

    connection.execute("CREATE TABLE files(file_id, location_id)")
    connection.executemany("INSERT INTO files(file_id, location_id) VALUES (?, ?)", files_info)

    print('FILES TABLE\n')
    cursor = connection.cursor()
    for row in cursor.execute("SELECT file_id, location_id FROM files"):
        print(row)

    connection.commit()
    connection.close()


def create_file_table(file_info):
    connection = sqlite3.connect(':memory:')

    connection.execute("CREATE TABLE file(file_id, file_name, file_size, creation_time, md5_hash)")
    connection.executemany("INSERT INTO file(file_id, file_name, file_size, creation_time, md5_hash) VALUES (?, ?, ?, ?, ?)", file_info)

    print('FILE_INFO TABLE\n')
    cursor = connection.cursor()
    for row in cursor.execute("SELECT file_id, file_name, file_size, creation_time, md5_hash FROM file"):
        print(row)

    connection.commit()
    connection.close()


def get_files_from(location):
    files = []
    items = os.listdir(location)
    for item in items:
        path = os.path.join(location, item)
        if os.path.isfile(path):
            # files must contain absolute path for each file
            files.append((item, path))

    return files


def hash_file(path, block_size=65536):
    my_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = my_file.read(block_size)

    while len(buf) > 0:
        hasher.update(buf)
        buf = my_file.read(block_size)
    my_file.close()

    return hasher.hexdigest()


# id_file, nume_fisier, size_fisier, creation_time, md5_pe_continut_fisier
def add_files_info_to_tables(path):
    files = get_files_from(path)

    location_id = 0
    file_id = 1
    for file in files:
        file_name = file[0]
        file_path = file[1]
        file_size = os.path.getsize(file_path)
        file_creation_time = os.path.getmtime(file_path)
        file_md5 = hash_file(file_path)

        location_info = [(location_id, file_path)]
        files_info = [(file_id, location_id)]
        file_info = [(file_id, file_name, file_size, file_creation_time, file_md5)]

        create_location_table(location_info)
        create_files_table(files_info)
        create_file_table(file_info)

        location_id += 1
        file_id += 1


add_files_info_to_tables(PATH)
