from django.urls import path

from .views import product_details, products, get_new_id

app_name = 'products'

urlpatterns = [
    path('', products, name='list'),
    path('<int:pid>/', product_details, name='details'),
    path('new_id/', get_new_id, name='new_id'),
]
