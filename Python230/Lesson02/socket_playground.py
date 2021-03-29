import socket

def service_by_name():
    """ Check what port is used by what service """
    ssh =  socket.getservbyname('ssh')
    http = socket.getservbyname('http')

    print(f'ssh: {ssh}')
    print(f'http: {http}')


def service_by_port():
    """ Check what service is used by what port """
    ssh = socket.getservbyport(22)
    https = socket.getservbyport(443)

    print(f'22: {ssh}')
    print(f'443: {https}')


def host_name():
    """ Get the host of a machine """
    hostname = socket.gethostname()
    print(f'Hostname is {hostname}')


def host_name_by_ip():
    """ Get the IP address of a machine """
    ip = socket.gethostbyname(socket.gethostname())
    print(f'Hostname by IP = {ip}')


def playing_with_sockets():
    """ Getting info about a socket. This is just the basics """
    foo = socket.socket()
    print(foo)
    print(foo.family)
    print(foo.proto)
    print(foo.type)


def get_constants(prefix):
    """ Filtered mapping of socket module constants to their name """
    return {
            getattr(socket, name): name
            for name in dir(socket) if name.startswith(prefix)
        }


if __name__ == '__main__':
    service_by_name()
    service_by_port()
    host_name()
    host_name_by_ip()
    playing_with_sockets()
    get_constants('AF')
