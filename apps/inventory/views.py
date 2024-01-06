from rest_framework import viewsets
from apps.inventory.models import Product
from apps.inventory.api.serializers import ProductSerializer, CategorySerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)
