from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import ListaCompra, ItemCompra
from apps.Users.models import Students
from apps.products.models import Product
from .serializers import CompraSerializer, CompraListSerializer, CompraEstudiantilSerializer, ProductSerializer,ItemOrdenCompraSerializer


class ProcesarCompra(generics.CreateAPIView):
    queryset = ListaCompra.objects.all()
    serializer_class = CompraSerializer

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)  # Convertir el JSON a un diccionario de Python
        serializer = CompraSerializer(data=data)  # Convertir el diccionario de Python a un objeto de tipo CompraSerializer

        if serializer.is_valid(): # Validar el objeto de tipo CompraSerializer
            try:
                codigo = serializer.validated_data['uid']  # Obtengo el codigo de la tarjeta del estudiante del request
                estudiante = Students.objects.get(uid=codigo)  # se obtiene el estudiante por el codigo de la tarjeta
                if estudiante:
                    total = serializer.validated_data['total']  # Obtenemos el total de la orden de compra
                    if estudiante.balance > total:
                        productos = serializer.validated_data['product_detail']
                        for producto_data in productos:
                            product = producto_data['products']
                            get_product = Product.objects.get(id=product.id)
                            if get_product.stock > 0:
                                get_product.stock -= producto_data['quantity']
                                if get_product.stock == 0:
                                    get_product.state = False
                                get_product.save()
                            else:
                                return Response({"message": "Producto no disponible"},
                                                status=status.HTTP_400_BAD_REQUEST)
                        restar_saldo = float(estudiante.balance) - float(total)
                        estudiante.balance = restar_saldo
                        estudiante.save()

                        orden_compra = ListaCompra.objects.create(uid=codigo, total=total) # Creamos la orden de compra

                        # Recorremos los productos de la orden de compra y restamos el stock


                        # Recorremos los productos de la orden de compra y los creamos en
                        for producto_data in productos:
                            producto = ItemCompra.objects.create(
                                products=producto_data['products'],
                                quantity=producto_data['quantity'],
                                total=producto_data['total']
                            )

                            # Asignamos la orden de compra al item de orden compra
                            producto.orden_compra = orden_compra
                            producto.save()

                        return Response({"message": "Orden de compra creada"}, status=status.HTTP_201_CREATED)

                    else:
                        return Response({"message": "Saldo insuficiente"}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    return Response({"message": "El estudiante no existe"}, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({"message": f"Error al crear la orden de compra", "error":f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

class ComprasEstudiante(generics.ListAPIView):
    serializer_class = CompraEstudiantilSerializer

    def get_queryset(self):
        uid = self.kwargs['uid']
        return ListaCompra.objects.filter(uid=uid)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = CompraListSerializer(queryset, many=True)
            serializer_data = [dict(data) for data in serializer.data]

            for data in serializer_data:
                for product_detail in data['product_detail']:
                    product_ids = product_detail['products']
                    products = Product.objects.filter(id=product_ids)
                    product_detail['products'] = ProductSerializer(products, many=True).data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Listar los item de compra
class ItemCompraListApiView(generics.ListAPIView):
    serializer_class = CompraListSerializer
    queryset = ListaCompra.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = CompraListSerializer(queryset, many=True)
            serializer_data = [dict(data) for data in serializer.data]

            for data in serializer_data:
                for product_detail in data['product_detail']:
                    product_ids = product_detail['products']
                    products = Product.objects.filter(id=product_ids)
                    product_detail['products'] = ProductSerializer(products, many=True).data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Listar solo item
class ListItem(generics.ListAPIView):
    serializer_class = ItemCompraListApiView
    queryset = ItemCompra.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemOrdenCompraSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)