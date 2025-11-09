from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def createOrderView(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm()

    return render(request, 'order/order_create.html', {'form': form})

def orderListView(request):
    if request.method == 'GET':
        order = models.Order.objects.all().order_by('-id')
    return render(request, 'order/order_list.html', {'order': order})

def updateOrderView(request, id):
    order_id = get_object_or_404(models.Order, id=id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=order_id)
        if form.is_valid:
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm(instance=order_id)
    return render(request, 'order/order_update.html', {'form': form, 'order_id': order_id})

def deleteOrder(request, id):
    order_id = get_object_or_404(models.Order, id=id)

    if request.method == 'POST':
        order_id.delete()
        return redirect('order_list')

    return render(request, 'order/order_confirm_delete.html', {'order': order_id})
