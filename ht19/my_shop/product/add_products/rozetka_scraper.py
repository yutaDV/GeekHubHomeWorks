import sys
import os
import django

from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapper_app.settings")


if __name__ == '__main__':
    django.setup()

from rozetka_api import  product_params
from  product.views import Product, ScrapingTask


def new_product(id_product):
    details = product_params(id_product)
    if details:
        if details['in_stock'] == '0':
            active = False
        else:
            active = True
        Product.objects.update_or_create(product_id=details['item_id'],
                                                   defaults={
                                                       'title': details['title'], 'price': details['current_price'],
                                                       'old_price': details['old_price'], 'brand': details['brand'],
                                                       'url': details['href'], 'in_stock': active}
                                                   )

bufer = (ScrapingTask.objects.all().last()).New_ids
new_procucts_id = bufer.split('\n')
for product_id in new_procucts_id:
    new_product(product_id)




