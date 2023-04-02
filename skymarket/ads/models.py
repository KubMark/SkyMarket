from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

    image = models.ImageField(upload_to='ad_pics/', default=None, blank=True)
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, blank=True, null=True, default=None)


class Comment(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    text = models.CharField(max_length=800, blank=False, null=False, verbose_name='Ваш отзыв')
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, verbose_name='Объявление', on_delete=models.CASCADE)
