# from django.db import models
# from apps.products.models import Product
#
# # Create your models here.
# class OrdenCompra(models.Model):
#     id_shopping = models.IntegerField(primary_key=True, unique=True)
#     code_students = models.CharField(max_length=50)
#     # product_detail = models.ManyToManyField(Product, through='ItemOrdenCompra')
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(auto_now_add=True)
#     state = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.id_shopping
#
#
# class ItemOrdenCompra(models.Model):
#     id = models.AutoField(primary_key=True)
#     code = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='product_detail', null=True, blank=True)
#     products = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(auto_now_add=True)
#     state = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.products


