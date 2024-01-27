from django.db import models
from apps.base.models import BaseModel


# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

