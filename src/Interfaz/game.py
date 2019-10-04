import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFrame, QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QIcon

class GameWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.initParameters()
    
    def initParameters(self):
        #Crea un Layout horizontal que tendrá tres columnas
        self.horizontalBox = QHBoxLayout()
        #Columna 1 Informacion del Jugador 1
        self.player1Label = self.createPlayerLabel("Jugador 1",self.horizontalBox)  
        #Columna 2 zona del tablero del juego
        self.boardSpace=QFrame()
        self.boardSpace.setStyleSheet('background-image: url(/home/yeison/Projects/Python/TicTacToe/src/Interfaz/tablero.png);' 
                                      "background-repeat: no-repeat;"
                                      "background-position:center;")
        self.boardSpace.setFixedWidth(400)
        
        self.verticalBox = QVBoxLayout() 

        """self.board = QLabel()
        self.boardPixmap = QPixmap('/home/yeison/Projects/Python/TicTacToe/src/Interfaz/tablero.png')
        self.board.setPixmap(self.boardPixmap)
        self.board.setAlignment(Qt.AlignCenter)
        
        

        self.verticalBox.addWidget(self.board)
        self.boardSpace.setLayout(self.verticalBox)"""

        #self.horizontalBox.addWidget(self.board)
        self.horizontalBox.addWidget(self.boardSpace)
        #Columna 3 Informacion del Jugador 2
        self.player2Label = self.createPlayerLabel("Jugador 2",self.horizontalBox)
        #Agrega el Layout al QFrame 
        self.setLayout(self.horizontalBox)
        #Muestra el QFrame
        self.show()

    #Funcion que crea el Label un jugador
    def createPlayerLabel(self,label,box):
        l = QLabel()
        l.setText(label)
        l.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        l.setAlignment(Qt.AlignHCenter)
        box.addWidget(l)
        return l
        