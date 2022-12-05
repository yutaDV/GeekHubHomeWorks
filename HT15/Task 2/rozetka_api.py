"""rozetka_api.py, де створти клас RozetkaAPI, який буде містити 1 метод get_item_data,
      який на вхід отримує id товара з сайту розетки та повертає словник з такими даними:
      item_id (він же і приймається на вхід), title, old_price, current_price,
      href (лінка на цей товар на сайті), brand, category.
      Всі інші методи, що потрібні для роботи мають бути приватні/захищені."""


import requests

class RozetkaAPI:

    url = "https://rozetka.com.ua/api/product-api/v4/goods/get-main?front-type=xl&country=UA&lang=ua&goodsId="
    base_url = None

    def __init__(self, id_product):
        self.id_product = id_product

    def get_item_data(self):

        self.base_url = self.url + self.id_product
        page = requests.get(self.base_url).json()
        item_information = page.get("data")
        item_date = {}
        for kay, value in item_information.items():
            if kay == 'id':
                item_date['item_id'] = value
            if kay == 'title':
                item_date['title'] = value
            if kay == 'price':
                item_date['current_price'] = value
            if kay == 'old_price':
                item_date['old_price'] = value
            if kay == 'href':
                item_date['href'] = value
            if kay == 'brand':
                item_date['brand'] = value
            if kay == 'category':
                item_date['category'] = f"{value}"
        return item_date

