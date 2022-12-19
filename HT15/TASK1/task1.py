"""HT 15 TASK  # 1.  Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт
   https://www.expireddomains.net/domain-lists/ (з ним будьте обережні :подмигивание:
   :череп_и_кости:), вибираєте будь-яку на ваш вибір доменну зону і парсите список
    доменів з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно
    ураховуючи пагінацію). Всі отримані значення зберегти в CSV файл."""

import csv
import random
import time
from random import choice

import requests
from bs4 import BeautifulSoup


class Domains:
	"""Клас збирає інформацію з сайту та записує її у файл"""
	base_url = "https://www.expireddomains.net/"
	url = "godaddy-closeout-domains/?"
	all_domains = []
	session = requests.Session()

	def __init__(self, header=None):
		self.header = self.random_headers()

	def random_headers(self):

		desktop_agents = [
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

		return {'User-Agent': choice(desktop_agents),
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'uk - UA, uk; q = 0.9, en - US; q = 0.8, en;q = 0.7',
			'cache-control': 'no - cache',
			'pragma': 'no - cache',
			'sec-ch-ua': '"Google Chrome"; v = "107", "Chromium"; v = "107", "Not=A?Brand"; v = "24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"macOS"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same - origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1'
			}

	def get_information(self, number_page):
		"""Запит всієї інформації з сайту"""

		element = self.session.get(f"{self.base_url}{self.url}{number_page}", headers=self.header).content
		print(f"{self.base_url}{self.url}{number_page}")
		return element

	def parse(self, number_page):
		element = self.get_information(number_page)
		soup = BeautifulSoup(element, "lxml")
		table = soup.find('table', class_='base1')
		return table

	def get_header(self, tabl):
		"""Запис заголовків"""

		headers = []
		for header in tabl.find_all('th'):
			headers.append(header.text)
		return headers

	def get_rows(self, tabl):
		"""Запис рядків"""

		for row in tabl.find_all('tr')[1:]:
			td = row.find_all('td')
			row = [i.text.replace('\n', '') for i in td]
			self.all_domains.append(row)
		return

	def transformation(self):
		"""Перетворення отриманої інформації в список"""

		first_page = '#listing'
		tabl = self.parse(first_page)
		headers = self.get_header(tabl)
		self.all_domains.append(headers)
		self.get_rows(tabl)
		for page in range(25, 325, 25):
			time.sleep(random.randrange(10, 25))
			next_page = f'start={page}#listing'
			tabl = self.parse(next_page)
			self.get_rows(tabl)
		return self.all_domains

	def writer(self):
		"""Запис отриманої інформації в csv файл"""

		with open("basa.csv", 'w') as f:
			writer = csv.writer(f)
			for row in self.all_domains:
				writer.writerow(row)


if __name__ == '__main__':
	domain = Domains()
	time.sleep(random.randrange(30, 45))
	domain.transformation()
	domain.writer()
	print('ok')
