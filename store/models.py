from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from Shop.settings import AUTH_USER_MODEL


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)



    def __str__(self):
        return f"{self.name} "


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    thumbnail = models.ImageField(upload_to="products")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} "

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f'{self.product.name}( {self.quantity}) {self.user.username}'


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} "


class Header(models.Model):
    title = models.CharField(max_length=110)
    description = models.TextField(max_length=400, blank=True, )
    picture = models.ImageField(upload_to="header", blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.description} {self.picture}"
