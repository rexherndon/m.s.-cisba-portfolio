# a better name for this file would be config.py, since configuration settings for this app are here.

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
