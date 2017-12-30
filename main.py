import PyQt5
from PyQt5.QtWidgets import *
import sys

# import ui file here
from mainwindow import Ui_MainWindow 
from lamp import Ui_Lamp

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# possible windows
		self.lampWindow = LampWindow()

		## connect buttons
		self.button_lamp.clicked.connect(lambda: self.lamp_clicked())

	def lamp_clicked(self):
		self.lampWindow.show()
		self.hide()

class LampWindow(QWidget, Ui_Lamp):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# connect button
		self.button_on.clicked.connect(lambda: self.button_on_pressed())
		self.button_off.clicked.connect(lambda: self.button_off_pressed())


	def button_on_pressed(self):
		print("ON")

	def button_off_pressed(self):
		print("OFF")



def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()