import requests 
from config import *
from bs4 import BeautifulSoup

class RiaNewsApi():

	def __init__(self):
		self.link = 'https://ria.ru/economy/'

	def start_parse(self):
		pass

	def test(self):
		req = requests.get(self.link)
		soup = BeautifulSoup(req.text, "html.parser")
		result = soup.findAll('div', {"class": "list-item"})
		for page in result:
			a = page.findAll('div', {"class": "list-item__content"})
			b = a[0].findAll('title')
			print(a)
		

class WorldWideApi():

	def __init__(self):
		self.link = f'http://newsapi.org/v2/top-headlines?country=ru&apiKey={worldwide_api_key}'

	def start_parse(self):
		pass

	def test(self):
		print('test')
		req = requests.get(self.link)
		
class MeduzaNewsApi():

	def __init__(self):
		import meduza

	def start_parse(self):
		pass

	def test(self):
		pass