from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class CustomUser(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    password = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "password"]

    def __str__(self):
        return self.first_name + " " + self.last_name
