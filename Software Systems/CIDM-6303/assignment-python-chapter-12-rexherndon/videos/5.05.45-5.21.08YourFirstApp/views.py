# This is file products/views.py
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello World")


"""
views defines dynamic webpages
views usually display data from a database, e.g. list of products
The function name matches the webpage name. 
The url.py module maps URLS to the views
"""
