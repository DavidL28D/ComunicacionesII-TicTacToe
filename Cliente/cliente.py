import socket
import struct
import sys

class client():

    def __init__(self):

        self.iniciar()

    def iniciar(self):

        multicast_group = ('224.3.29.71', 10000)
        message='Epa quiero jugar...'

        # Create the datagram socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        sock.settimeout(3)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        try:

            # Send data to the multicast group
            sock.sendto(message.encode('utf-8'), multicast_group)

            print('Enviando reto...')
            # Look for responses from all recipients
            while True:
                try:
                    data, server = sock.recvfrom(16)
                except socket.timeout:
                    print('No hay jugadores')
                    break
                else:
                    print(f'Jugador host: {data} desde {server}')

        finally:
            print('Cerrando Socket')
            sock.close()
