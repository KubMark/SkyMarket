from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager, UserRoles


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    phone = PhoneNumberField()
    role = models.CharField(max_length=30, choices=UserRoles.choices, default=UserRoles.USER)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='user_pics/', default=None, blank=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()
