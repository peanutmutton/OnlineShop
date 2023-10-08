from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="shop")