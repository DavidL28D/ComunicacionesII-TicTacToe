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
        
        t = tablero()
        print('Esperando que el jugador enemigo coloque una ficha..')

        for i in range(3):
            self.fase_preparacion(t, conn)

        print('Fase de preparacion terminada..')
        t.mostrar_tablero()
        print('')

        while True:
            
            print('Esperando jugada enemiga...')
            message = conn.recv(1024)
            message = message.decode()
            print("Mensaje Recibido: ", message)
            message = input(str("Mensaje a enviar: "))
            if message == "quit()":
                message = "Se ha abandonado la conexion"
                conn.send(message.encode())
                print("\n")
                break
            conn.send(message.encode())

