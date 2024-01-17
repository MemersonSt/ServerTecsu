from django.urls import path
from .views import ProcesarCompra


urlpatterns = [
    path('procesar-compra/', ProcesarCompra.as_view(), name='procesar_compra'),
]
