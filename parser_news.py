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
				article = self.get_state_text(title['href'])
			except Exception as e:
				article = e

			try:
				self.write_state(title.text, article, picture)
			except Exception as ex:
				print('waiting', ex)
				time.sleep(3)

	def write_state(self, title, text_state, picture):
		from telegraph import Telegraph

		telegraph = Telegraph()

		telegraph.create_account(short_name='1337')

		response = telegraph.create_page(
		    str(title),
		    html_content= str(picture) + str(text_state)
		)
		

		print('https://telegra.ph/{}'.format(response['path']))

	def get_state_text(self, url):

		req = requests.get(url)

		reuslt_html = ''

		soup = BeautifulSoup(req.text, "html.parser")
		flag_article = False
		for paragrah in soup.findAll('div', {"class": "article__block"}):
			if paragrah['data-type'] == 'text':
				if paragrah['data-type'] == 'article' and flag_article is False:
					flag_article == True
					print()
				if paragrah['data-type'] == 'article' and flag_article:
					break
				reuslt_html += str(paragrah.text) + '\n'
				# print(paragrah.text)
		return reuslt_html

		

class BeInCryptoApi():

	def __init__(self):
		 self.link = 'https://beincrypto.ru/news/'

	def start_parse(self):
		pass

	def test(self):
		req = requests.get(self.link)

		soup = BeautifulSoup(req.text, "html.parser")

		all_states = soup.findAll('article', {"class": "multi-news-card bb-1 d-lg-flex flex-lg-column mb-5"})

		for state in all_states:
			
			title = state.find('h3').find('a').text
			image = state.find('amp-img')['src']
			image = f'<img src="{image}">'
			link = state.find('a')['href']
			text = self.get_state_text(link)
			self.write_state(title, image, text)
			# print(title)
			# print(image)

	def get_state_text(self, link):
		req = requests.get(link)

		soup = BeautifulSoup(req.text, "html.parser")

		state_text = ""

		states = soup.find('div', {"class": "entry-content-inner"})

		for p in states.findAll('p'):
			if p.find('amp-ad') is not None or p.find('amp-img') is not None or p.find('span') is not None:
				continue
			state_text += str(p) + '\n'

		return state_text

	def write_state(self, title, image, text):
		from telegraph import Telegraph

		telegraph = Telegraph()

		telegraph.create_account(short_name='1337')

		# print(str(image) + '\n' + str(text))

		try:
			response = telegraph.create_page(
		    str(title),
		    html_content=str(image) + '\n' + str(text))
			print('https://telegra.ph/{}'.format(response['path']))
		except Exception as e:
			print(str(image) + '\n' + str(text))
			print(e)
		

		
