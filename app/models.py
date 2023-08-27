from django.db import models


class Product(models.Model):
    Item = models.CharField(max_length=255)
    Price = models.FloatField()