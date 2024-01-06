from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', include('apps.Users.urls')),
    path('products/', include('apps.inventory.api.routers')),
]
