"""HT 15 TASK  # 1.  Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт
   https://www.expireddomains.net/domain-lists/ (з ним будьте обережні :подмигивание:
   :череп_и_кости:), вибираєте будь-яку на ваш вибір доменну зону і парсите список
    доменів з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно
    ураховуючи пагінацію). Всі отримані значення зберегти в CSV файл."""

import csv

import requests
from bs4 import BeautifulSoup


class Domains:
	"""Клас збирає інформацію з сайту та записує її у файл"""
	base_url = "https://www.expireddomains.net/"
	url = "godaddy-closeout-domains/?"
	all_domains = []

	def get_information(self, number_page):
		"""Запит всієї інформації з сайту"""

		element = requests.get(f"{self.base_url}{self.url}{number_page}").text
		print(f"{self.base_url}{self.url}{number_page}")
		return element

	def parse(self, number_page):
		element = self.get_information(number_page)
		soup = BeautifulSoup(element, "html.parser")
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
	domain.transformation()
	domain.writer()
	print('ok')
