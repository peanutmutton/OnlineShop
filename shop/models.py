from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


#Location.

class Oblast(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=20)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="shop")
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(District, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop")