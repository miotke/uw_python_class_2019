""" Client Socket """

import socket

# Creates the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

# Makes a connection to the server socket
client_socket.connect(('127.0.0.1', 50001))

# Sends a mesage to the server socket
client_socket.sendall(b'hello?')

# Receivces the message from the server socket
client_socket.recv(64)

