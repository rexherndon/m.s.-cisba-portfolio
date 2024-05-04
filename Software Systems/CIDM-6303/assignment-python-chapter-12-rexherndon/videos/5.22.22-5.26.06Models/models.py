from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


"""
Models are classes representing objects in OOP. 
Models also store data about the object in a database
Django automatically manages data transfer to and from models and the database
This model is called Products and has four class attributes: name, price, stock, image_url
Django models must inheret from models.Model to provide built-in functionality
To learn move visit https://docs.djangoproject.com/en/3.1/topics/db/models/
"""
