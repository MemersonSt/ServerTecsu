from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tecsu/', include('apps.Users.urls')),
    path('tecsu/', include('apps.products.api.routers')),
    path('tecsu/', include('apps.transactions.urls')),
    path('tecsu/', include('apps.shoppingCart.urls')),
    path('docs/', include_docs_urls(title='API TEC-SU')),
]
