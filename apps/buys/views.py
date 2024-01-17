from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import OrdenCompra, ItemOrdenCompra
from apps.Users.models import Estudents
from .serializers import CompraSerializer


class ProcesarCompra(generics.CreateAPIView):
    queryset = OrdenCompra.objects.all()
    serializer_class = CompraSerializer

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)  # Convertir el JSON a un diccionario de Python
        serializer = CompraSerializer(data=data)  # Convertir el diccionario de Python a un objeto de tipo CompraSerializer

        if serializer.is_valid(): # Validar el objeto de tipo CompraSerializer
            # Obtenemos el codigo del estudiante
            codigo = serializer.validated_data['code_students']
            verificar = Estudents.objects.filter(code_students=codigo).exists()
            if verificar:
                # Obtenemos el id de la orden de compra
                id_orden_compra = serializer.validated_data['id_shopping']

                # Obtenemos el total de la orden de compra
                total = serializer.validated_data['total']

                # Creamos la orden de compra
                orden_compra = OrdenCompra.objects.create(id_shopping=id_orden_compra, code_students=codigo, total=total)
                productos = serializer.validated_data['product_detail']
                for producto_data in productos:
                    producto = ItemOrdenCompra.objects.create(
                        products=producto_data['products'],
                        quantity=producto_data['quantity'],
                        total=producto_data['total']
                    )

                    # Asignamos la orden de compra al item de orden compra
                    producto.orden_compra = orden_compra
                    producto.save()

                return Response({"message": "Orden de compra creada"}, status=status.HTTP_201_CREATED)

            else:
                return Response({"message": "El estudiante no existe"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def calcular_total(productos):
    total = 0
    for producto in productos:
        total += producto['total']
    return total

