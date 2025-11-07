from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categoryList(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

def productList(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def categoryProducts(request,id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return render(request, 'shop/category_products.html', {'category': category, 'products': products})
