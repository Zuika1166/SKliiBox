from django.shortcuts import render
from timeit import default_timer
from django.contrib.auth.models import Group
from .models import Product, Order

# Create your views here.
def shop_render(request):
    products = [
        ('LapTop', 215000),
        ('DeskTop', 501000),
        ('IPphone', 89000),
        ('EarPods', 12000),
    ]

    context = {
        'time_run': default_timer,
        'products': products
    }
    return render(request, 'ShopApp/home.html', context=context)


def groups_list(request):
    context = {
        'groups': Group.objects.all(),
    }

    return render(request, 'ShopApp/groups.html', context=context)


def products_list(request):
    context = {
        "products": Product.objects.all(), 
    }


    return render(request, "ShopApp/products_list.html", context=context)


def orders_list(request):
    context = {
        "orders": Order.objects.all(), 
    }
    print(Order.objects.all())
    return render(request, 'ShopApp/orders.html', context=context)