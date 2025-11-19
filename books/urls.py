from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]