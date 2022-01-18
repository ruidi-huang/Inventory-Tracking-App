from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import csv

# Create your views here.

def index(request):
    items = Product.objects.all()
    items_count = items.count()
    context={
        'items_count': items_count
    }
    return render(request, 'dashboard/index.html', context)



def product(request):
    items = Product.objects.all()
    items_count = items.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context={
        'items': items,
        'form': form,
        'items_count': items_count
    }
    return render(request, 'dashboard/product.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    context={'item': item}
    return render(request, 'dashboard/product_delete.html', context)

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context={
        'form': form, 
    }
    return render(request, 'dashboard/product_update.html', context)




def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['name','category', 'quantity'])

    users = Product.objects.all().values_list('name','category', 'quantity')
    for user in users:
        writer.writerow(user)

    return response