from django.urls import path
from . import views
urlpatterns = [
 path('<int:id>/add/', views.add_to_cart, name='cart.add'),
 path('', views.index, name=('cart.index')),
 path('clear/', views.clear, name='cart.clear'),
 path('purchase/', views.purchase, name='cart.purchase'),
 ]