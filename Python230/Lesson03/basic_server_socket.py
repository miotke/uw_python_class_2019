""" Basic server socket in Python """

import socket

local_server_address = '127.0.0.1'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
server_socket.bind((local_host, 5000))

server_socket.listen()

# Needs a client socket to accpet
server_socket.accept()

