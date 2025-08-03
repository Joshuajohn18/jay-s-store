# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
def index(request):
    search_term = request.GET.get('search')
    
    if search_term:
        products = Product.objects.filter(name__icontains=search_term)
    else:
        products = Product.objects.all()
    
    template_data = {
        'title': 'products',
        'products': products
    }

    return render(request, 'products/index.html', {'template_data': template_data})

def show(request, id):
      product =  get_object_or_404(Product,id=id)
      template_data= {}
      template_data['title'] = product.name
      template_data['product'] = product
      return render (request, 'products/show.html',
 {'template_data': template_data})