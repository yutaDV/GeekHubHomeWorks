import csv
import requests


class CsvFile:
	"""Клас отримує та читає csv файл"""
	url = "https://robotsparebinindustries.com/orders.csv"

	def __get_file(self):
		result = requests.get(self.url)
		return result

	def read_file(self):
		data = self.__get_file()
		base = []
		content = data.content.decode('iso-8859-1')
		for line in csv.reader(content.splitlines()):
			if line[1] != 'Head':
				base.append(line[1:])
		return base


if __name__ == '__main__':
	file = CsvFile()
	print(file.read_file())
