"""Викорисовуючи Scrapy, написати скрипт, який буде приймати на вхід назву
та ID категорії (у форматі назва/id/) із сайту https://rozetka.com.ua і буде
 збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд,
 категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад,
 якщо передана категорія mobile-phones/c80003/, то файл буде називатися c80003_products.csv)
 категорії для прикладів all-tv/c80037/, headphones/c80027, """

import subprocess

import spiders.rozetka_api

if __name__ == "__main__":
    name_category = spiders.rozetka_api.category.split('/')
    name_file = name_category[0] + '_' + name_category[1]
    subprocess.run(["scrapy", "crawl", "rozetka_api", "-o", f"{name_file}.csv"])