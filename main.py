import PyQt5
from PyQt5.QtWidgets import *
import sys
import requests

LAMP_URL = "https://5658d085.ngrok.io"

# import ui file here
from mainwindow import Ui_MainWindow 
from lamp import Ui_Lamp

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		## connect buttons
		self.button_lamp.clicked.connect(lambda: self.lamp_clicked())
		self.button_exit.clicked.connect(lambda: self.exit_clicked())

	def lamp_clicked(self):
		lampWindow = LampWindow()
		lampWindow.showFullScreen()
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



def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.showFullScreen()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()