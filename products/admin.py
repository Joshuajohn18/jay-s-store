from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']  # <-- this sorts the list by 'name'
    list_display = ['name']  # <-- this shows the 'name' column in the admin list view
    search_fields= ['name']
admin.site.register(Product, MovieAdmin)
admin.site.register(Category)
