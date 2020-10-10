from django.db import models
from .category import Category


class Product(models.Model):
    brandname = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    variety = models.CharField(max_length=50, default=None)
    weight = models.CharField(max_length=50, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=1)

    image = models.ImageField(upload_to='products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)

        else:
            return Product.get_all_products()
