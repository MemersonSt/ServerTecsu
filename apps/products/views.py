from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import Product
from apps.products.api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                data = ProductSerializer(product).data
                return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"Error al crear el producto", "error":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                data = ProductSerializer(product).data
                return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Error al actualizar el producto", "error":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            product.state = False
            product.save()
            return Response({"message": "Producto eliminado"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Error al eliminar el producto", "error":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Error al listar los productos", "error":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
