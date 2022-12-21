"""Викорисовуючи Scrapy, написати скрипт, який буде приймати на вхід назву
та ID категорії (у форматі назва/id/) із сайту https://rozetka.com.ua і буде
 збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд,
 категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад,
 якщо передана категорія mobile-phones/c80003/, то файл буде називатися c80003_products.csv)
 для виконання завдання взято категорію навушники -  headphones/c80027, """

import subprocess

from spiders.rozetka_api import category

if __name__ == "__main__":
    name_file = category.split('/')[1]
    subprocess.run(["scrapy", "crawl", "rozetka_api", "-O", f"{name_file}_products.csv"])