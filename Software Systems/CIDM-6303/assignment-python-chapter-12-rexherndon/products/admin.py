from django.contrib import admin
# .models just means look for models in the current folder.
from .models import Product, Offer

# Register your models here.

# This gives us the ability to see all of the products and each of their fields instead of having to click on each Product object to see what it is.
class ProductAdmin(admin.ModelAdmin):
    # Fields found in products/models.py
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    # Fields found in products/models.py
    list_display = ('code', 'discount')

# Registers the Product and Offer class to the admin console so we can see it in http://127.0.0.1:8000/admin/
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)


