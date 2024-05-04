# This file is pyshop/views.py NOT movies/view.py
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
