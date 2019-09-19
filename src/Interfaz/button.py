import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

class Button(QPushButton):
    width = 100
    heigth = 30
    def __init__(self, name, posx, posy,QMainWindow):
        super().__init__(self)
        self.setGeometry(self.width,self.heigth)
        self.move(posx,posy)

