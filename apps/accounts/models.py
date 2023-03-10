from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password

from phonenumber_field.modelfields import PhoneNumberField
from apps.accounts.managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(
        max_length=128,
        unique=True,
        verbose_name="Email Address",
    )

    first_name = models.CharField(
        max_length=128,
        null=True,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=128,
        null=True,
        verbose_name="Last Name",
    )

    phone_number = PhoneNumberField(
        unique=True,
        null=True,
        verbose_name="Mobile Number",
    )

    image = models.ImageField(
        upload_to='images/',
        null=True,
        verbose_name='Custom User Image',
    )

    password = models.CharField(
        max_length=128,
        validators=[validate_password],
        verbose_name="Password",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def my_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'


class Address(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='address',
        verbose_name="Custom Users",
    )

    address = models.CharField(
        max_length=256,
        null=True,
        verbose_name="Address",
    )

    city = models.CharField(
        max_length=128,
        null=True,
        verbose_name="City",
    )

    country = models.CharField(
        max_length=128,
        null=True,
        verbose_name="Country",
    )

    zip_code = models.CharField(
        max_length=5,
        null=True,
        validators=[RegexValidator('^[0-9]{5}$', ('Invalid postal code.'))],
        verbose_name="Zip Code",
    )

    def __str__(self):
        return self.city


class Otp(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='otp',
        verbose_name="Custom Users",
    )

    otp = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', ('Invalid postal code.'))],
        verbose_name="One-time password",
    )

    secret_key = models.CharField(
        max_length=40,
        verbose_name='Random Base 32',
    )

    def __str__(self):
        return self.otp
