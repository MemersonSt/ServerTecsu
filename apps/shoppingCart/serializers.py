from rest_framework import serializers
from .models import Orden, OrdenDetalle


class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'


class OrdenDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetalle
        fields = '__all__'