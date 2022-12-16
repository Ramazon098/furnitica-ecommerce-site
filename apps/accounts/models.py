from re import L
from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class CustomUsers(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = PhoneNumberField(verbose_name="Mobile Number")
    first_name = models.CharField(max_length=128, verbose_name="First Name")
    last_name = models.CharField(max_length=128, verbose_name="Last Name")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    @property
    def my_name(self):
        return f"{self.first_name} {self.last_name}"
