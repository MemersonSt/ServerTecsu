from django.urls import path
from .views import TransactionCreateView, TransactionListView

urlpatterns = [
    path('transaction/create/', TransactionCreateView.as_view(), name = 'transaction_create'),
    path('transaction/list/', TransactionListView.as_view(), name = 'transaction_list'),
]