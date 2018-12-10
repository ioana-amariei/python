# Adauga intr-o arhiva toate fisierele cu size mai mic de 100kb si modificate cu cel mult 5 minute in urma
#   (nu va fi adaugat acelasi fisier de 2 ori).
import os
import zipfile


root = 'C:\\facultate\\an3\\sem1\\python\\python\\labs\\lab7\\archive-test'
archive_path = 'C:\\facultate\\an3\\sem1\\python\\python\\labs\\lab7\\archive-test\\archive.zip'
max_size = 100 * 1000
max_time = 50000 * 60000

files_and_dirs = os.listdir(root)
files = []
for item in files_and_dirs:
    path = os.path.join(root, item)
    if os.path.isfile(path):
        files.append(item)

for file in files:
    path = os.path.join(root, file)
    file_size = os.path.getsize(path)
    creation_time = os.path.getmtime(path)
    if file_size < max_size and creation_time < max_time:
        zip = zipfile.ZipFile(archive_path, 'a')
        zip.write(archive_path, os.path.basename(path))
        zip.close()

