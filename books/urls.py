from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookListView, name='book_list'),
    path('book_list/<int:id>/', views.bookDetailView, name='book_detail'),
    path('search/', views.searchView, name='search'),
]