from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"Kategoria: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    picture = models.ImageField(null=True, blank=True, upload_to='profile-picture')
    add_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    extra_info = models.CharField(max_length=200, default="", null=True)
    material = models.CharField(max_length=200, default="", null=True)
    condition = models.CharField(max_length=200, default="", null=True)
    amount = models.CharField(max_length=200, default="", null=True)
    color = models.CharField(max_length=200, default="", null=True)
    size = models.CharField(max_length=200, default="", null=True)
    is_available = models.BooleanField(default=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.id})

    def __str__(self):
        return f"Produkt: {self.name}, cena: {self.price}."

    def total_fav(self):
        return self.favourite.count()


class ExtraProductPicture(models.Model):
    extra_picture = models.ImageField(upload_to='profile-picture', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Zdjecie [{self.id}]"
