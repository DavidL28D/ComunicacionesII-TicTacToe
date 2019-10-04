import socket
import struct
import syslog
import json
import time
from Motor.tablero import tablero

class client():

    def __init__(self):

        self.iniciar()

    def obtener_interfaz_red(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        TCP_IP = s.getsockname()[0]
        s.close()

        return TCP_IP

    def preparar(self, t, s):
        
        message = t.preparar_tablero(2)
        print('\nResultado')
        t.mostrar_tablero()
        print('')
        s.send(message.encode())
        print('Esperando que el jugador enemigo coloque una ficha..')

    def fase_preparacion(self, t, s):

        message = s.recv(1024)
        message = message.decode()
        coordenadas = message.split(',')
        t.poner_ficha(int(coordenadas[0]), int(coordenadas[1]), 1)
        self.preparar(t, s)

    def iniciar(self):

        grupo_multicast = '224.0.0.1'
        puerto_multicast = 3000
        TCP_IP = self.obtener_interfaz_red()
        TCP_PORT = 5005
        
        # iniciar conexion tcp
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        message = "Juguemos puto"
        sock.sendto(message.encode(), (grupo_multicast, puerto_multicast))
        sock.close()
        s.bind((TCP_IP, TCP_PORT))
        s.listen()
        conn, addr = s.accept()
        print ('- Conectado a jugador enemigo con ip: {0}'.format(addr[0]))
        data = conn.recv(1024)
        print ("- Mensaje del enemigo:", data.decode())
        
        # Fase de preparacion
        t = tablero()
        print('Esperando que el jugador enemigo coloque una ficha..')

        for i in range(3):
            self.fase_preparacion(t, conn)

        print('Fase de preparacion terminada..')
        t.mostrar_tablero()
        print('')
        # Fase de preparacion

        while True:

            print('Esperando jugada enemiga...')

            message = conn.recv(1024)
            message = message.decode()
            coordenadas = message.split(',')

            if(coordenadas[0] == 'Jugador enemigo ha vencido.'):
                t.validar_movimiento(int(coordenadas[1]), int(coordenadas[2]), int(coordenadas[3]), int(coordenadas[4]), 1)
                print('\nJugador enemigo ha vencido.')
                print('Resultado')
                t.mostrar_tablero()
                print('')
                break

            t.validar_movimiento(int(coordenadas[0]), int(coordenadas[1]), int(coordenadas[2]), int(coordenadas[3]), 1)

            while True:
                print('Mi Turno..')
                t.mostrar_tablero()
                print('')

                xi = int(input("Ingrese la coordenada x de la pieza a mover: "))
                yi = int(input("Ingrese la coordenada y de la pieza a mover: "))
                xf = int(input("Ingrese la coordenada x la casilla a donde quieres mover la pieza: "))
                yf = int(input("Ingrese la coordenada y la casilla a donde quieres mover la pieza: "))

                if(t.validar_movimiento(yi, xi, yf, xf, 2)):
                    break

            print('\nResultado')
            t.mostrar_tablero()
            print('')

            if(t.comprobar_ganador(yf,xf)):

                print('He ganado')
                message = "Jugador enemigo ha vencido.,"+str(yi)+','+str(xi)+','+str(yf)+','+str(xf)
                conn.send(message.encode())
                print("")
                break

            message = str(yi)+','+str(xi)+','+str(yf)+','+str(xf)
            conn.send(message.encode())

