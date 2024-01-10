from django.urls import path
from .views import OrdenCreateApiView, OrdenDetalleCreateApiView, OrdenListApiView

urlpatterns = [
    path('orden/create/', OrdenCreateApiView.as_view()),
    path('ordendetalle/create/', OrdenDetalleCreateApiView.as_view()),
    path('orden/list/', OrdenListApiView.as_view()),
]