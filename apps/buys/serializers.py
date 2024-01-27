from rest_framework import serializers
from .models import ListaCompra, ItemCompra


class OrdenCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCompra
        fields = (
            'id_shopping',
            'uid',
            'total',
        )


class ItemOrdenCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompra
        fields = '__all__'


class CompraSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=50)
    product_detail = ItemOrdenCompraSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

