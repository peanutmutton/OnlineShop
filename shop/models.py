from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="shop")

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop")
