import PyQt5
from PyQt5.QtWidgets import *
import sys
import requests
import json

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

		# show
		self.showFullScreen()

	def lamp_clicked(self):
		lampWindow = LampWindow()
		self.close()

	def crypto_clicked(self):
		cryptoWindow = CryptoWindow()
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

		# show
		self.showFullScreen()

	def button_on_pressed(self):
		# send post request to lamp server
		requests.post(LAMP_URL + "/on/")

	def button_off_pressed(self):
		requests.post(LAMP_URL + "/off/")

	def button_back_pressed(self):
		mainWindow = MainWindow()
		self.close()

class CryptoWindow(QWidget, Ui_Crypto):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# eth request
		self.eth_req = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD"
		# btc request
		self.btc_req = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD"

		# connect buttons
		self.button_back.clicked.connect(lambda: self.button_back_pressed())

		# show
		self.showFullScreen()

		# set eth & btc price
		self.set_eth_price()
		self.set_btc_price()

	def button_back_pressed(self):
		mainWindow = MainWindow()
		self.close()

	def set_eth_price(self):
		resp = requests.get(self.eth_req)
		data = json.loads(resp.text)

		# set price
		self.label_eth_price.setText('$ {:,.2f}'.format(data['RAW']['ETH']['USD']['PRICE']))

		# set delta
		eth_delta = data['RAW']['ETH']['USD']['CHANGEPCT24HOUR']
		eth_delta_sign = '+'
		self.label_eth_delta.setStyleSheet('color:green')
		if eth_delta < 0: 
			eth_delta_sign = ''
			self.label_eth_delta.setStyleSheet('color:red')
		self.label_eth_delta.setText('(%s%.2f %%)' % (eth_delta_sign, eth_delta))

	def set_btc_price(self):
		resp = requests.get(self.btc_req)
		data = json.loads(resp.text)

		# set price
		self.label_btc_price.setText('$ {:,.2f}'.format(data['RAW']['BTC']['USD']['PRICE']))

		# set delta
		btc_delta = data['RAW']['BTC']['USD']['CHANGEPCT24HOUR']
		btc_delta_sign = '+'
		self.label_btc_delta.setStyleSheet('color:green')
		if btc_delta < 0: 
			btc_delta_sign = ''
			self.label_btc_delta.setStyleSheet('color:red')
		self.label_btc_delta.setText('(%s%.2f %%)' % (btc_delta_sign, btc_delta))

def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.showFullScreen()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()