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


def create_tables():
    connection = sqlite3.connect('files.db')

    connection.execute("CREATE TABLE location(location_id INT, location FLOAT)")
    connection.execute("CREATE TABLE files(file_id INT, location_id INT)")
    connection.execute("CREATE TABLE file(file_id INT, file_name VARCHAR , file_size INT, creation_time REAL , md5_hash VARCHAR )")

    connection.commit()
    connection.close()


def insert_into_location(info):
    connection = sqlite3.connect('files.db')
    connection.executemany("INSERT INTO location(location_id, location) VALUES (?, ?)", info)
    connection.commit()
    connection.close()


def insert_into_files(info):
    connection = sqlite3.connect('files.db')
    connection.executemany("INSERT INTO files(file_id, location_id) VALUES (?, ?)", info)

    connection.commit()
    connection.close()


def insert_into_file(info):
    connection = sqlite3.connect('files.db')
    connection.executemany("INSERT INTO file(file_id, file_name, file_size, creation_time, md5_hash) VALUES (?, ?, ?, ?, ?)", info)
    connection.commit()
    connection.close()


def get_files_from(location):
    files = []
    items = os.listdir(location)
    for item in items:
        path = os.path.join(location, item)
        if os.path.isfile(path):
            file_name = item
            # files must contain absolute path for each file
            files.append((file_name, path))

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

        insert_into_location(location_info)
        insert_into_files(files_info)
        insert_into_file(file_info)

        location_id += 1
        file_id += 1


create_tables()
add_files_info_to_tables(PATH)
