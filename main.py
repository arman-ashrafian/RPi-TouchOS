import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import requests
import json
from open_weather import OWM

LAMP_URL = "https://5658d085.ngrok.io"
ETH_ADDY = "0xaddfc1233fe9909e159715ac179a6ba4a470a451"
ETHPLORER_API = "freekey"

# import ui files here
from mainwindow import Ui_MainWindow 
from lamp import Ui_Lamp
from crypto import Ui_Crypto
from weather import Ui_Weather

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		## connect buttons
		self.button_lamp.clicked.connect(lambda: self.lamp_clicked())
		self.button_exit.clicked.connect(lambda: self.exit_clicked())
		self.button_crypto.clicked.connect(lambda: self.crypto_clicked())
		self.button_weather.clicked.connect(lambda: self.weather_clicked())

		# show
		self.showFullScreen()

	def lamp_clicked(self):
		lampWindow = LampWindow()
		self.close()

	def crypto_clicked(self):
		cryptoWindow = CryptoWindow()
		self.close()

	def weather_clicked(self):
		weatherWindow = WeatherWindow()
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
		self.button_back.setEnabled(False)
		mainWindow = MainWindow()
		self.close()

class CryptoWindow(QWidget, Ui_Crypto):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# eth request
		self.eth_req = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD&e=Coinbase"
		# eth account request
		self.eth_req_account = "https://api.ethplorer.io/getAddressInfo/{}?apiKey={}".format(ETH_ADDY, ETHPLORER_API)

		# btc request
		self.btc_req = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=Coinbase"

		# connect buttons
		self.button_back.clicked.connect(lambda: self.button_back_pressed())

		# show
		self.showFullScreen()

		# set eth & btc price
		self.set_eth_price()
		self.set_btc_price()

		# set up timers for price updates
		self.timer_eth = QtCore.QTimer()
		self.timer_eth.timeout.connect(self.set_eth_price)

		self.timer_btc = QtCore.QTimer()
		self.timer_btc.timeout.connect(self.set_btc_price)

		self.timer_eth.start(20000)	# 20 seconds
		self.timer_btc.start(20000) # 20 seconds

	def button_back_pressed(self):
		self.button_back.setEnabled(False)
		mainWindow = MainWindow()
		self.close()

	def set_eth_price(self):
		resp = requests.get(self.eth_req)
		data = json.loads(resp.text)

		# set price
		eth_price = data['RAW']['ETH']['USD']['PRICE']
		self.label_eth_price.setText('$ {:,.2f}'.format(eth_price))

		# set delta
		eth_delta = data['RAW']['ETH']['USD']['CHANGEPCT24HOUR']
		eth_delta_sign = '+'
		self.label_eth_delta.setStyleSheet('color:green')
		if eth_delta < 0: 
			eth_delta_sign = ''
			self.label_eth_delta.setStyleSheet('color:red')
		self.label_eth_delta.setText('(%s%.2f %%)' % (eth_delta_sign, eth_delta))

		self.set_eth_balance(eth_price)

	def set_eth_balance(self, currentPrice):
		resp = requests.get(self.eth_req_account)
		data = json.loads(resp.text)

		eth_balance = data['ETH']['balance']
		usd_balance = currentPrice * eth_balance

		self.label_ethbalance.setText('ETH: %.4f' % eth_balance)
		self.label_usdbalance.setText('USD: $%.2f' % usd_balance)

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

class WeatherWindow(QWidget, Ui_Weather):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		# connect buttons
		self.button_back.clicked.connect(lambda: self.button_back_pressed())

		# show
		self.showFullScreen()

		# weather
		self.city = "Laguna Niguel"
		self.owm = OWM(self.city)
		self.display_weather()

		# weather update timer
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.display_weather)
		self.timer.start(300000) # 5 minutes

	def button_back_pressed(self):
		self.button_back.setEnabled(False)
		mainWindow = MainWindow()
		self.close()

	def display_weather(self):
		weather = self.owm.get_weather()

		# city name
		self.label_city.setText(self.city)

		# temp
		temp = weather.get_temperature('fahrenheit')['temp']
		temp = "{:.0f}".format(temp)
		self.label_temp.setText(temp + '°')

		# icon
		icon = weather.get_weather_icon_name()
		self.label_icon.setPixmap(PyQt5.QtGui.QPixmap('ui/weather icons/{}.png'.format(icon)))
		self.label_icon.show()

		# status
		status = weather.get_detailed_status()
		self.label_status.setText(status)

		# max temp
		max_temp = weather.get_temperature('fahrenheit')['temp_max']
		max_temp = "{:.0f}".format(max_temp)
		self.label_max_temp.setText(max_temp + '°')

		# min temp
		min_temp = weather.get_temperature('fahrenheit')['temp_min']
		min_temp = "{:.0f}".format(min_temp)
		self.label_min_temp.setText(min_temp + '°')

		# humidity
		hum = weather.get_humidity()
		self.label_humidity.setText('{}%'.format(hum))

def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.showFullScreen()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()