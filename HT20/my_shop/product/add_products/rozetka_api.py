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
            if kay == 'sell_status':
                if value == 'active':
                    item_date['in_stock'] = 1
                else:
                    item_date['in_stock'] = 0
        return item_date


def product_params(id_product):
    item = RozetkaAPI(id_product)
    try:
        item_list = item.get_item_data()
    except:
        return False
    else:
        return item_list

if __name__ == '__main__':

    print(product_params('363882639'))
