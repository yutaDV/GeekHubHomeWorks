"""data_operations.py з класами CsvOperations та DataBaseOperations.
      CsvOperations містить метод для читання даних. Метод для читання приймає аргументом шлях
      до csv файлу де в колонкі ID записані як валідні, так і не валідні id товарів з сайту.
      DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно приймає дані для запису.
      Всі інші методи, що потрібні для роботи мають бути приватні/захищені."""

import csv
import sqlite3


class CsvOperations:
    data = []

    def read_data(self):

        with open('id_basa.csv') as f:
            reader = csv.reader(f)
            headers = next(reader)
            for row in reader:
                self.data.append(row[0])
        return self.data


class DataBaseOperations:

    def __init__(self, item_dict):
        self.item_dict = item_dict

    def add_information(self):

        params_list = []
        for kay, value in self.item_dict.items():
            params_list.append(value)
        conn = sqlite3.connect('BASA.db')
        cursor = conn.cursor()
        params = tuple(params_list)
        cursor.execute("INSERT INTO ITEMS VALUES (?,?,?,?,?,?,?)", params)
        conn.commit()
        conn.close()
        return
