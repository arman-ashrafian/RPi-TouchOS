import PyQt5
from PyQt5.QtWidgets import *
import sys

# import ui file here
from mainwindow import Ui_MainWindow 

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()