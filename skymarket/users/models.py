from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles(models.TextChoices):
    ADMIN = 'admin'
    MEMBER = 'member'


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    phone = PhoneNumberField()
    role = models.CharField(max_length=30, choices=UserRoles.choices, default=UserRoles.MEMBER)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='user_pics/', default=None, blank=True)
