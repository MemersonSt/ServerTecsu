from rest_framework import generics
from .models import Orden, OrdenDetalle
from .serializers import OrdenSerializer, OrdenDetalleSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class OrdenCreateApiView(generics.CreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class OrdenDetalleCreateApiView(generics.CreateAPIView):
    queryset = OrdenDetalle.objects.all()
    serializer_class = OrdenDetalleSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrdenDetalleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class OrdenListApiView(generics.ListAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    print(queryset)
