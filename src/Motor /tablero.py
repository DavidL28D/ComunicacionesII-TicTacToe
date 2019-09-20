class tablero:

    def __init__(self):

        self.tablero = self.crear_tablero()

    def crear_tablero(self):

        matrix = []

        for i in range(3):
            matrix.append([])
            for j in range(3):     
                matrix[i].append(0)

        return matrix

    def preparar_tablero(self):

        for i in range(6):

            print("*** Preparacion ***")
            self.mostrar_tablero()
            print("*** Preparacion ***\n")

            if( i%2 ==0 ):

                tipo = 1
                print("Jugador 1: ")

            else:

                tipo = 2
                print("Jugador 2: ")

            while(True):    

                x = int(input("Ingresa la coordenada x: "))
                y = int(input("Ingresa la coordenada y: "))

                if((x >= 0 and x<3) and (y >= 0 and y<3)):

                    if(self.tablero[y][x] == 0):

                        self.poner_ficha(y, x, tipo)
                        break

                    else:
                        print("\nYa existe una ficha en la posicion indicada")
                    
                else:
                    print("\nIncorrecto, intente nuevamente.")
            
            print("")


    def mostrar_tablero(self):

        for fila in self.tablero:
            print(" ".join(map(str, fila)))

    def poner_ficha(self, y, x, tipo):

        self.tablero[y][x] = tipo
        #print(self.comprobar_ganador(y,x))

    def mover_ficha(self, yi, xi, yf, xf, tipo):

        self.tablero[yf][xf] = tipo
        self.tablero[yi][xi] = 0

    def comprobar_ganador(self, y, x):

        t = self.tablero
        tipo = self.tablero[y][x]
        alfa = 1

        print("\n")
        for i in range(4):

            alfa = 1
            ax = x
            ay = y

            if(i==0): # Horizontal

                while(ax+1 < 3): # Horizontal Derecha

                    ax += 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break
                
                ax = x

                while(ax-1 >= 0): # Horizontal 
                    
                    ax -= 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

            elif(i==1): # Vertical

                while(ay-1 >= 0): # Vertical Arriba

                    ay -= 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

                ay = y

                while(ay+1 < 3): # Vertical Abajo

                    ay += 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

            elif(i==2): # Diagonal NE - SO

                while(ax+1 < 3 and ay-1 >= 0): # Diagonal NE
                    
                    ax += 1
                    ay -= 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

                ax = x
                ay = y
                
                while(ax-1 >=0 and ay+1 < 3): # Diagonal SO

                    ax -= 1
                    ay += 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

            elif(i==3): # Diagonal NO - SE

                while(ax-1 >= 0 and ay-1 >= 0): # Diagonal NO
                    
                    ax -= 1
                    ay -= 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

                ax = x
                ay = y
                
                while(ax+1 < 3 and ay+1 < 3): # Diagonal SE

                    ax += 1
                    ay += 1
                    atipo = t[ay][ax]

                    if(atipo == tipo):
                        alfa += 1
                    else:
                        break

            #print(alfa, ": Horizontal")
            #print(alfa, ": Vertical")
            #print(alfa, ": Diagonal /")
            #print(alfa, ": Diagonal \ ")

            if(alfa == 3):
                return True

        return False

