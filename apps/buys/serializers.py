from rest_framework import serializers
from .models import ListaCompra, ItemCompra
from apps.products.api.serializers import ProductSerializer


class OrdenCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCompra
        fields = (
            'id_shopping',
            'cedula',
            'uid',
            'total',

        )


class ItemOrdenCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompra
        fields = '__all__'


class CompraSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=50)
    product_detail = ItemOrdenCompraSerializer(many=True, required=False)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    cedula = serializers.CharField(max_length=20, required=False)


class CompraListSerializer(serializers.ModelSerializer):
    product_detail = ItemOrdenCompraSerializer(many=True)

    class Meta:
        model = ListaCompra
        fields = (
            'id_shopping',
            'cedula',
            'total',
            'date',
            'product_detail',
        )


class ItemCompraEstudiantilSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    products = ProductSerializer(many=True)
    quantity = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

class CompraEstudiantilSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=50)
    cedula = serializers.CharField(max_length=20)
    product_detail = ItemCompraEstudiantilSerializer(many=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()

