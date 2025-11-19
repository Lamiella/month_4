from django.urls import path
from . import views

urlpatterns = [
    path('all_things/', views.AllThingsView.as_view(), name='all_things'),
    path('home_things/', views.HomeThingView.as_view(), name='home_things'),
    path('accessories/', views.AccessoriesView.as_view(), name='accessories'),
    path('shoes/', views.ShoesView.as_view(), name='shoes'),
    path('dress/', views.DressView.as_view(), name='dress'),
    path('outerwear/', views.OuterwearView.as_view(), name='outerwear'),
]