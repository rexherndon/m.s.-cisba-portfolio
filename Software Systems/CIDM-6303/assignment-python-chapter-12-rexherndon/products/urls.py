from django.urls import path
from . import views



urlpatterns = [
    # /products is the root of our path. It is our index page. AKA - path('')
    path('', views.index),
    path('new', views.new)
]

""" Notes: 
urlpatterns is a list of URLs and matching python function 
views.index means the index function in the views.py file
the '' in path('', )  means the root of the URL, e.g. index.html page
"""

""" Notes: 
views.index means the index function in the views.py file
The '' in path('', )  means the URL to the root of products app  http://127.0.0.1:8000/products/
view.new means the new function in the views.py file
The 'new' in path() means a subfolder called new in the urls http://127.0.0.1:8000/products/new
"""