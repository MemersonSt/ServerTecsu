from django.urls import path
from .views import ProcesarCompra, ComprasEstudiante, ItemCompraListApiView, ListItem


urlpatterns = [
    path('procesar-compra/', ProcesarCompra.as_view(), name='procesar_compra'),
    path('compras-estudiante/<str:cedula>/', ComprasEstudiante.as_view(), name='compras_estudiante'),
    path('item-compra/', ItemCompraListApiView.as_view(), name='item_compra'),
    path('list-item/', ListItem.as_view(), name='list_item')
]
