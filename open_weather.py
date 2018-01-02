# open weather map wrapper

import pyowm

class OWM:
	def __init__(self, city):
		API_KEY = "065b8b40e70bde7087ff44ea0ef8d5c1"
		self.owm = pyowm.OWM(API_KEY)
		self.observation = self.owm.weather_at_place('%s, ca, usa' % city)

	def get_weather(self):
		return self.observation.get_weather()