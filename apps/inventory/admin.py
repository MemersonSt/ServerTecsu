from django.contrib import admin
from apps.inventory.models import Category, Brand, Product, Estudents, Sale, DetailSale

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Estudents)
admin.site.register(Sale)
admin.site.register(DetailSale)
