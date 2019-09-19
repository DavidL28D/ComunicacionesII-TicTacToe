import socket
import struct

class server():

    def __init__(self):

        self.iniciar()

    def iniciar(self):

        multicast_group = '224.3.29.71'
        server_address = ('', 10000)

        # Creando el socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the server address
        sock.bind(server_address)

        # Tell the operating system to add the socket to the multicast group
        # on all interfaces.
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        # Receive/respond loop
        print('Esperando por jugador...')

        data, address = sock.recvfrom(1024)
        print(f'Jugador invitado: {data} desde {address}')

        print(f'Aceptando el desafio de {address}')
        message = 'SI VA PUES'
        sock.sendto(message.encode('utf-8'), address)

        while True:
            
            data, address = sock.recvfrom(1024)
            print(f'Jugador invitado: {data} desde {address}')
            
