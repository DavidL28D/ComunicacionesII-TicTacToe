
import sys
from Cliente.cliente import client
from Servidor.servidor import server
from Interfaz.window import Window
from PyQt5.QtWidgets import QApplication
import PyQt5
#import qdarkystyle

def main():
	#Punto de entrada a la aplicacion--------------------------------------------------------------------------------
	print(PyQt5.QtWidgets.QStyleFactory.keys())
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	#app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	win = Window()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
    
    

