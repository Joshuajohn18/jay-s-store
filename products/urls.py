from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='products'),
 path('product/<int:id>/', views.show_product, name='show_product')
 ]