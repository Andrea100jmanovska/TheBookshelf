from django.shortcuts import render
from store.models import Product
# Create your views here.


def home(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:9]
    return render(request, 'core/home.html',{
        'products': products
    })


def frontpage(request):
    return render(request, 'core/frontpage.html')


def about(request):
    return render(request, 'core/about.html')