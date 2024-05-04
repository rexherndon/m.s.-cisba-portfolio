# This is file products/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World")


def new(request):
    return HttpResponse("New products")


"""
The products app now has two webpages: index and new
HttpsResponse published the text. Later the views will display 
data from a database. 
"""
