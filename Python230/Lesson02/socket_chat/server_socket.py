""" Server Socket """

import socket

# Creates a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

# Binds an IP address, in the case localhost, to the server socket
server_socket.bind(('127.0.0.1', 50001))

# Listens for a single connection from a client socket
server_socket.listen(1)

# Creates a connection and accepts client sockets
connection, client_addres = server_socket.accept()

