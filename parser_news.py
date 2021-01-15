import requests 
from config import *

RiaNewsApi = 1
class RiaNewsApi():

	def __init__(self):
		self.link = 'https://ria.ru/economy/'

	def start_parse(self):
		pass

	def test(self):
		r = requests.get(self.link)
		with open('test.html', 'w', encoding='utf-8') as file:
			file.write(r.text)


class WorldWideApi():

	def __init__(self):
		self.link = f'http://newsapi.org/v2/top-headlines?country=ru&apiKey={worldwide_api_key}'

class MeduzaNewsApi():

	def __init__(self):
		import meduza