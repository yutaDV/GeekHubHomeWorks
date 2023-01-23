import subprocess
import os

from django.shortcuts import render, get_object_or_404

from .models import Product, ScrapingTask
from .forms import NewIdsForm
from .add_products.rozetka_api import product_params
from cart.forms import CartAddProductForm


def products(request):
    all_products = Product.objects.all()
    return render(request, 'product/product_list.html', context={'all_products': all_products})

def product_details(request, pid):
    product = get_object_or_404(Product, id=pid)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/product_details.html', context={'product': product, 'cart_product_form': cart_product_form})

def get_new_id(request):
    if request.method == "POST":
        form = NewIdsForm(request.POST)
        if form.is_valid():
            form.save()
            subprocess.Popen(["python", "add_products/rozetka_scraper.py"])
    else:
        form = NewIdsForm()
    return render(request, 'product/add_products.html', context={'form': form})


def new_product(id_product):
    details = product_params(id_product) #'363882639'
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

