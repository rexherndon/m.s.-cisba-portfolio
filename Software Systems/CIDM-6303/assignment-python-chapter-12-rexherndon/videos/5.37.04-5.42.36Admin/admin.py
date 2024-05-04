from django.contrib import admin
from .models import Product

# Register the model Product from the models.py file
admin.site.register(Product)


"""
For Django to know we want an administrative panel to manage Products, 
We must 'register' the products model. 
Products model must match the name in the models.py file
"from . models import Product"  means import the Product module from the models.py file 
in the current directory
"""
