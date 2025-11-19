from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views import generic

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'

class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

class CategoryProductsView(generic.ListView):
    model = Product
    template_name = 'shop/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['id'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

# def categoryList(request):
#     categories = Category.objects.all()
#     return render(request, 'shop/categories.html', {'categories': categories})
#
# def productList(request):
#     products = Product.objects.all()
#     return render(request, 'shop/products.html', {'products': products})
#
# def categoryProducts(request,id):
#     category = get_object_or_404(Category, id=id)
#     products = category.products.all()
#     return render(request, 'shop/category_products.html', {'category': category, 'products': products})
