from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


"""
Models are classes representing objects in OOP. 
Models also store data about the object in a database
Django automatically manages data transfer to and from models and the database
The model called Products  has four class attributes: name, price, stock, image_url
The model called Offers has three class attributes: code, description, and discount. 
Django models must inheret from models.Model to provide built-in functionality
Learn more about models at https://docs.djangoproject.com/en/3.1/topics/db/models/
"""
