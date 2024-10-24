from django.contrib.auth.models import AbstractUser
from django.db import models

from Shop.settings import AUTH_USER_MODEL


class Shopper(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



