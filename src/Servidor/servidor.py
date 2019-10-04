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

    def enviar_jugada(self, t, s):
        pass

    def iniciar(self):

        TCP_IP = self.anunciar_servidor()
        TCP_PORT = 5005

        MESSAGE = "Hola {0}, Estamos conectados mediante TCP".format(TCP_IP)

        # inicia la conexion tcp
        s = socket.socket()
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE.encode())

        # Fase de preparacion
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
        # Fase de preparacion

        while True:
            
            while True:

                print('Mi Turno..')
                t.mostrar_tablero()
                print('')

                xi = int(input("Ingrese la coordenada x de la pieza a mover: "))
                yi = int(input("Ingrese la coordenada y de la pieza a mover: "))
                xf = int(input("Ingrese la coordenada x la casilla a donde quieres mover la pieza: "))
                yf = int(input("Ingrese la coordenada y la casilla a donde quieres mover la pieza: "))

                if(t.validar_movimiento(yi, xi, yf, xf, 1)):
                    break

            print('\nResultado')
            t.mostrar_tablero()
            print('')

            if(t.comprobar_ganador(yf,xf)):

                print('He ganado')
                message = "Jugador enemigo ha vencido.,"+str(yi)+','+str(xi)+','+str(yf)+','+str(xf)
                s.send(message.encode())
                print("")
                break
                
            message = str(yi)+','+str(xi)+','+str(yf)+','+str(xf)
            s.send(message.encode())

            print('Esperando jugada enemiga..')
            message = s.recv(1024)
            message = message.decode()
            coordenadas = message.split(',')

            if(coordenadas[0] == 'Jugador enemigo ha vencido.'):
                t.validar_movimiento(int(coordenadas[1]), int(coordenadas[2]), int(coordenadas[3]), int(coordenadas[4]), 2)
                print('\nJugador enemigo ha vencido.')
                print('Resultado')
                t.mostrar_tablero()
                print('')
                break

            t.validar_movimiento(int(coordenadas[0]), int(coordenadas[1]), int(coordenadas[2]), int(coordenadas[3]), 2)


