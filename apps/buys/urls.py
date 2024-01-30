from django.urls import path
from .views import ProcesarCompra, ComprasEstudiante


urlpatterns = [
    path('procesar-compra/', ProcesarCompra.as_view(), name='procesar_compra'),
    path('compras-estudiante/<str:uid>/', ComprasEstudiante.as_view(), name='compras_estudiante'),
]
