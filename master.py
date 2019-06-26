
import sys
from Cliente.cliente import client
from Servidor.servidor import server

if sys.argv[1] == 'jugar':

    server()

elif sys.argv[1] == 'unirse':

    client()

else:
    print("Opcion incorrecta")