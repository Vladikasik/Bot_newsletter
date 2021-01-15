import requests 
from config import *

class RiaNewsApi():

	def __init__(self):
		self.link = 'https://ria.ru/economy/'

	def start_parse(self):
		pass

	def test(self):
		req = requests.get(self.link)
		

class WorldWideApi():

	def __init__(self):
		self.link = f'http://newsapi.org/v2/top-headlines?country=ru&apiKey={worldwide_api_key}'

class MeduzaNewsApi():

	def __init__(self):
		import meduza