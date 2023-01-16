from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    id_product = models.IntegerField(blank=False)
    title = models.CharField(max_length=50, default= 'Default title')
    price= models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    brand = models.CharField(max_length=50, default= 'Default title')
    link = models.CharField(max_length=50, default= 'Default link')

    def __str__(self):
        return f'{self.title} {self.brand}'

    def get_absolute_url(self):
        return reverse('app:product_detail',
                       args=[self.id_product])