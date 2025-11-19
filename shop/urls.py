from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('categories/<int:id>/', views.CategoryProductsView.as_view(), name='category_products'),
]