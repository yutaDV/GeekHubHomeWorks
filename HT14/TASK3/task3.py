"""HT 14 TASK  # 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
 інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл"""

import csv

import requests
from bs4 import BeautifulSoup

class Quotes:
	"""Клас збирає інформацію з сайту цитат та записує інформацію в файл"""
	base_url = "http://quotes.toscrape.com/"
	url = "/page/"
	all_quotes = []

	def get_information(self, number_page):
		"""Запит всієї інформації з сайту"""

		element = requests.get(f"{self.base_url}{self.url}{number_page}").content
		print(f"{self.base_url}{self.url}{number_page}")
		return element

	def get_inform_author(self, link):
		"""Отримання детальної інформації про автора"""

		res = requests.get(f"{self.base_url}{link}").content
		soup = BeautifulSoup(res, "lxml")
		birth_date = soup.find(class_="author-born-date").get_text()
		birth_place = soup.find(class_="author-born-location").get_text()
		description = soup.find(class_="author-description").get_text()
		return birth_date, birth_place, description

	def transformation(self):
		"""Розбір отриманої інформації та відбір потрібних категорій (інформація з 10 сторінок)"""

		for page in range(1, 2):
			element = self.get_information(page)
			soup = BeautifulSoup(element, "lxml")
			quotes = soup.find_all(class_="quote")
			print(quotes)
			for quote in quotes:
				birth_date, birth_place, description = self.get_inform_author(quote.find("a")["href"])
				self.all_quotes.append({
					"text": quote.find(class_="text").get_text(),
					"author": quote.find(class_="author").get_text(),
					"tags": quote.find(class_="tags").get_text(),
					"author's birthday": birth_date,
					"author's born location": birth_place,
					"description": description
				})
		return

	def writer(self):
		"""Запис отриманої інформації"""

		with open('basa.csv', 'w') as file:
			writer = csv.DictWriter(
				file, fieldnames=list(self.all_quotes[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
			writer.writeheader()
			for row in self.all_quotes:
				writer.writerow(row)


if __name__ == '__main__':
	quote = Quotes()
	quote.transformation()
	quote.writer()
	print('ok')
