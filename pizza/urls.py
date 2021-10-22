
from django.urls import path
from pizza.views import home, order,order_list

urlpatterns = [
    path('',home, name ='home'),
    path('order/',order, name ='order'),
    path('list/',order_list, name ='list')
]