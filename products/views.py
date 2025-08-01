# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product': product})