import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from Servidor.servidor import server
from Cliente.cliente import client
from Interfaz.button import Button
class Window(QMainWindow):

	def __init__(self):
		
		super().__init__()
		self.width = 800
		self.height = 600
		self.initUI()
		
	def initUI(self):
		#playBtn = Button('Play',100,30,self)
		#playBtn.clicked.connect(self.play)
		playBtn = QPushButton('Play',self)
		playBtn.resize(100,30)
		playBtn.move(50,350)
		playBtn.clicked.connect(self.play)

		joinBtn = QPushButton('Join',self)
		joinBtn.resize(100,30)
		joinBtn.move(200,350)
		joinBtn.clicked.connect(self.join)
		self.setGeometry(100,100,self.width,self.height)
		self.setWindowTitle("TicTacToe")
		
		self.show()

	def play(self):
		server()

	def join(self):
		client()