import socket
import struct
import sys
import json
import time

class server():

    def __init__(self):

        self.iniciar()

    def iniciar(self):

        multicast_group = '224.3.29.71'
        server_address = ('', 1234)

        # crea el socket por el cual se van a transferir los datagramas
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # enlazar socket
        sock.bind(server_address)

        # tiempo de espera de respuesta (1 minuto)
        sock.settimeout(60)

        # añadiendo el socket al grupo multicast
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        try:

            # recibiendo respuestas
            print('Esperando por jugador...')

            data, address = sock.recvfrom (1234)
            print(f'Retador: {data} desde {address}')

            message = 'SIVAPUTO'
            sock.sendto(message.encode('utf-8'), address)

            sock.settimeout(3)
        
        except socket.timeout:

            print("No existe jugadores disponibles")
            sock.close()
        
        else:

            while True:

                time.sleep(1)

                try:

                    data, address = sock.recvfrom(1234)
                    print(f'Retador: {data} desde {address}')
                    message = 'Conectado'
                    sock.sendto(message.encode('utf-8'), address)

                except socket.timeout:

                    print('El retador se desconecto.')
                    sock.close()
                    break

                else:
                    pass
                '''
                if band:
                    message = input('Escribir: ')
                    sock.sendto(message.encode(), multicast_group)
                else:
                    data, address = sock.recvfrom(1024)
                    data = json.loads(data.decode())
                    print(f'Jugador invitado: {data.get("a")} desde {address}')
                    print(f'Jugador invitado: {data.get("b")} desde {address}')
                #data, address = sock.recvfrom(1024)
                #print(f'Jugador invitado: {data} desde {address}')
                '''

            