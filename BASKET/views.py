from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

class CreateOrderView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm
    template_name = 'order/order_create.html'
    success_url = '/order_list/'

class OrderListView(generic.ListView):
    model = models.Order
    template_name = 'order/order_list.html'
    context_object_name = 'order'
    ordering = ['-id']

class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    template_name = 'order/order_update.html'
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.Order, id=order_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderUpdateView, self).form_valid(form=form)

class DeleteOrderView(generic.DeleteView):
    template_name = 'order/order_confirm_delete.html'
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.Order, id=order_id)


# def createOrderView(request):
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST, request.FILES)
#         if form.is_valid:
#             form.save()
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm()
#
#     return render(request, 'order/order_create.html', {'form': form})
#
# def orderListView(request):
#     if request.method == 'GET':
#         order = models.Order.objects.all().order_by('-id')
#     return render(request, 'order/order_list.html', {'order': order})
#
# def updateOrderView(request, id):
#     order_id = get_object_or_404(models.Order, id=id)
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST, instance=order_id)
#         if form.is_valid:
#             form.save()
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm(instance=order_id)
#     return render(request, 'order/order_update.html', {'form': form, 'order_id': order_id})
#
# def deleteOrder(request, id):
#     order_id = get_object_or_404(models.Order, id=id)
#
#     if request.method == 'POST':
#         order_id.delete()
#         return redirect('order_list')
#
#     return render(request, 'order/order_confirm_delete.html', {'order': order_id})