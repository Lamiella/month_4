from django.shortcuts import render
from . import models
from django.views import generic


class AllThingsView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/all_things.html'
    context_object_name = 'things'

class HomeThingView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/home_things.html'
    context_object_name = 'home_things'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#Домашняя одежда')

class AccessoriesView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/accessories.html'
    context_object_name = 'accessories'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#Аксессуары')

class ShoesView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/shoes.html'
    context_object_name = 'shoes'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#Обувь')

class DressView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/dress.html'
    context_object_name = 'dress'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#Платья')

class OuterwearView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/outerwear.html'
    context_object_name = 'outerwear'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#Верхняя одежда')


#Все товары
# def all_thingsView(request):
#     if request.method == 'GET':
#         things = models.Products.objects.all()
#         return render(request, 'waikiki/all_things.html', {'things': things})

#Домашняя одежда
# def homeThingsView(request):
#     if request.method == 'GET':
#         home_things = models.Products.objects.filter(tags__name='#Домашняя одежда')
#         return render(request, 'waikiki/home_things.html', {'home_things':home_things})

#Аксессуары
# def accessoriesView(request):
#     if request.method == 'GET':
#         accessories = models.Products.objects.filter(tags__name='#Аксессуары')
#         return render(request, 'waikiki/accessories.html', {'accessories':accessories})

#Обувь
# def shoesView(request):
#     if request.method == 'GET':
#         shoes = models.Products.objects.filter(tags__name='#Обувь')
#         return render(request, 'waikiki/shoes.html', {'shoes':shoes})

#Платья
# def dressView(request):
#     if request.method == 'GET':
#         dress = models.Products.objects.filter(tags__name='#Платья')
#         return render(request, 'waikiki/dress.html', {'dress':dress})

#Верхняя одежда
# def outerwearView(request):
#     if request.method == 'GET':
#         outerwear = models.Products.objects.filter(tags__name='#Верхняя одежда')
#         return render(request, 'waikiki/outerwear.html', {'outerwear':outerwear})