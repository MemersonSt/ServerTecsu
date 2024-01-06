from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name

