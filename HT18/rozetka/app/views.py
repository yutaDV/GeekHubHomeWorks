from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app/product/list.html', context={'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id,)
    return render(request, 'app/product/detail.html', context={'product': product})

