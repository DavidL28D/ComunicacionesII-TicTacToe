import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFrame, QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import *

from Interfaz.button import Button

class MenuWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__()
        self.width = 800
        self.height = 600
        self.parent = parent
        self.initMenu()
    

    def initMenu(self):
        self.setGeometry(100,100,self.width,self.height)
        self.createButtons()
        self.createTitle()
        self.createHorizontalLayout()
        self.createVerticalLayout()
        self.setLayout(self.verticaBox)
        self.show()
    
    def createButtons(self):
        self.playBtn = Button('Play',self.parent)
        self.joinBtn = Button('Join',self.parent)

    def createTitle(self):
        self.title = QLabel()
        self.title.setText("TicTacToe")
        self.title.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
	
    def createHorizontalLayout(self):
        self.horizontalbox = QHBoxLayout()	
        self.horizontalbox.addStretch(1)
        self.horizontalbox.addWidget(self.playBtn)		
        self.horizontalbox.addStretch(1)
        self.horizontalbox.addWidget(self.joinBtn)	
        self.horizontalbox.addStretch(1)

    def createVerticalLayout(self):
        self.verticaBox = QVBoxLayout()
        self.verticaBox.addStretch(2)
        self.verticaBox.addWidget(self.title)
        self.verticaBox.addStretch(2)
        self.verticaBox.addLayout(self.horizontalbox)	
        self.verticaBox.addStretch(4)		