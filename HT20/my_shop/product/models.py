from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(blank=False)
    title = models.CharField(max_length=50, default= 'Default title')
    price= models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default='0,00')
    brand = models.CharField(max_length=50, default= 'Default title')
    url= models.CharField(max_length=50, default= 'Default link')
    in_stock = models.BooleanField()


class ScrapingTask(models.Model):
    New_ids = models.TextField(max_length=1000, default="Enter ids here")

    def __str__(self):
        return self.New_ids