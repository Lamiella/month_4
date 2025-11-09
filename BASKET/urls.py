from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.orderListView, name='order_list'),
    path('order_list/<int:id>/update/', views.updateOrderView, name='update_order'),
    path('order_list/<int:id>/delete/', views.deleteOrder, name='delete_order'),
    path('create_order/', views.createOrderView, name='create_order')
]