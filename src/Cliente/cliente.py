import socket
import struct
import syslog
import json
import time

class client():

    def __init__(self):

        self.iniciar()

    def iniciar(self):

        multicast_group = ('224.3.29.71', 1234)
        
        # crea el socket por el cual se van a transferir los datagramas
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # tiempo de espera de respuesta (5 min)
        sock.settimeout(3)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


        try:

            # enviando la data al grupo multicast
            print('Enviando reto...')
            message='Epa quiero jugar'
            sock.sendto(message.encode('utf-8'), multicast_group)
            data, server = sock.recvfrom(1234)
            print(f'Host: {data} desde {server}')

        except socket.timeout:

            print("No existe jugadores disponibles")
            sock.close()

        else:

            while True:

                time.sleep(1)

                try:

                    message = 'Conectado.'
                    sock.sendto(message.encode('utf-8'), server)
                    data, server = sock.recvfrom(1234)
                    print(f'Host: {data} desde {server}')
                    
                except socket.timeout:

                    print('El host se desconecto.')
                    sock.close()
                    break

                else:
                    pass
                    
                '''
                #message = input('Escribir: ')
                #sock.sendto(message.encode('utf-8'), multicast_group)

                lisA = [1,2,3,4]
                lisB = [5,6,7,8,9]
                message = input('Escribir: ')
                message = json.dumps({"a":lisA, "b":lisB})
                sock.sendto(message.encode(), multicast_group)
                '''
