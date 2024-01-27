from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import ListaCompra, ItemCompra
from apps.Users.models import Students
from apps.products.models import Product
from .serializers import CompraSerializer


class ProcesarCompra(generics.CreateAPIView):
    queryset = ListaCompra.objects.all()
    serializer_class = CompraSerializer

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)  # Convertir el JSON a un diccionario de Python
        serializer = CompraSerializer(data=data)  # Convertir el diccionario de Python a un objeto de tipo CompraSerializer

        if serializer.is_valid(): # Validar el objeto de tipo CompraSerializer
            try:
                # Obtenemos el codigo de la tarjeta del estudiante
                codigo = serializer.validated_data['uid']
                estudiante = Students.objects.get(uid=codigo)  # Obtenemos el estudiante por el codigo de la tarjeta
                if estudiante:
                    total = serializer.validated_data['total']  # Obtenemos el total de la orden de compra
                    if estudiante.balance > total:
                        restar_saldo = float(estudiante.balance) - float(total)
                        estudiante.balance = restar_saldo
                        estudiante.save()

                        orden_compra = ListaCompra.objects.create(uid=codigo, total=total) # Creamos la orden de compra
                        productos = serializer.validated_data['product_detail']

                        # Recorremos los productos de la orden de compra y restamos el stock
                        for producto_data in productos:
                            product = producto_data['products']
                            get_product = Product.objects.get(id=product.id)
                            get_product.stock -= producto_data['quantity']
                            get_product.save()

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



