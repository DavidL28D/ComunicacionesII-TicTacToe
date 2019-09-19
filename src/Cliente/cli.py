import socket
import struct
import sys
import threading

class client():

    def __init__(self):

        self.iniciar()

    def iniciar(self):

        multicast_group = ('224.3.29.71', 10000)
        

        # Create the datagram socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        sock.settimeout(3)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        # Send data to the multicast group
        print('Enviando reto...')
        message='Epa quiero jugar...'
        sock.sendto(message.encode('utf-8'), multicast_group)

        try:
            data, server = sock.recvfrom(16)
            print(f'Jugador host: {data} desde {server}')
        except socket.timeout:
            print(f'Todo el mundo esta cagao.')
            print("Cerrando el socket")
            sock.close()
        else:
            while True:
                message = input('Escribir: ')
                sock.sendto(message.encode('utf-8'), multicast_group)
