import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import *
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
		self.setGeometry(100,100,self.width,self.height)
		self.setWindowTitle("TicTacToe")
		self.createButtons()
		self.createTitle()
		self.createHorizontalLayout()
		self.createVerticalLayout()
		home = QWidget()
		home.setLayout(self.vbox)		
		self.setCentralWidget(home)	
		self.show()

	def play(self):
		server()		

	def join(self):
		client()

	def createButtons(self):
		self.playBtn = Button('Play',self)
		self.joinBtn = Button('Join',self)

	def createTitle(self):
		self.title = QLabel()
		self.title.setText("TicTacToe")
		self.title.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
		self.title.setAlignment(Qt.AlignCenter)
	
	def createHorizontalLayout(self):
		self.hbox = QHBoxLayout()	
		self.hbox.addStretch(1)
		self.hbox.addWidget(self.playBtn)		
		self.hbox.addStretch(1)
		self.hbox.addWidget(self.joinBtn)	
		self.hbox.addStretch(1)

	def createVerticalLayout(self):
		self.vbox = QVBoxLayout()
		self.vbox.addStretch(2)
		self.vbox.addWidget(self.title)
		self.vbox.addStretch(2)
		self.vbox.addLayout(self.hbox)	
		self.vbox.addStretch(4)		