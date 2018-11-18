# 6. Scrieti un script care primeste 3 parametri de la consola.
# 	Primul va fi un path catre un fisier,
#   al doilea un path catre un director iar
#   al treilea va fi dimensiunea unui buffer.
# 	Scriptul va copia fisierul dat ca parametru in directorul dat ca parametru,
#   utilizand un buffer de marimea celui de-al treilea parametru, in bytes.
import ntpath
import sys
import os

if len(sys.argv) < 4 or len(sys.argv) > 4:
    raise TypeError

file_path = sys.argv[1]
folder_path = sys.argv[2]
buffer_size = int(sys.argv[3])

if not os.path.isfile(file_path):
    raise TypeError

if not os.path.isdir(folder_path):
    raise TypeError

if buffer_size < 1:
    raise TypeError

try:
    f_read = open(file_path, "rb")
    file_copy_path = os.path.join(folder_path, ntpath.basename(file_path))
    f_write = open(file_copy_path, "wb+")
    data = f_read.read(buffer_size)
    while data:
        f_write.write(data)
        data = f_read.read(buffer_size)
    f_write.close()
    f_read.close()
except Exception as e:
    print(str(e))
