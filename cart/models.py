from django.db import models
from products.models import Product
# Create your models here.
from django.contrib.auth.models import User
class Order(models.Model):
 id = models.AutoField(primary_key=True)
 total = models.IntegerField()
 date = models.DateTimeField(auto_now_add=True)
 user = models.ForeignKey(User,
 on_delete=models.CASCADE)
 def __str__(self):
  return str(self.id) + ' - ' + self.user.username
 
class Item(models.Model): 
  id = models.AutoField(primary_key=True)
  price = models.IntegerField()
  quantity = models.IntegerField()
  order = models.ForeignKey(Order,
  on_delete=models.CASCADE)
  product = models.ForeignKey(Product,
 on_delete=models.CASCADE)
  def __str__(self):
   return str(self.id) + ' - ' + self.product.name