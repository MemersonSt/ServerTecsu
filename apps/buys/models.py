from django.db import models
from apps.products.models import Product


class ListaCompra(models.Model):
    id_shopping = models.IntegerField(primary_key=True, unique=True)
    code_students = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_shopping


class ItemCompra(models.Model):
    id = models.AutoField(primary_key=True)
    orden_compra = models.ForeignKey(ListaCompra, on_delete=models.CASCADE, related_name='product_detail', null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.products





