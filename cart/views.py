from urllib import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required
@login_required
def purchase(request):
 cart = request.session.get('cart', {})
 product_ids = list(cart.keys())
 if (product_ids == []):
  return redirect('cart.index')
 product_in_cart = Product.objects.filter(id__in=product_ids)
 cart_total = calculate_cart_total(cart, product_in_cart)
 order = Order()
 order.user = request.user
 order.total = cart_total
 order.save()
 for product in product_in_cart:
  item = Item()
 item.product = product
 item.price = product.price
 item.order = order
 item.quantity = cart[str(product.id)]
 item.save()
 request.session['cart'] = {}
 template_data = {}
 template_data['title'] = 'Purchase confirmation'
 template_data['order_id'] = order.id
 return render(request, 'cart/purchase.html',
 {'template_data': template_data})

def index(request):
 cart_total = 0
 Product_in_cart = []
 cart = request.session.get('cart', {})
 Product_ids = list(cart.keys())
 if (Product_ids != []):
  Product_in_cart = Product.objects.filter(id__in=Product_ids)
 cart_total = calculate_cart_total(cart,
 Product_in_cart)
 template_data = {}
 template_data['title'] = 'Cart'
 template_data['product_in_cart'] = Product_in_cart
 template_data['cart_total'] = cart_total
 return render(request, 'cart/index.html',
 {'template_data': template_data})
def add_to_cart(request, id):
     get_object_or_404(Product, id=id)
     cart = request.session.get('cart', {})
     cart[id] = request.POST['quantity']
     request.session['cart'] = cart
     return redirect('home')
def clear(request):
  request.session['cart']= {}
  return redirect('cart.index')