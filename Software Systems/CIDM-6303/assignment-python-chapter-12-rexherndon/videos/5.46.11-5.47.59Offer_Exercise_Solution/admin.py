from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "discount")


# Register the model Product and others from the models.py file
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)


""" Notes: 
class ProductAdmin(admin.ModelAdmin class) inherets functionality from admin.ModelAdmin class
list_display is a predefined attribute of the admin.ModelAdmin
list_display instructs Django to list only certain attributes from the models
Django's models are python classes with field attributes to store data about an object
Django's models automatically transfers the data to and from the database behind the scene
For more info, https://docs.djangoproject.com/en/3.1/intro/tutorial07/ 
"""
