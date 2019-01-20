# Al doilea program query_files.py va interoga tabele cu informatii.
# Va putea sa afiseze informatii despre fisiere
#     dupa size - lista de fisiere ce au acelasi size
#     dupa nume - lista de fisiere ce au acelasi nume
#     dupa hash - lista de fisiere ce au acelasi hash
#     dupa creation_time - fisiere create dupa o anumita data.

#    * informatiile returnate pentru un fisier vor fi complete:
# id_file, locatie, nume_fisier, size_fisier, creation_time, md5_pe_continut_fisier

import sqlite3
import time

connection = sqlite3.connect('files.db')
cursor = connection.cursor()

print('lista de fisiere ce au acelasi size')
for row in connection.execute('SELECT DISTINCT f1.file_id, location, f1.file_name, f1.file_size, f1.creation_time, f1.md5_hash '
                              'FROM file f1, file f2, files, location '
                              'WHERE f1.file_id == files.file_id AND files.location_id == location.location_id '
                              'AND f1.file_size == f2.file_size '
                              'AND f1.file_id != f2.file_id'):
    print(row)

print('----------------------------------')
print('lista de fisiere ce au acelasi nume')
for row in connection.execute('SELECT DISTINCT f1.file_id, location, f1.file_name, f1.file_size, f1.creation_time, f1.md5_hash '
                              'FROM file f1, file f2, files, location '
                              'WHERE f1.file_id == files.file_id AND files.location_id == location.location_id '
                              'AND f1.file_name == f2.file_name '
                              'AND f1.file_id != f2.file_id'):
    print(row)


print('----------------------------------')
print('lista de fisiere ce au acelasi hash')
for row in connection.execute('SELECT DISTINCT f1.file_id, location, f1.file_name, f1.file_size, f1.creation_time, f1.md5_hash '
                              'FROM file f1, file f2, files, location '
                              'WHERE f1.file_id == files.file_id AND files.location_id == location.location_id '
                              'AND f1.md5_hash == f2.md5_hash '
                              'AND f1.file_id != f2.file_id'):
    print(row)


last_time = (2019, 1, 19, 17, 3, 38, 1, 48, 0)
seconds = time.mktime(last_time)

print('----------------------------------')
print('fisiere create dupa o anumita data')
for row in connection.execute('SELECT f1.file_id, location, f1.file_name, f1.file_size, f1.creation_time, f1.md5_hash '
                              'FROM file f1, files, location '
                              'WHERE f1.file_id == files.file_id AND files.location_id == location.location_id '
                              'AND CAST(f1.creation_time AS REAL) > (?)', (seconds, )):
    print(row)