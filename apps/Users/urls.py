from django.urls import path
from .views import Login

urlpatterns = [
    # path('product/', ProductAPIView.as_view(), name = 'product_api')
    path('user/', Login.as_view(), name = 'login'),
]