from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=50)
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

class Estudents(BaseModel):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    class Meta:
        verbose_name = 'Estudents'
        verbose_name_plural = 'Estudents'
    def __str__(self):
        return self.name

class Sale(BaseModel):
    client = models.ForeignKey(Estudents, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
    def __str__(self):
        return self.client.name

class DetailSale(BaseModel):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'DetailSale'
        verbose_name_plural = 'DetailSales'
    def __str__(self):
        return self.product.name