from decimal import Decimal
from django.conf import settings

from product.models import Product


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """ Додати продукт до корзини."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # оновити сесію
        self.session[settings.CART_SESSION_ID] = self.cart
        #  зміненно
        self.session.modified = True

    def remove(self, product):
        """ видалення з корзини"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """ перевірка товарів в кошику """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price']) #перетворення в число
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_quantity(self):
        """ скільки товарів в кошику(всього) """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ загальна вартість """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        """очищення кошику"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True