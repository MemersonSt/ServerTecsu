# from rest_framework import serializers
# from .models import Product, OrdenCompra, ItemOrdenCompra
#
#
# class ItemOrdenCompraSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemOrdenCompra
#         fields = '__all__'
#
#
# class OrdenCompraSerializer(serializers.ModelSerializer):
#     product_detail = ItemOrdenCompraSerializer(many=True)
#
#     class Meta:
#         model = OrdenCompra
#         fields = '__all__'
#
