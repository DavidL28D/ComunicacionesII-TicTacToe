import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton

class Button(QPushButton):
    height=60
    width = 100
    def __init__(self,label,window):
        super().__init__()        
        self.initParameters(100,500,label,window)

    def initParameters(self,posx,posy,label,window):
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)
        self.setText(label)
        self.show()
        if label == "Play":
            self.clicked.connect(window.play)
        if label == "Join":
            self.clicked.connect(window.join)