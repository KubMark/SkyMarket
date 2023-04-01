from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# Здесь переопределить сериалайзер, который использует djoser
# для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone')


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["role"]
