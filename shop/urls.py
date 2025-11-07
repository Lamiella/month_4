from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categoryList, name='categories'),
    path('products/', views.productList, name='products'),
    path('categories/<int:id>/', views.categoryProducts, name='category_products'),
]