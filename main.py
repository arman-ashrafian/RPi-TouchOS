import PyQt5
from PyQt5.QtWidgets import *
import sys
import requests

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

LAMP_URL = "https://5658d085.ngrok.io"

# import ui file here
from mainwindow import Ui_MainWindow 
from lamp import Ui_Lamp
from crypto import Ui_Crypto

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		## connect buttons
		self.button_lamp.clicked.connect(lambda: self.lamp_clicked())
		self.button_exit.clicked.connect(lambda: self.exit_clicked())
		self.button_crypto.clicked.connect(lambda: self.crypto_clicked())

	def lamp_clicked(self):
		lampWindow = LampWindow()
		lampWindow.showFullScreen()
		self.close()

	def crypto_clicked(self):
		cryptoWindow = CryptoWindow()
		cryptoWindow.showFullScreen()
		self.close()

	def exit_clicked(self):
		sys.exit()

class LampWindow(QWidget, Ui_Lamp):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# connect button
		self.button_on.clicked.connect(lambda: self.button_on_pressed())
		self.button_off.clicked.connect(lambda: self.button_off_pressed())
		self.button_back.clicked.connect(lambda: self.button_back_pressed())

	def button_on_pressed(self):
		# send post request to lamp server
		requests.post(LAMP_URL + "/on/")

	def button_off_pressed(self):
		requests.post(LAMP_URL + "/off/")

	def button_back_pressed(self):
		mainWindow = MainWindow()
		mainWindow.showFullScreen()
		self.close()

class CryptoWindow(QWidget, Ui_Crypto):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		m = PlotCanvas(self, width=5, height=4)
		m.move(100,100)

		# connect buttons
		self.button_back.clicked.connect(lambda: self.button_back_pressed())

	def button_back_pressed(self):
		mainWindow = MainWindow()
		mainWindow.showFullScreen()
		self.close()

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.showFullScreen()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()