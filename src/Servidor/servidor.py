import socket
import struct
import sys
import json
import time
from Motor.tablero import tablero

class server():

    def __init__(self):

        self.iniciar()

    def anunciar_servidor(self):

        grupo_multicast = '224.0.0.1'
        puerto_multicast = 3000

        direccion_bind = '0.0.0.0'
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        membership = socket.inet_aton(grupo_multicast) + socket.inet_aton(direccion_bind)

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((direccion_bind, puerto_multicast))
        print("Esperando un jugador...")
        message, address = sock.recvfrom(255)

        TCP_IP = str(address[0])
        print('- Conectado a jugador enemigo con ip: {0}'.format(TCP_IP))
        print('- Mensaje del enemigo: {0}'.format(message.decode()))

        sock.close()

        return TCP_IP

    def preparar(self, t, s):
        
        message = t.preparar_tablero(1)
        print('\nResultado')
        t.mostrar_tablero()
        print('')
        s.send(message.encode())
        print('Esperando que el jugador enemigo coloque una ficha..')

    def fase_preparacion(self, t, s):

        message = s.recv(1024)
        message = message.decode()
        coordenadas = message.split(',')
        t.poner_ficha(int(coordenadas[0]), int(coordenadas[1]), 2)
        self.preparar(t, s)

    def iniciar(self):

        TCP_IP = self.anunciar_servidor()
        TCP_PORT = 5005

        MESSAGE = "Hola {0}, Estamos conectados mediante TCP".format(TCP_IP)

        # inicia la conexion tcp
        s = socket.socket()
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE.encode())

        t = tablero()
        self.preparar(t, s)
        for i in range(2):
            self.fase_preparacion(t, s)

        message = s.recv(1024)
        message = message.decode()
        coordenadas = message.split(',')
        t.poner_ficha(int(coordenadas[0]), int(coordenadas[1]), 2)

        print('Fase de preparacion terminada..')
        t.mostrar_tablero()
        print('')
        

        while True:
            message = input(str("Mensaje a enviar: "))
            if message == "quit()":
                message = "Se ha abandonado la conexión"
                s.send(message.encode())
                print("\n")
                break
            s.send(message.encode())

            print('Esperando jugada enemiga..')
            message = s.recv(1024)
            message = message.decode()
            print("Recibido: ", message)


