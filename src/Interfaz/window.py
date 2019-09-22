import sys
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QListWidget, QStackedWidget, QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import *
from Servidor.servidor import server
from Cliente.cliente import client
from Interfaz.button import Button
from Interfaz.menu import MenuWidget
from Interfaz.game import GameWidget

class Window(QMainWindow):
	
	def __init__(self):		
		super().__init__()
		self.width = 800
		self.height = 600
		self.initUI()
		
	def initUI(self):
		self.setGeometry(100,100,self.width,self.height)
		self.setWindowTitle("TicTacToe")
		#Creacion del Widget Apilado
		self.windows = QStackedWidget(self)	

		#Creacion de los items a apilar
		self.menu = MenuWidget(self)
		self.game = GameWidget()

		#Agregar los widgets al Widget apilado
		self.windows.addWidget(self.menu)
		self.windows.addWidget(self.game)

		self.setCentralWidget(self.windows)
			
		self.show()

	def play(self):
		self.windows.setCurrentIndex(1)
		print ("Play")
		#server()
				

	def join(self):
		#client()
		pass
