# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import OrdenCompra, ItemOrdenCompra
# from .serializers import OrdenCompraSerializer, ItemOrdenCompraSerializer
#
#
# class OrdenCompraList(generics.ListCreateAPIView):
#     queryset = OrdenCompra.objects.all()
#     serializer_class = OrdenCompraSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = OrdenCompraSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'message': 'Error al crear la orden de compra'},
#                         status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, *args, **kwargs):
#         orden_compra = OrdenCompra.objects.all()
#         serializer = OrdenCompraSerializer(orden_compra, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class OrdenCompraDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrdenCompra.objects.all()
#     serializer_class = OrdenCompraSerializer
#
#     def get(self, request, *args, **kwargs):
#         try:
#             orden_compra = OrdenCompra.objects.get(id_shopping=kwargs['pk'])
#             serializer = OrdenCompraSerializer(orden_compra)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except OrdenCompra.DoesNotExist:
#             return Response({'message': 'No existe la orden de compra'},
#                             status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, *args, **kwargs):
#         try:
#             orden_compra = OrdenCompra.objects.get(id_shopping=kwargs['pk'])
#             serializer = OrdenCompraSerializer(orden_compra, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         except OrdenCompra.DoesNotExist:
#             return Response({'message': 'No existe la orden de compra'},
#                             status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, *args, **kwargs):
#         try:
#             orden_compra = OrdenCompra.objects.get(id_shopping=kwargs['pk'])
#             orden_compra.delete()
#             return Response({'message': 'Orden de compra eliminada'},
#                             status=status.HTTP_200_OK)
#         except OrdenCompra.DoesNotExist:
#             return Response({'message': 'No existe la orden de compra'},
#                             status=status.HTTP_404_NOT_FOUND)
#
#
# class ItemOrdenCompraList(generics.ListCreateAPIView):
#     queryset = ItemOrdenCompra.objects.all()
#     serializer_class = ItemOrdenCompraSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = ItemOrdenCompraSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'message': 'Error al crear el item de la orden de compra'},
#                         status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, *args, **kwargs):
#         item_orden_compra = ItemOrdenCompra.objects.all()
#         serializer = ItemOrdenCompraSerializer(item_orden_compra, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
