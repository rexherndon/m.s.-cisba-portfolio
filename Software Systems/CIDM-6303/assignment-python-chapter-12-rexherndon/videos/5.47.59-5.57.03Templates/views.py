# This is file products/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    # for getting all products in the database
    products = Product.objects.all()
    # pass the products variable through a dictionary to render()
    # render() also needs to know the name of the template index.html
    return render(request, "index.html", {"products": products})


def new(request):
    return HttpResponse("New products")


""" Notes. Other useful objects for getting data from the database
products = Product.objects.filter() # for getting a subset of products based on a critiera
product = Product.objects.get() # for getting a single product based on primary key
products = Product.objects.save()  #for adding or updating a product

In render(), index.html is the name of our template
{'products': products}  is a dictionary key:value pair
                        'products' can be any name you choose
            : products}  is the name of the products variable defined earlier

In index.html: 
    {% %}  is called a 'template tag' A tempate tag let us run python code in the html template
    A template tag contaings python commands, name of Django objects, and variables we can access
    
"""
