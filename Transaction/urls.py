from django.urls import path

from . import views

urlpatterns = [
    path('transactions', views.TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>', views.TransactionDetail.as_view(), name='transaction-detail')
]
