from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


# Register the model Product from the models.py file
admin.site.register(Product, ProductAdmin)


"""
This code created a ProductAdmin class to list only the fields: name, price, and stock
list_display informs Django to which fields to display. 
ProductsAdmin() must inherit from admin.ModelAdmin for build-in Django functionality to work
Django will automatically create an administrative panel for the Product model
admin.site.register(Product, ProductAdmin) means register the Products model and match it with the 
ProductAdmin class
If you have more models to register, you need multiple admin.site.register() lines for each model
"""
