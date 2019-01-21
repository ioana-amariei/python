# Sa se scrie o functie cu numele problema1 ce returneaza o lista ordonata crescator ce contine toate cuvintele
# din sirul de caractere s dat ca parametru. Un cuvant este format din: litere mici si mari, cifre si
# caracterul underscore '_'.

import re
import urllib
from urllib import request
import os
import hashlib
import zipfile
import socket


def problema1(s):
    list_with_words = re.split('\W', s)
    list_with_words.sort()
    return [e for e in list_with_words if e is not '']


# print(problema1('@c3sta 3st3, un cuvant_.'))


# Sa se scrie o functie cu numele problema2 care primeste ca parametri un sir de caractere s si un
# sir de caractere url ce reprezinta un link http.
# Sa se returneze True daca s se gaseste in continutul de la link-ul http dat, sau False altfel.


def problema2(s, url):
    response = urllib.request.urlopen(url)
    page_content = response.read()

    return s.encode() in page_content


# print(problema2("facebook", "https://mbasic.facebook.com/"))
# print(problema2(s="2014 hackaday.com. All Rights Reserved.", url="http://retro.hackaday.com/"))
# print(problema2(s="google", url="https://www.google.com.hk"))
# print(problema2(s="gooogli", url="https://www.google.com.hk"))


# Sa se scrie o functie cu numele problema3 care primeste ca parametru un sir de caractere path ce
# reprezinta path-ul unui director.
# Sa se returneze o lista ordonata crescator cu hash-urile md5 ale tuturor fisierelor din director ( nerecursiv ).


def problema3(path):
    directories = os.listdir(path)

    files = []
    for element in directories:
        full_path = os.path.join(path, element)
        if os.path.isfile(full_path):
            files.append(full_path)

    md5 = []
    for filename in files:
        my_file = open(filename, 'rb')
        hasher = hashlib.md5()
        buf = my_file.read(65536)

        while len(buf) > 0:
            hasher.update(buf)
            buf = my_file.read(65536)
        my_file.close()

        digest = hasher.hexdigest()
        md5.append(digest)

    md5.sort()
    return md5


# print(problema3('C:\\facultate\\an3\\sem1\\python\\python\\labs'))


# Sa se scrie o functie cu numele problema4 ce primeste ca parametru un sir de caractere path ce
# reprezinta path-ul unei arhive zip.
# Sa se returneze o lista ordonata crescator cu numele fisierelor care au size dupa compresie mai mare de 1 KB
# ( 1000 de bytes ).


def problema4(path):
    ordered_list = []
    z = zipfile.ZipFile(path)
    for i in z.infolist():
        if i.compress_size > 1000:
            name = os.path.basename(i.filename)
            ordered_list.append(name)

    ordered_list.sort()
    return ordered_list


# print(problema4('C:\\facultate\\an3\\sem1\\Introduction-to-.Net\\project\\CLMS\\CLMS\\clms.zip'))


# Sa se scrie o functie cu numele problema5 care primeste ca argumente un sir de caractere host,
# un numar port si un sir de caractere text.
# Sa se returneze raspunsul final de la server, ca si string, urmand urmatorul protocol definit:
# - clientul trimite continutul argumentului text la server
# - clientul va primi de la server un alt sir de caractere (de lungime 32)
# - clientul trimite serverului hash-ul sha256 al sirului primit anterior
# - clientul primeste raspunsul final de la server (de lungime 32) pe care il returneaza

def problema5(host, port, text):
    def get_sha256(text):
        hash = hashlib.sha256()
        hash.update(text.encode())
        return hash.hexdigest()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(text.encode())
    message = sock.recv(32).decode()
    sock.send(get_sha256(message).encode())
    message = sock.recv(32).decode()

    sock.close()
    return message

