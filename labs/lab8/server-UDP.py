# 2a. Implement using the socket module (UDP), a server that when is receiving a UDP packet (datagram)
# writes in a text file the following information: time and date, address, port, length, md5 hash of the content
# in hex format, sha256.

import socket
import hashlib
import time


def compute_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def compute_sha256(my_string):
    m = hashlib.sha256()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


ADDRESS = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start = time.clock()
server_socket.bind((ADDRESS, PORT))

while True:
    (data, address) = server_socket.recvfrom(1024)

    data_length = len(data)
    content = data.decode()
    md5_hash_of_content = compute_md5(content)
    sha256_hash_of_content = compute_sha256(content)

    my_file = open('message_from_client_info.txt', 'a+')
    my_file.write('Time: ' + time.asctime(time.localtime(time.clock() - start)) + ' seconds\n')
    my_file.write('Address: ' + address[0] + '\n')
    my_file.write('Port: ' + str(address[1]) + '\n')
    my_file.write('Length: ' + str(data_length) + '\n')
    my_file.write('Content: ' + content + '\n')
    my_file.write('md5 hash of content: ' + md5_hash_of_content + '\n')
    my_file.write('sha256 hash of content: ' + sha256_hash_of_content + '\n')
    my_file.write('-----------------------------------\n')

    my_file.close()
