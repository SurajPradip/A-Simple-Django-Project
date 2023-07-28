from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class customUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class loggers2(models.Model):
    username = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    url_path = models.CharField(max_length=200)
    auth = models.BooleanField(blank=True, null=True)


class products(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=None)
    SKU = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class productImage(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.product.name}---Image-{self.pk}"
