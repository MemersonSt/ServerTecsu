from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', include('apps.Users.urls')),
    path('products/', include('apps.products.api.routers')),
    path('docs/', include_docs_urls(title='API TEC-SU')),
]
