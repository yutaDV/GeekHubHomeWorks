""" HT 15 task 2. Написати програму, яка має складатися з трьох файлів/модулів.
    - rozetka_api.py, де створти клас RozetkaAPI, який буде містити 1 метод get_item_data,
      який на вхід отримує id товара з сайту розетки та повертає словник з такими даними:
      item_id (він же і приймається на вхід), title, old_price, current_price,
      href (лінка на цей товар на сайті), brand, category.
      Всі інші методи, що потрібні для роботи мають бути приватні/захищені.
    - data_operations.py з класами CsvOperations та DataBaseOperations.
      CsvOperations містить метод для читання даних. Метод для читання приймає аргументом шлях
      до csv файлу де в колонкі ID записані як валідні, так і не валідні id товарів з сайту.
      DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно приймає дані для запису.
      Всі інші методи, що потрібні для роботи мають бути приватні/захищені.
     - task.py - головний модуль, який ініціалізує і запускає весь процес.
    Суть процесу: читаємо ID товарів з csv файлу, отримуємо необхідні дані і записуємо їх в базу.
    Якщо ID не валідний/немає даних - вивести відповідне повідомлення і перейти до наступного."""

import data_operations
import rozetka_api


def start():

    data = data_operations.CsvOperations()
    list_id = data.read_data()
    for id_item in list_id:
        item = rozetka_api.RozetkaAPI(id_item)
        try:
            item_list = item.get_item_data()
        except:
            print(f'{id_item} is not correct')
        else:
            data = data_operations.DataBaseOperations(item_list)
            data.add_information()
            print(f'{id_item} was recorded')
    return 'ok'


if __name__ == '__main__':

    print(start())
