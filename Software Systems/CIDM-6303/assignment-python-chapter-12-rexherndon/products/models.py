from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255) # CharField is kinda like VarChar or String.
    price = models.FloatField() # FloatField is just like Float
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) # This is the standard max length for URLs

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
