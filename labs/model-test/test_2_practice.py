# Sa se scrie o functie cu numele problema1 ce returneaza o lista ordonata crescator ce contine toate cuvintele
# din sirul de caractere s dat ca parametru. Un cuvant este format din: litere mici si mari, cifre si
# caracterul underscore '_'.

import re
import os
import urllib
from urllib import request
import hashlib
import zipfile
import socket


def problema1(s):
    word_pattern = '(\w+)'
    words = re.findall(word_pattern, s)

    words.sort()
    return words


# print(problema1('@c3sta 3st3, un cuvant_.'))


# Sa se scrie o functie cu numele problema2 care primeste ca parametri un sir de caractere s si un
# sir de caractere url ce reprezinta un link http.
# Sa se returneze True daca s se gaseste in continutul de la link-ul http dat, sau False altfel.


def problema2(s, url):
    response = urllib.request.urlopen(url)
    content = response.read()

    return s.encode() in content


# print(problema2("facebook", "https://mbasic.facebook.com/"))
# print(problema2(s="2014 hackaday.com. All Rights Reserved.", url="http://retro.hackaday.com/"))
# print(problema2(s="google", url="https://www.google.com.hk"))
# print(problema2(s="gooogli", url="https://www.google.com.hk"))


# Sa se scrie o functie cu numele problema3 care primeste ca parametru un sir de caractere path ce
# reprezinta path-ul unui director.
# Sa se returneze o lista ordonata crescator cu hash-urile md5 ale tuturor fisierelor din director ( nerecursiv ).


def problema3(path):
    def hash(filepath, block_size=4096):
        try:
            hash = hashlib.md5()
            f = open(filepath, 'rb')
            while True:
                data = f.read(block_size)
                if len(data) is 0:
                    break
                hash.update(data)
            f.close()
            return hash.hexdigest()
        except:
            return ''

    files = os.listdir(path)
    md5 = []

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            md5.append(hash(file_path))

    md5.sort()

    return md5

# print(problema3('C:\\facultate\\an3\\sem1\\python\\python\\labs'))


# Sa se scrie o functie cu numele problema4 ce primeste ca parametru un sir de caractere path ce
# reprezinta path-ul unei arhive zip.
# Sa se returneze o lista ordonata crescator cu numele fisierelor care au size dupa compresie mai mare de 1 KB
# ( 1000 de bytes ).

def problema4(path):
    list = []
    z = zipfile.ZipFile(path)

    for i in z.infolist():
        if i.compress_size > 1000:
            name = os.path.basename(i.filename)
            list.append(name)

    list.sort()
    return list


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

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.send(text.encode())
    message = s.recv(32).decode()

    hash_message = get_sha256(message)
    s.send(hash_message.encode())

    final_message = s.recv(32).decode()
    s.close()

    return final_message




