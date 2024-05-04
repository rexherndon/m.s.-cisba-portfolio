from django.http import HttpResponse
from django.shortcuts import render
# This is so we can use our models in our webpages!
from .models import Product


# Create your views here.

# Index in this case refers to the default products page. Right now it's http://127.0.0.1:8000/products
def index(request):
    # Lists all objects in our products table.
    products = Product.objects.all()
    # Renders/returns index.html and our product info after sending the http request to us. Products is referred to as our 'context'
    return render(request, 'index.html', 
                    {'products': products})


# http://127.0.0.1:8000/products/new
def new(request):
    return HttpResponse('New Products')

"""
views defines dynamic webpages
views usually display data from a database, e.g. list of products
The function name matches the webpage name. 
The url.py module maps URLS to the views
"""

"""
The products app now has two webpages: index and new
HttpsResponse published the text. Later the views will display 
data from a database. 
"""