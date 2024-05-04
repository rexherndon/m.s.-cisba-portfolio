# This is file products/urls.py
from django.urls import path
from . import views

urlpatterns = [path("", views.index)]

""" Notes: 
urlpatterns is a list of URLs and matching python function 
views.index means the index function in the views.py file
the '' in path('', )  means the root of the URL, e.g. index.html page
"""
