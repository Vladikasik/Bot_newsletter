import requests 
from config import *
from bs4 import BeautifulSoup
import time

class RiaNewsApi():

	def __init__(self):
		self.link = 'https://ria.ru/economy/'

	def start_parse(self):
		pass

	def test(self):
		req = requests.get(self.link)
		soup = BeautifulSoup(req.text, "html.parser")
		result = soup.findAll('div', {"class": "list-item"})
		for state_block in result:
			print(1)
			state = state_block.find('div', {"class": "list-item__content"})
			title = state.find('a', {'class': 'list-item__title color-font-hover-only'})
			picture = state.find('picture').find('img')

			try:
				self.write_state(title.text, picture)
			except Exception as ex:
				print('waiting')
				time.sleep(3)

	def write_state(self, title, picture):
		from telegraph import Telegraph

		telegraph = Telegraph()

		telegraph.create_account(short_name='1337')

		response = telegraph.create_page(
		    str(title),
		    html_content=str(picture)
		)
		

		print('https://telegra.ph/{}'.format(response['path']))

	def get_state_text(self, url):
		pass

class BeInCryptoApi():

	def __init__(self):
		 self.link = 'https://beincrypto.ru/news/'

	def start_parse(self):
		pass

	def test(self):
		pass
